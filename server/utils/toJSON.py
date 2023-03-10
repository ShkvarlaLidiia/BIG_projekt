def toJSON (arr) :  
    json_arr = []
    for item in arr:
        json_arr.append(item.__dict__)
    return json_arr