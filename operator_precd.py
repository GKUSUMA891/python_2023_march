
8-5+8/3==65/10-2+5%2  
8-5+2==5/10-2+5%2    first / priority  
8-5+2==6-2+5%2     first2nd step: / priority 
8-5+2==6-2+1    third step:  % priority 
3+2==4+1        fourth step: - priority 
5==5       fifth step:  + priority 
result= 1
-------------------------------------------------------------------------------
(2//3+4*2%3-1**9**8)   
here ** have the same precedency so wee need to go t54o associtivity so Right to left 
1st   1**9**8=>1
next follor division(//) Left to Right so 
2nd   2//3=>0
 0+4*2%3-1*1  
 =>0+8%3-1*1 =>next 8%3  =>2  
next 0+2-1*1 
=>1*1=>1  0+2-1 =>1
next 0+1*1=>  1*1=>1  
o/p=1
---------------------------------------------------
l = 15
m = 109
n = 152
result = l+ m * n / m - l ** 2
print(result)
procedure:15+109*152/109-15**2
           15+109*152/109-225
           15+16568/109-225
           15+152.0-225
   result:-58.0
#-------------------------------------------------------
print(56+22//8-2*5)
procedure:56+2-2*5
            56+2-10
             58-10
  result:48
