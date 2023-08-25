dict_1 = {
    "a":1,"b":2, "name": "Bob"
}

dict_2 = {
    "b":3,"c":4, "name": "Alice"
}


print("First dictionary =", dict_1)
print("Second dictionary =", dict_2)
print("Using merge operator")
merge_dict = dict_1 | dict_2 
print(merge_dict)
