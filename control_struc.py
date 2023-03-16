a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a>b and a>c:
      print("a is largest")
if b>a and b>c:
      print("b is largest")
if c>a and c>b:
      print("c is largest")
if a==b:
    print('a and b are same')
elif a!=b:
    print("a and b are not same")
result:
        enter a value:12
        enter b value:3
        enter c value:44
        c is largest
        a and b are not same
            -----------------------------------------------------------------------
for i in ["string","c++","kus","idiot"]:
    print(i)
    if i==len(i):
        print([i])
result:
      string
      c++
      kus
      idiot
      ---------------------------------------------------------------
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
result:
      1
      2
      3
      4
      5
      i is no longer less than 6
  ---------------------------------------------------
  ii=0
while ii<6:
    ii+=1
    #print(i)
    if ii==5:
        continue
    print(ii)
result:
      1
      2
      3
      4
      6
      -----------------------------------------------------------------------
        print([i])
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
      result:
            1
            2
            3
      --------------------------------------------------------------
i=0
while i<6:
    i+=1
    #print(i)
    if i==5:
        continue
    print(i)
result:
      1
      2
      3
      4
      6


