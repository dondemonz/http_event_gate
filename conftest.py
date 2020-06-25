from fixture.load_dll import DllHelper
from model.input_data import *
from fixture.search import SearchHelper
import pytest
import time
# import os


@pytest.fixture(scope="session")
def search():
    fixture = SearchHelper()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def fix(request):
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<"+objId+">,parent_id<"+slave+">,name<Test_HTTP_Event_Gate>,port<"+http_evgate_port+">").encode("utf-8"))
    time.sleep(1)
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<VBJSCRIPT_GROUP>,objid<"+objId+">,parent_id<"+slave+">,name<Program VB/JScript"+objId+">").encode("utf-8"))
    time.sleep(1)
    # у дженкинса проблемы с доступом к файлу, через пайчарм тест проходит.
    # f = open("C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\http_event_proxy\\paths.txt", "w+")
    # f.write(file_paths_data)
    # f.close()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<VBJSCRIPT>,objid<"+objId+">,parent_id<"+objId+">,name<Program VB/JScript"+objId+">,code<"+script_data+">").encode("utf-8"))
    time.sleep(1)
    print('\nStart fixture')

    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<" + objId + ">").encode("utf-8"))
        time.sleep(1)
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<VBJSCRIPT_GROUP>,objid<" + objId + ">").encode("utf-8"))
        # дженкинс не может создать файл, не хватает прав, пока не решил эту проблему, поэтому удалять файл нельзя
        # os.remove("C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\http_event_proxy\\paths.txt")
        print('\nEnd fixture')
        fix.disconnect()

    request.addfinalizer(fin)
    return fix
