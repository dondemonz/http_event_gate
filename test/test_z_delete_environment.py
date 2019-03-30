from model.input_data import *

def test_delete_environment(fix):
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<"+objId+">").encode("utf-8"))

