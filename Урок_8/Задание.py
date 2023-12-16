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
    return response.json()["access_token"]

def test_get_employee():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url + "/employee", headers=headers)
    assert response.status_code == 200

def test_post_employee():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    employee_data = {
  
    }
    response = requests.post(url + "/employee", json=employee_data, headers=headers)
    assert response.status_code == 201

def test_get_employee_by_id():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    employee_id = 1  
    response = requests.get(url + f"/employee/{employee_id}", headers=headers)
    assert response.status_code == 200

def test_patch_employee():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    employee_id = 1  
    updated_data = {
 
    }
    response = requests.patch(url + f"/employee/{employee_id}", json=updated_data, headers=headers)
    assert response.status_code == 200