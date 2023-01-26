from bson import ObjectId

def flatten_dict(input_data, prefix = "", schema=False):
    output_data = {}
    for key, value in input_data.items():
        new_key = prefix + "." + key if prefix else key
        if isinstance(value, dict):
            output_data.update(flatten_dict(value, new_key))
            if not schema:
                output_data[new_key] = value
        else:
            output_data[new_key] = value
    return output_data

def format_result(data):
    output_data = {}
    for key, value in data.items():
        keys = key.split(".")
        d = output_data
        for k in keys[:-1]:
            if k not in d:
                d[k] = {}
            d = d[k]
        d[keys[-1]] = value
    return output_data

import json
class DataFormatter:
    def __init__(self, *args, **kwargs):
        self.schema = {k:v for k,v in self.__class__.__dict__.items() if not k.startswith("__")}

    def format(self, data, many=False, ref=[]):
        schema = flatten_dict(self.schema, schema=True)
        if many:
            result = []
            for d in list(data):
                ref_data = {}
                for rf in ref:
                    ref_data[rf] = json.loads(getattr(d, rf).to_json())
                try:
                    d = d.to_mongo() | ref_data
                except:
                    d = d | ref_data
                d = flatten_dict(d)
                new_data = {}
                for k in schema:
                    new_data[k] = str(d.get(schema[k])) if isinstance(d.get(schema[k]), ObjectId) else d.get(schema[k])
                result.append(format_result(new_data))
            return result
        else:
            ref_data = {}
            for rf in ref:
                ref_data[rf] = json.loads(getattr(data, rf).to_json())
            try:
                data = data.to_mongo() | ref_data
            except:
                data = data | ref_data
            data = flatten_dict(data)
            new_data = {}
            for k in schema:
                new_data[k] = str(data.get(schema[k])) if isinstance(data.get(schema[k]), ObjectId) else data.get(schema[k])
            return format_result(new_data)
