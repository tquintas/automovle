import json

with open("automovle/all-vehicles-model.json", "r") as f:
    data = json.load(f)

with open("automovle/makes.json", "r") as f:
    makes = json.load(f)

new_data = {}
rare_data = {}
for d in data:
    trim = {}
    make = d["make"]
    make_info_list = list(filter(lambda dd: dd["make_id"] == make.lower().replace(" ","-").replace(".","").replace(",",""), makes["Makes"]))
    make_info = make_info_list[0]
    trim.update(make_info)
    trim["make_display"] = make
    trim['make_is_common'] = trim['make_is_common'] == "1"
    trim["model"] = d["model"]
    trim["year"] = int(d["year"])
    if "Gasoline" in d["fueltype1"]:
        if "Electricity" in d["fueltype"]:
            fuel = "Hybrid"
        else:
            fuel = "Gasoline"
    else:
        fuel = d["fueltype1"]
    trim["fuel"] = fuel
    trim["drive"] = d["drive"]
    trim["class"] = d["vclass"]
    trim["base_model"] = d["basemodel"]
    trim["full_name"] = make + " " + d["model"]
    id = int(d['id'])
    if make_info["make_is_common"] and make_info["make_country"] != "USA":
        new_data[id] = trim
    else:
        rare_data[id] = trim

with open("automovle/carinfos.json", "w") as f:
    json.dump(new_data, f)
with open("automovle/rarecarinfos.json", "w") as f:
    json.dump(rare_data, f)
with open("automovle/carids.txt", "w") as f:
    f.write(str(sorted(new_data.keys())))
with open("automovle/rarecarids.txt", "w") as f:
    f.write(str(sorted(rare_data.keys())))