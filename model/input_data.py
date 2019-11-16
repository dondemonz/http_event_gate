iidkId = "1"
iidkPort = "1030"  # "1030"
http_evgate_port = "88"
localHostIp = "172.16.11.102"  # используется для iidk
slave = "VQA-2"
slave_ip = "172.16.11.102"  # используется в тестах
user = "1"
password = "1"
auth = (user, password)  # пользователь/пароль
objId = "999"
file_paths_data = "/testreq" '\n' "/test/*"
script_data = 'function Init()\n'\
              '{Core.RegisterEventHandler("HTTP_EVENT_PROXY","999","PENDING_REQUEST", Response)} \n'\
              'function Response(e)\n'\
              '{Log.Trace(e._path) \n'\
              'switch(e._path) \n'\
              '{case "/test/xml": Core.DoReact("HTTP_EVENT_PROXY","999","RESPONSE","_id",e._id,"_body","<xml><param>value</param><xml>");break;\n'\
              'case "/test/json": Core.DoReact("HTTP_EVENT_PROXY","999","RESPONSE","_id",e._id,"_body","{\\"param\\": \\"value\\",\\"array\\": {\\"param1\\": \\"value\\"}}","_content_type","application/json"); break;\n'\
              'default: Core.DoReact("HTTP_EVENT_PROXY","999","RESPONSE","_id",e._id,"_body","Response","_content_type","text/plain");break;}}'





