import requests
import json
from model.input_data import *
from parse import search

# Перед началом теста необходимо подложить файл paths.txt в папку *SecurOS\Modules\http_event_proxy и добавить обработчик в скрипты из файла Additional_Function.js
def test_SendRequestGET():
    response = requests.get(url="http://" + slave_ip + ":88/event?param=123")
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    text = response.text
    method = response.request.method
    param = search('param<{}>', text)
    param = param.fixed[0]
    assert param == "123"
    assert method == "GET"


def test_SendRequestPOSTWithXML():
    data = "<root><node1>value1</node1><node2>value2</node2></root>"
    response = requests.post(url="http://" + slave_ip + ":88/event", data=data)
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    body = response.request.body
    method = response.request.method
    assert method == "POST"
    assert data == body


def test_SendUserRequestGETandResponse(fix):
    response = requests.get(url="http://" + slave_ip + ":88/testreq?param=pam")
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    method = response.request.method
    param = response.request.path_url
    assert param == "/testreq?param=pam"
    assert method == "GET"


def test_SendUserRequestGETandResponseWithXML():
    response = requests.get(url="http://" + slave_ip + ":88/test/xml?param=xml")
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    text = response.text
    method = response.request.method
    param = search('</param><{}>', text)
    param = param.fixed[0]
    assert param == "xml"
    assert method == "GET"


def test_SendUserRequestPOSTandResponseWithJSON():
    data = "<root><node1>value1</node1><node2>value2</node2></root>"
    response = requests.post(url="http://" + slave_ip + ":88/test/json", data=data)
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    body = json.dumps(response.json())
    data2 = json.loads(body)
    data3 = data2["param"]
    path = response.request.path_url
    assert data3 == "value"
    assert path == "/test/json"
