from fixture.load_dll import DllHelper
from model.input_data import *
import pytest
import time
import os


@pytest.fixture
def fix(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture

@pytest.fixture(scope="session", autouse=True)
def fix2(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<"+objId+">,parent_id<"+slave+">,name<Test_HTTP_Event_Gate>,port<88>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<VBJSCRIPT_GROUP>,objid<"+objId+">,parent_id<"+slave+">,name<Program VB/JScript"+objId+">").encode("utf-8"))
    f = open("C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\http_event_proxy\\paths.txt", "w")
    f.write(file_paths_data)
    f.close()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<VBJSCRIPT>,objid<"+objId+">,parent_id<"+objId+">,name<Program VB/JScript"+objId+">,code<"+script_data+">").encode("utf-8"))
    time.sleep(1)
    print('\nSome recource')
    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<" + objId + ">").encode("utf-8"))
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<VBJSCRIPT_GROUP>,objid<" + objId + ">").encode("utf-8"))
        os.remove("C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\http_event_proxy\\paths.txt")
        print('\nSome resource fin')
    request.addfinalizer(fin)
    return request