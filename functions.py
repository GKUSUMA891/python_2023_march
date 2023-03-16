kus=25
def fun_name(name):
    print("iam from" + name)
    if kus==2250:
        print("s")
    else:
        print("F")
fun_name("bangalore")
result:
  iam frombangalore
  F
 --------------------------------------------------------------
def fun_name(name,age,id=30):
    print("name:",name,"age:",age,"id:",id)
fun_name("kushi",40)
fun_name("prema",45,45456)
fun_name("dskj",45)
result:
  name: kushi age: 40 id: 30
  name: prema age: 45 id: 45456
  name: dskj age: 45 id: 30
--------------------------------  
def fun_name(name,age=95,id=4):
    print("name:",name,"age:",age,"id:",id)
fun_name(40)
result:
   name: 40 age: 95 id: 4
 ----------------------------------------------------
def fun_name(name,age=95,id):
    print("name:",name,"age:",age,"id:",id)
fun_name(40)#error 
-----------------------------------
def required_arg(fruit,veg):
    print(fruit + " is my favv" + " i hate" + veg)
required_arg("mango","palak")
required_arg("papaya","cabbage")
#required_arg("orange","menthi","sdkjfh") return type error
result:
     mango is my favv i hatepalak
     papaya is my favv i hatecabbage

-----------------------------------------------------------------

 def keyword_org(Bi,Qa,dev=345):
    print(Bi + " From B&i" + Qa + " from QA." )
keyword_org(Bi="bannysha",Qa="kusuma")
keyword_org(Qa="bannysha",Bi="kusuma",dev=345)
keyword_org(Qa="yogi",Bi="jogi",dev=3)
#keyword_org("df","qwe",dev)#name eroor
result:
  bannysha From B&ikusuma from QA.
  kusuma From B&ibannysha from QA.
  jogi From B&iyogi from QA.
  ------------------------------------------------
 def variable_arg(*m):
    print(m)
variable_arg(10)
variable_arg(10,20)
variable_arg(34,556,7,8,"djfh")
variable_arg(30,40,506,6,"jhwru","ewiurhy",5.6)
variable_arg([10,20,30],40,50,60,{"key":"val"})
variable_arg()
result:
  (10,)
  (10, 20)
  (34, 556, 7, 8, 'djfh')
  (30, 40, 506, 6, 'jhwru', 'ewiurhy', 5.6)
  ([10, 20, 30], 40, 50, 60, {'key': 'val'})
  ()

