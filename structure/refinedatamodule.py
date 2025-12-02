import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data 

data = load_data("store_data.json")

#function to clean the data
def clean_data(data):
    text_to_num = {"one" : 1, "two" : 2, "three" : 3, "four": 4, "five": 5}
    
    unique_users = set()
    cleaned_data = []
    
    for user in data:
        #clean rating - consistent typing
        raw_rating = str(user['rating']).strip().lower()
        if(raw_rating in text_to_num):
            raw_rating = text_to_num[raw_rating]
        user['rating'] = raw_rating

        #handle missing values
        raw_age = user.get("age")
        if(raw_age == None):
            user["age"] = None

        #handle duplicate values - deduplication
        if(user['name'].strip() in unique_users):
            continue
        unique_users.add(user['name'])
        cleaned_data.append(user)
        
    return cleaned_data

data = clean_data(data)
print(data, len(data))
        