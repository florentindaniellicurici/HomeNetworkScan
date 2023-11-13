import json
import os

def export_to_json_file(dict_in):
    jfile_name = "jdb.json"
    file_dict = {}

    if os.path.exists(jfile_name) and os.path.getsize(jfile_name) > 0:
        with open(jfile_name, "r") as json_file:
            jdict = json.load(json_file)
        print("this is {}".format(jdict))

        new_dict = jdict.copy()
        for j, k in dict_in.items():

            if j in jdict:

                new_dict[j] = new_dict[j] + 1
            else:
                new_dict[j] = 1

        print("new: {}".format(new_dict))

        with open(jfile_name, "w") as json_file:
            json.dump(new_dict, json_file)


    else:
        with open(jfile_name, "w") as json_file:
            json.dump(dict_in, json_file)

