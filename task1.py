list_key = ['one', 'two', 'three', 'four']
list_val = [1, 2, 3, 4, 5]
dictlist = dict(zip(
    list_key, list_val + [None] * (len(list_key) - len(list_val))))
print (dictlist)
