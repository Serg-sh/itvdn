user = {
    "name": "JohnDoe",
    "info": {
        "basic": {
            "age": 25,
            "salary": 5000
        },
        "additional": {
            "study": "mathematics",
            "family": "married"
        },
        "special": {
            "projects": [
                {"name": "quantum computer", "stage": "in_progress"},
                {"name": "laser_gun", "stage": "in_production"}
            ]
        }
    }
}


def get_data(data_dict, keys):
    data = data_dict
    for key in keys:
        data = data[key]
    return data


def get_data_rec(data_dict, keys, index=0):
    if index < len(keys):
        return get_data_rec(data_dict[keys[index]], keys, index + 1)
    return data_dict


print(get_data(user, ["info", "special", "projects", 0, "name"]))
print(get_data_rec(user, ["info", "special", "projects", 0, "name"]))

str_1 = "1_2,40_5,5_32"

fun = lambda s: int(s.split("_")[0]) + int(s.split("_")[1])

list_1 = [fun(res) for res in str_1.split(",")]

print(list_1)

ls = [[1, 2], [3, 4]]
list_2 = [x for y in ls for x in y]

print(list_2)
