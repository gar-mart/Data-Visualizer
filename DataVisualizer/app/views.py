from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponse
from . import models


def simple_view(request):
    return render(request,'app/example.html')

def variable_view(request):

    vari={'fname':'ros','lname':'od'}

    return render(request,'app/variable.html',context=vari)


def sports_view(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/sports.html',
        {
            'title':'sports Page',
            'year':datetime.now().year,
        }
    )



def home(request):
    """Renders the home page."""
    import requests
    import json
    ticker = ""

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_c0d481c48bf649358c1c29030c400e0d")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error------"

        return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'api':api,
        }
        )
       

    else:
        return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'ticker':"enter ticker above",
        }
    )
            

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        } 
    )
