import json
import os

def export_to_json_file(dict_in):
    jfile_name = "jdb.json"
    file_dict = {}
    with open(jfile_name, "w") as json_file:
            json.dump(dict_in, json_file)

