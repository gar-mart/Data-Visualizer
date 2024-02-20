from django.shortcuts import render
from django.db import connection
from django.db import models
from .models import LineChart, ConditionColumns, ug_TableNames, ug_TableColumns
from django.contrib.auth.decorators import login_required

import json
import pandas as pd
from django.core.serializers import serialize

from django.http import JsonResponse



    
def get_user_table_columns(request):
    table_name = request.GET.get('table_name')
    user_id = request.GET.get('user_id')  
    
    if not table_name or not user_id:
        return JsonResponse([], safe=False)

    columns = call_GetUserTableColumnsByUser(user_id)
    
    return JsonResponse(columns, safe=False)


def call_GetUserTableColumnsByUser(user_id):
    with connection.cursor() as cursor:
        cursor.execute("EXEC ugTables.GetUGTableColumnsByUserId %s", [user_id])
        rows = cursor.fetchall()

    return [ug_TableColumns(ug_table_id=str(row[0]), column_name=str(row[1]), data_type=str(row[2]))  for row in rows]




def call_Get_ugTableNamesByUser(user_id):
    with connection.cursor() as cursor:

        cursor.execute("EXEC ugTables.GetUGTableNamesByUserId %s",[user_id])  
        rows = cursor.fetchall()

    return [ug_TableNames(table_name=str(row[0]), ug_table_id=str(row[1])) for row in rows]



def call_line_chart_results(y_axis, x_axis, table_name, user_id):
    with connection.cursor() as cursor:

        cursor.execute("EXEC Visualize.VisualizeChart %s,%s,%s,%s",[y_axis, x_axis, table_name, user_id])  
        rows = cursor.fetchall()

    return [LineChart(YAxis=str(row[0]), XAxis=str(row[1])) for row in rows]





@login_required
def visualize(request):
    table_results = None
    table_results_json = None
    user_id = request.user.id 
    is_post = False

    ug_table_names = call_Get_ugTableNamesByUser(user_id)
    ug_table_names_ids_json = json.dumps([{'table_name': item.table_name, 'ug_table_id': item.ug_table_id} for item in ug_table_names])


    columns_results = call_GetUserTableColumnsByUser(user_id)
    columns_results_json = serialize('json', columns_results)

    if request.method == "POST":
        y_axis = request.POST.get('y_axis')
        x_axis = request.POST.get('x_axis')
        table_name = request.POST.get('table_name')

        table_results = call_line_chart_results(y_axis, x_axis, table_name, user_id) 
        table_results_json = serialize('json', table_results)
        ug_table_names_json = serialize('json', ug_table_names)
        is_post = True


    context = {
        'table_results_json': table_results_json,
        'ug_table_names_ids_json': ug_table_names_ids_json,
        'columns_results_json': columns_results_json,
        'is_post' : is_post
    }

    return render(request, 'Visualize/visualize.html', context)





def view_ugTable_by_ugTableId(ug_table_id, page): 
    with connection.cursor() as cursor:
        cursor.execute(";EXEC ugTables.ViewUGTableByUGTableId %s, %s",[ug_table_id, page])  
        column_names = [col[0] for col in cursor.description]
        data = cursor.fetchall()
    return column_names, data

def get_ugTable_total_count_by_ugTableId(ug_table_id):
    with connection.cursor() as cursor:
        cursor.execute(";EXEC ugTables.GetUGTablesTotalCountById %s",[ug_table_id])  
        total_rows_count = cursor.fetchone()[0] 
    return total_rows_count 
    
    


@login_required
def view_table(request, ug_table_id, page):

    columns, data = view_ugTable_by_ugTableId(ug_table_id, page)
    total_rows_count = get_ugTable_total_count_by_ugTableId(ug_table_id)
    
    rows_per_page = 50
    total_pages = (total_rows_count + rows_per_page - 1) // rows_per_page
    page_range = range(1, total_pages + 1)


    return render(request, 'Visualize/view_table.html', {'columns': columns, 
                                                         'data': data,
                                                         'page_range': page_range,
                                                         'current_page': int(page),
                                                         'ug_table_id' : int(ug_table_id)
                                                         })



