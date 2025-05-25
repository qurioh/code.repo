
    
bio = {
    "name": "qurioh",
    "age":22,
    "city": "voi",
    "hobies": ["dancing", "gaming", "drawing"],
    "likes_cycling": False
}

print(bio["name"])
bio["email"] = "user@gmail.com"
print(bio)

def show_first_key(data):
    if len(data) > 0:
        first_key = list(data.keys())[0]
        print("The first key is:", first_key)
    else:
        print("The dictionary is empty.")

show_first_key(bio)

