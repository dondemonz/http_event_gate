from parse import search


def check_event_gate_response(fix):
    n = fix.cb1.decode("utf-8")
    print("n!!!"+n)
    objaction = search('objaction<{}>', n)
    print("obj"+objaction)
    #objaction = a.fixed[0]
    #objid = search('objid<{}>', n)
    #objid = id.fixed[0]
    #objtype = search('objtype<{}>', n)
    #objtype = t.fixed[0]
    return objaction
           #objid, objtype
