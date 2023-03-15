a=10
if a==10:
    print("True")
if a>15:
    print("a is greaterthan")
if a<=15:
    print("a is lessthan")
if a is a:
    print("True")   
if a:
    print(a)
for i in range(a):
    if i:
        print(i)
        if i==3:
             break
result:
    True
    a is lessthan
    True
    10
    1
    2
    3 
-------------------------------------------------------------------------------
var=int(input("input:"))
if var-2==var:
    print("even number")
elif var%2==0:
    print(var,"is even number")
else:
    print("odd number")
result:
      input:13
      odd number
 ----------------------------------------------------
kus=[10,20,45,67,82]
print(kus)
kus.append(100)
print(kus,"append")
print("list append successfully")
kus.remove(20)
print(kus,"remove")
print("list remove successfully")
if kus[3]==100:
    print(kus)
if 82 not in kus:
    print("False")
elif 82 in kus:
    print("True")
result:
        [ 10, 20, 45, 67, 82]
        [10, 20, 45, 67, 82, 100] append
        list append successfully
        [10, 45, 67, 82, 100] remove
        list remove successfully
        True


