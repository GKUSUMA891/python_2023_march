sub=[10,23,34,56,678]
'''sub.reverse()
print(sub)
    new_list=sub.copy()
    new_list.reverse()
    print(new_list)
for i in reversed(sub):
    print(i)
print(sub[::-1])'''
new_list=[]
for i in reversed(sub):
    new_list.append(i)
    #new_list.reverse()
print(new_list)
