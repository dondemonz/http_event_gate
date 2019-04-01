from model.input_data import *
import os

def test_delete_environment(fix):
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<"+objId+">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<VBJSCRIPT_GROUP>,objid<"+objId+">").encode("utf-8"))
    os.remove("C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\http_event_proxy\\paths.txt")

