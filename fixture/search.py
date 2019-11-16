import json
from parse import search


class SearchHelper:

    def __init__(self):
        self.self = self

    def search_for_element(self, response, resp_param):
        text = response.text
        # поиск param в теле text
        param = search(resp_param, text)
        # выборка нужного элемента
        element = param.fixed[0]
        return element

    def search_in_json(self, response, param):
        # тело джисона
        body = json.dumps(response.json())
        # словарь из джисона
        data2 = json.loads(body)
        # соответсвие параметру в словаре
        element = data2[param]
        # print("element"+element)
        return element

    def destroy(self):
        self.destroy()
