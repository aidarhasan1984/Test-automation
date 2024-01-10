import requests
import pytest

url = "https://x-clients-be.onrender.com"

def get_auth_token():
    auth_url = url + "/auth/login"
    auth_data = {
        "username": "raphael",
        "password": "cool-but-crude"
    }
    response = requests.post(auth_url, json=auth_data)
    return response.json()["userToken"]

def test_get_employee():
    token = get_auth_token()
    headers = {"x-client-token": token}
    response = requests.get(url + "/employee", headers=headers)
    assert response.status_code == 200

def test_post_employee():
    token = get_auth_token()
    headers = {"x-client-token": token}
    employee_data = {
        
    }
    response = requests.post(url + "/employee", json=employee_data, headers=headers)
    assert response.status_code == 201

def test_get_employee_by_id():
    token = get_auth_token()
    headers = {"x-client-token": token}
    employee_id = 1  
    response = requests.get(url + f"/employee/{employee_id}", headers=headers)
    assert response.status_code == 200

def test_patch_employee():
    token = get_auth_token()
    headers = {"x-client-token": token}
    employee_id = 1  
    updated_data = {
        
    }
    response = requests.patch(url + f"/employee/{employee_id}", json=updated_data, headers=headers)
    assert response.status_code == 200

def test_get_employee_negative():
    token = get_auth_token()
    headers = {"x-client-token": token}
    employee_id = 9999  
    response = requests.get(url + f"/employee/{employee_id}", headers=headers)
    assert response.status_code == 404

def test_patch_employee_negative():
    token = get_auth_token()
    headers = {"x-client-token": token}
    employee_id = 9999  
    updated_data = {
      
    }
    response = requests.patch(url + f"/employee/{employee_id}", json=updated_data, headers=headers)
    assert response.status_code == 404