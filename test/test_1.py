# Должен быть создан интерфейс iidk
# Должен быть пользователь с полными правами

from model.input_data import *
import time


def test_create_environment(fix):
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<"+objId+">,parent_id<"+slave+">,name<Test_HTTP_Event_Gate>,port<88>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<VBJSCRIPT_GROUP>,objid<"+objId+">,parent_id<"+slave+">,name<Program VB/JScript"+objId+">").encode("utf-8"))


def test_create_file_paths():
    f = open("C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\http_event_proxy\\paths.txt", "w")
    f.write(file_paths_data)
    f.close()


def test_create_program_script(fix):
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<VBJSCRIPT>,objid<"+objId+">,parent_id<"+objId+">,name<Program VB/JScript"+objId+">,code<"+script_data+">").encode("utf-8"))
    time.sleep(1)
