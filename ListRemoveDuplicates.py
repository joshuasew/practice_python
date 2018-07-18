# Joshua Sew-Hee
# 6/15/18
# List Remove Duplicates

def list_remove_dup_set(alist):
    alist = set(alist)
    alist = list(alist)
    return alist

def list_remove_dup_loop(alist):
    new_list = []

    for i in alist:
        if i not in new_list:
            new_list.append(i)
    return new_list


names = ["Michele", "Rob", "Robin", "Sara", "Rob", "Michele"]

print("Using sets: ", end='')
print(list_remove_dup_set(names))
print("Using loop: ", end='')
print(list_remove_dup_loop(names))
