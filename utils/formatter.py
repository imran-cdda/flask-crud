from bson import ObjectId

def format_dict(input_dict, parent=None, res = {}):
    for k, v in input_dict.items():
        if isinstance(v, dict):
            if parent:
                format_dict(v, f"{parent}.{k}", res)
            else:
                format_dict(v, f"{k}", res)
        else:
            if parent:
                res[f"{parent}.{k}"] = v
            else:
                res[k] = v
    return res

import json
class DataFormatter:
    def __init__(self):
        data = {}
        for key in self.__dir__():
            if isinstance(self.__getattribute__(key), str) and "__" not in key:
                data[key] = self.__getattribute__(key)
        self.schema = data

    def format(self, data):
        data = format_dict(data.to_mongo())
        result = {}
        for k in self.schema:
            result[k] = str(data.get(self.schema[k])) if isinstance(data.get(self.schema[k]), ObjectId) else data.get(self.schema[k])
        return result
