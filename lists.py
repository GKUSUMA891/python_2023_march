#sum of elements
'''list1=[10,30,40,50]
sum=0
n=len(list1)
for i in range(0,n):
    sum=sum+list1[i]
print(sum)'''
      #-------------------
'''sum=0
i=0
list1=[10,20,304,50,69]
n=len(list1)
while(i<n):
    sum=sum+list1[i]
    i+=1
print(sum)'''

'''ma=[100,200,300,400,500]
m=sum(ma)
print("sum of list:",m)'''
#--------------------
#sum of elements inside a range
'''sum=0
for i in range(0,20):
    sum+=i
    print(sum)'''

#copy,append
'''a=[10,20,30,40,50,60,70]
print("a is:",a)
b=a.copy()
print("b is:",b)
b.append(1000)
print(b)'''
#for and if
'''num=[10,20,30,40,[12,13,14,15],80]
for i in num:
    if [12,13,14,15] in num:
        print(num)
        if i==num[1]:
            break
print(i)'''
#extend,remove,count
'''man=[100,200,300,400,500]
man.extend([300,203,104,105,[1,2,3,4,5],300])
print(man)
man.append(555)
print(man)
man.remove(100)
print(man)
man[2]=180
print(man)
n=man.count(300)
print("count:",n)'''
#--------------------
#sorting
'''man=[10,2,32,43,50,26,57,88,79]
man.sort()
print("sorting:",man)

man.sort(reverse=True)
print("descending:",man)

man.sort(reverse=False)
print("ascending:",man)'''
#---------------------------------
'''list1=[10,20,30,40,'johny']
for i in range(0,len(list1)):
    m=list1.index(list1[i])
print(m)'''
#----------------------
 #all(),any(),enumarate(),len()
a=['True',1,2,3,4]
b=[1,0,50,77]
print(all(a))
print(any(a))
print(all(b))
print(any(b))
print("length of a:",len(a))
for i in enumerate([1,2,3,4,'mango',6,50]):
    print(i)






























