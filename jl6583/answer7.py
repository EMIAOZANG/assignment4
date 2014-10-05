#starting list
init_list = range(1,10)
#modifying the list with only slicing and list operations(in-place)
del init_list[4:9] #if del operation is not allowed, use list.pop() within a for loop will do the same thing
for values in range(1,4):
    init_list.extend(init_list[:4])
init_list.sort()
init_list.remove(2)
init_list.insert(7,3)
print init_list

#or this can be done with subscriptions
init_list = range(1,10)
#modification
init_list = init_list[:4]*4
init_list.sort()
init_list[7] = 3
print init_list
