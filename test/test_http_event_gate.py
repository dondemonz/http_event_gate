import requests
import pytest
from model.input_data import *
import time
from fixture.search import SearchHelper
# from model.check_event_gate_response import check_event_gate_response

# Тест использует файл paths.txt в папке *SecurOS\Modules\http_event_proxy


def test_send_request_get(search):
    response = requests.get(url="http://" + slave_ip + ":" + http_evgate_port + "/event?param=123")
    assert str(response.status_code) == "200"
    element = search.search_for_element(response, resp_param='param<{}>')
    assert element == "123"


def test_send_request_post_with_xml(search):  # здесь проверяется полное значение data
    data = "<root><node1>value1</node1><node2>value2</node2></root>"
    response = requests.post(url="http://" + slave_ip + ":" + http_evgate_port + "/event", data=data)
    assert str(response.status_code) == "200"
    element = search.search_for_element(response, resp_param='body<{}>,')
    assert data == element


def test_send_user_request_get_and_response():  # в тесте проводиться проверка на корректный запрос и не корректный параметр, респонс приходит, но там пусто (так и задумано).
    response = requests.get(url="http://" + slave_ip + ":" + http_evgate_port + "/testreq?param=pam")
    time.sleep(3)
    assert str(response.status_code) == "200"
    assert response.text == "Response"


def test_send_user_request_get_and_response_with_xml(search):
    response = requests.get(url="http://" + slave_ip + ":" + http_evgate_port + "/test/xml?param=xml")
    time.sleep(2)
    assert str(response.status_code) == "200"
    element = search.search_for_element(response, resp_param='<param>{}</param>')
    assert element == "value"


def test_send_user_request_post_and_response_with_json(search):  # а здесь вместо полного значения (как в 1 тесте) проверяется конкретное значение
    data = "<root><node1>value1</node1><node2>value2</node2></root>"
    response = requests.post(url="http://" + slave_ip + ":" + http_evgate_port + "/test/json", data=data)
    assert str(response.status_code) == "200"
    element = search.search_in_json(response, "param")
    assert element == "value"




