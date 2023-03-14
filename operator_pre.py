print(6*3+4**2//5-8)
precedence:6*3+16//5-8
          18+3-8
          21-8
      result:13
 ------------------------------------------------------
a=17
b=5
c=6
d=3
e=5
a%6-b/2+(c*d-5)/e

1st (c*d-5)=> * will execute first   6*3=18
2nd (c*d=5)=> - will execite  second 18-5=>13
3rd  a%6  =>17%6=>5
4th  b/2   =>5/2 =>2
5th  (c*d-5)/e=> 13/5=>2
6th  a%6-b/2=>  here  substaction (-) will execute  5-2=>3
7th   a%6-b/2 + (c*d-5)/e => + will execute means  3+2 => 5
 
