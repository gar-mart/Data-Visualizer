from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Profile
from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

from django.contrib.auth.models import User
from django.urls import conf, is_valid_path
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import ReviewForm
from .models import Review
from django.views import View

import pandas as pd
import random
from .forms import UploadFileForm
from .models import Document
from .forms import DocumentForm
import pyodbc


def generate_table_from_file(df, ug_table_name, category_name, user_id):
   column_defs = []

   # Guess the data types of columns
   for col in df.columns:
       if df[col].dtype == 'int64':
           column_defs.append((col, 'INT'))
       elif df[col].dtype == 'float64':
           column_defs.append((col, 'FLOAT'))
       elif df[col].dtype == 'bool':
           column_defs.append((col, 'BIT'))
       else:
           column_defs.append((col, 'NVARCHAR(255)'))

   
   
   with connection.cursor() as cursor:
      
       params = [ug_table_name, category_name, user_id, column_defs]
       cursor.execute(";EXEC ugTables.CreateUGTable %s, %s, %s, %s", params)

@login_required
def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()

            # Extract table name
            table_name = form.cleaned_data['table_name']
            category_name = form.cleaned_data['category_name']
            u_id = request.user.id 


            # Determine file type and read data using pandas
            if document.upload.name.endswith('.csv'):
                data = pd.read_csv(document.upload.path)
            elif document.upload.name.endswith('.xls') or document.upload.name.endswith('.xlsx'):
                data = pd.read_excel(document.upload.path)
            elif document.upload.name.endswith('.json'):
                data = pd.read_json(document.upload.path)
            else:
                # Invalid file type
                messages.error(request, 'Invalid file type.')
                return render(request, 'upload.html', {'form': form})

            with connection.cursor() as cursor:
            
                 table_exists = False
                 params = [table_name, category_name, u_id, table_exists]
                 cursor.execute(";EXEC ugTables.ugTableExists @uAssignedName = %s, @categoryName = %s, @userId = %s, @TableExists = %s OUTPUT", params)
                 
                 while cursor.nextset():
                     pass
                 table_exists = params[-1]
                 
                 if not table_exists:
                     generate_table_from_file(data, table_name, category_name, u_id)
                 params = [u_id, category_name, table_name, document.upload.path]
                 sql = ";EXEC Users.InsertFromCSV %s, %s, %s, %s"
                 cursor.execute(sql, params)

            return render(request, 'users/upload.html', {'form': form})
    else:
        form = DocumentForm()
    return render(request, 'users/upload.html', {'form': form})




from django.views.decorators.http import require_POST
from django.db import connection



def profiles(request):


    fmeth = request.method
    
    user_name = request.session.get('user_name', None) 
    number = 34 
    

    return render(request, 'users/profiles.html', {
        'user_name': user_name,
        'fmeth': fmeth,
        'number' : number
    })




def loginPage (request):
    u_id = request.user.id

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
       
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'users/profiles.html')
        

        else:
            messages.error(request, 'Username OR password is incorrect')
            return redirect('login')



    return render(request, 'users/login_register.html',{'u_id': u_id})



@login_required
def my_assets(request):

     with connection.cursor() as cursor:
        cursor.execute(";EXEC Users.GetMyAssets %s", [request.user.id])
        ugtables_results = cursor.fetchall()
    
     context = {
        'ugtables': ugtables_results if ugtables_results else None,
     }



     return render(request, 'users/my_assets.html', context)




def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')



def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'users/register.html')















