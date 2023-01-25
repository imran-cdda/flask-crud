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

class Formatter:
    def __init__(self, data, schema):
        self.data = format_dict(data.to_mongo())
        self.schema = schema

    def format(self):
        result = {}
        for k in self.schema:
            result[k] = self.data.get(self.schema[k])
        return result
