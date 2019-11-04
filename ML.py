def find_key_by_value(dictionary, value):
    key = []
    dict_items = dictionary.items()
    for item in dict_items:
        if item[1] == value:
            key.append(item[0])
    return key

def calculate_binary_ML_test(likes):
    likeC1, likeC2 = likes[0], likes[1]
    if likeC2 > likeC1:
        return 2
    return 1

def calculate_multi_class_ML_test(likes):
    likeC1, likeC2, likeC3, likeC4 =  likes[0], likes[1], likes[2], likes[3]
    likes = {'1' : likeC1,
             '2' : likeC2,
             '3' : likeC3,
             '4' : likeC4}
    ml = max(likes.values())
    key = find_key_by_value(likes, ml)
    return int(key[0])