import os
from flask import Flask, request, jsonify
import requests
from flask import json


def test_data_manipulate_get_all(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'data','all')
    print(endpoint)
    response = requests.get(endpoint)
    assert response.status_code == 200
    json_data = response.json()
    assert  {
   "event": "Outbreak",
   "event_category": "Dengue",
   "id": 8,
   "year": "2029"
  }  in json_data



def test_data_manipulate_remove_id(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'data','remove','id','8')
    
    print(endpoint)
    response = requests.delete(endpoint)
    assert response.status_code == 200
    json_data = response.json()
    assert  {
   "event": "Outbreak",
   "event_category": "Dengue",
   "id": 8,
   "year": "2029"
  }  not in json_data
