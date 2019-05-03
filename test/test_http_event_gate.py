import requests
import json
from model.input_data import *
from parse import search
import time
# from model.check_event_gate_response import check_event_gate_response

# Перед началом теста необходимо подложить файл paths.txt в папку *SecurOS\Modules\http_event_proxy и добавить обработчик в скрипты из файла Additional_Function.js
def test_SendRequestGET():
    response = requests.get(url="http://" + slave_ip + ":88/event?param=123")
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    text = response.text
    # поиск param в теле text
    param = search('param<{}>', text)
    # выборка нужного элемента
    param = param.fixed[0]
    assert param == "123"



def test_SendRequestPOSTWithXML():
    data = "<root><node1>value1</node1><node2>value2</node2></root>"
    response = requests.post(url="http://" + slave_ip + ":88/event", data=data)
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    text = response.text
    body = search('body<{}>,', text)
    b = body.fixed[0]
    assert data == b


def test_SendUserRequestGETandResponse():
    response = requests.get(url="http://" + slave_ip + ":88/testreq?param=pam")
    time.sleep(1)
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    assert response.text == "Response"

def test_SendUserRequestGETandResponseWithXML():
    response = requests.get(url="http://" + slave_ip + ":88/test/xml?param=xml")
    time.sleep(2)
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    text = response.text
    param = search('<param>{}</param>', text)
    param = param.fixed[0]
    assert param == "value"


def test_SendUserRequestPOSTandResponseWithJSON():
    data = "<root><node1>value1</node1><node2>value2</node2></root>"
    response = requests.post(url="http://" + slave_ip + ":88/test/json", data=data)
    user_resp_code = "200"
    assert str(response.status_code) == user_resp_code
    # тело джисона
    body = json.dumps(response.json())
    # словарь из джисона
    data2 = json.loads(body)
    # соответсвие параметру в словаре
    data3 = data2["param"]
    # print("data3"+data3)
    assert data3 == "value"

