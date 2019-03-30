# Должен быть создан интерфейс iidk
# Должен быть пользователь с полными правами

from model.input_data import *


def test_create_environment(fix):
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<HTTP_EVENT_PROXY>,objid<"+objId+">,parent_id<"+slave+">,name<Test_HTTP_Event_Gate>,port<88>").encode("utf-8"))
