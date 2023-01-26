import pprint

# def flatten_dict(input_data, prefix = ""):
#     output_data = {}
#     for key, value in input_data.items():
#         new_key = prefix + "." + key if prefix else key
#         if isinstance(value, dict):
#             output_data.update(flatten_dict(value, new_key))
#         else:
#             output_data[new_key] = value
#     return output_data
#
# input_data = {
#     "address": {
#         "lat": "54654654",
#         "full": {
#             "city": "gazipur",
#             "state": "dhaka",
#             "more": {
#                 "name": "dfjsdhf",
#                 "age": 1
#             }
#         },
#         "short": {
#             "ci": "dsgfdfs"
#         }
#     },
#     "name": "yeasir"
# }
#
# output_data = {**input_data, **flatten_dict(input_data)}

def flatten_dict(input_data, prefix = ""):
    output_data = {}
    for key, value in input_data.items():
        new_key = prefix + "." + key if prefix else key
        if isinstance(value, dict):
            output_data.update(flatten_dict(value, new_key))
        else:
            output_data[new_key] = value
    return output_data

input_data = {
    "address": {
        "lat": "54654654",
        "full": {
            "city": "gazipur",
            "state": "dhaka"
        }
    },
    "name": "yeasir"
}

output_data = {**input_data, **flatten_dict(input_data)}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(output_data)
