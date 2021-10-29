import json
import click
from click.decorators import help_option
from flask.json import jsonify
import requests


def all_record() -> json:  
    url = 'http://mk007.pythonanywhere.com/gymondoapi/v1/data/all'

    response = requests.get(url)

    return response.json()
def record_by_id(record_type) -> json:
    url = 'http://mk007.pythonanywhere.com/gymondoapi/v1/data/id/'+str(record_type)

    query_params = {
        'q': record_type,
    }

    response = requests.get(url)

    return response.json()
def add_record(record_type) -> json:
    ds = record_type.split(", ")
    print(ds)
    url = 'http://mk007.pythonanywhere.com/gymondoapi/v1/data/add?event='+ds[0]+'&ID='+ds[2]+'&year='+ds[3]+'&category='+ds[1]
    response = requests.post(url)

    return response

def remove_by_id(record_type) -> json:
    url = 'http://mk007.pythonanywhere.com/gymondoapi/v1/data/remove/id/'+str(record_type)

    response = requests.delete(url)

    return response.json()


@click.command()
@click.option(
    '--get_data', '-gd',default='',
    help='get all data or by id',
)

@click.option(
    '--add_data', '-ad',default='',
    help='add new data to the database',
)

@click.option(
    '--remove_data', '-rd',default='',
    help='remove data by id from the database',
)

def main(remove_data,get_data,add_data) -> None:
    """
    A little data interaction tool through api that helps you to play with the current data in the database. Provide the required command to get data, remove data or add data.
    Here are few examples command:
    
    1. gymondo --get_data all

    2. gymondo --get_data id 3

    4. gymondo --remove_data id 3

    5. gymondo --add data "Covid19, Pandemic, 14, 2019"

    You need a valid API endpoints from gymondoapi for the tool to work.
    """
    if get_data=='':
        all_data_json = all_record()
    elif get_data=='all':
        all_data_json = all_record()
    else:
        all_data_json = record_by_id(get_data)

    if remove_data=='':
        pass
    else:
        all_data_json = remove_by_id(remove_data)

    if add_data == '':
        pass
    else:
        all_data_json=add_record(add_data)
        
    print(f"The data right now: {all_data_json}.")


if __name__ == "__main__":
    main()