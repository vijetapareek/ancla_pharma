from django.shortcuts import render
import pandas as pd
import sqlite3
pd.set_option('display.max_colwidth', 100)
from datetime import datetime

con = sqlite3.connect(r"D:\workspace\finaltask\anclatech\db.sqlite3")
# Load the data into a DataFrame
product_df = pd.read_sql_query("SELECT * from product", con)
event_df = pd.read_sql_query("SELECT * from event", con)
con.close()

product_list = ['None'] + list(product_df.product_name.unique())
event_list = ['None'] +  list(event_df.event_name.unique())

product_df.prod_start_date = pd.to_datetime(product_df.prod_start_date,  infer_datetime_format=True)
product_df.prod_end_date = pd.to_datetime(product_df.prod_end_date, infer_datetime_format=True)

event_df.event_start_date = pd.to_datetime(event_df.event_start_date,  infer_datetime_format=True)
event_df.event_end_date = pd.to_datetime(event_df.event_end_date, infer_datetime_format=True)

import getpass
username= getpass.getuser()

# Create your views here.

# demo inputs
#product_name_selected = 'Lipitor'
#event_name_selected = 'appendicitis'
#start_date = '2011-01-27'
#end_date = '2016-12-31'


def pharmapp_view(request):
    product_name_selected = request.GET.get("product_name", None)
    event_name_selected = request.GET.get("event_name", None)
    prod_start_date = request.GET.get("prod_start_date", '')
    print(prod_start_date)
    event_start_date = request.GET.get("event_start_date", '')
    print(event_start_date)
    if (prod_start_date != "") and (event_start_date != ""):
        prod_start_date1 = datetime.strptime(prod_start_date, '%Y-%m-%d')
        event_start_date1 = datetime.strptime(event_start_date, '%Y-%m-%d')
        product_df1 = product_df[(product_df.product_name == product_name_selected) & (product_df.prod_start_date >= prod_start_date1)]
                 
        product_df_html = product_df1.to_html(index=False, index_names=False, justify='center')

        product_df_html_str = product_df_html.replace('\n', '')

        event_df1 = event_df[(event_df.event_name == event_name_selected) & (event_df.event_start_date >= event_start_date1)]
        event_df1 = event_df1

        event_df_html = event_df1.to_html(index=False, index_names=False, justify='center')

        event_df_html_str = event_df_html.replace('\n', '')

        product_event_df = pd.concat([product_df1, event_df1], axis=1)
        product_event_df_html = product_event_df.to_html(index=False, index_names=False, justify='center')

        product_event_df_html_str = product_event_df_html.replace('\n', '')

    else:
        product_df_html_str = None
        event_df_html_str = None
        product_event_df_html_str = None


    context = {'product_list': product_list, 'event_list': event_list,
               'product_name_selected': product_name_selected,
               'event_name_selected': event_name_selected,
               'prod_start_date': prod_start_date,
               'event_start_date': event_start_date,
               'product_df_html_str': product_df_html_str,
               'event_df_html_str': event_df_html_str,
               'product_event_df_html_str': product_event_df_html_str,
               'username': username,
               }

    return render(request=request,
                  template_name='pharmapp/pharma_website.html',
                  context=context)