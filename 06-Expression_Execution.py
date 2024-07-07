#Expression Execution

#string and numeric values can operate together with (* or Intu),Like
#its called Repeatation

a = 2
b = 3
txt = "@"
Multiplication = a*txt*3 
#Multi string(Two strings) can't oprate by * or INTU in that case,We have to use + or PLUS its the concatenation rule
#in first, 2*@ = 2@
# (2@)*3
# 2@2@2@
print(Multiplication)

#String & String can operate together with a "+ or PLUS"
#It is called Concatenation
A , B = "2" , 3
txt = "@"
Multiplication2=((A + txt)*B)
#There is a perenthesis thats why by precedence rule,the brecket will be worked 1st.
#(2@)*3
# 2@2@2@
Multiplication3=(A + txt * B)

#there are no perenthesis.By precedence not,and,or
#2 + @ * 3
#2 + @@@ 
#2@@@
print(Multiplication2)
print(Multiplication3)

#Numeric values can operate with all arithmetic(+,-,*,/) operators

C,D = 2,3
E = 4
Equal=(C+D*E)#Precedence Rule
print (Equal)

#Arithmetic expression with integer and float result is FLOAT
Q , W = 10 , 5.0
R=Q*W
print(R)#10*5.0=50.0

#Result of devision operator with two integers will be float
S,D = 1,2
F = S/D #1/2
print(F)

# Integer devision with float and integer will give int result but displayed as FLOAT
# integer devision (//)
#it will only show the integer value (0.5 will be shown as 0,1.99 will be shown 1)
#BUT it will be displayed in float which means 0.5 will show 0.0

G,H = 1.5 , 3
J = G//H #1.5//3 = 0.5 = 0.0
I = G/H #1.5/3 = 0.5
print(J , G / H)
 
#result of (A//B) is same as FLOOR (A/B)
#FLOOR gives the closest integer ,which is lesser than or equal to the float value
#0.1=0, 5.2=5, 7.99=7, 2=2
#butttttttttttttt, -5.2= -6

K,L = 12,5
j=K//L #12/5=2.4=2
print(j)

k,l = -12 , 5
h = k//l #-12//5= -2.4 = -3 
print(h)

s,d = 12 , -5
f=s//d  #12//-5 = -2.4 = -3

#REMAINDER IS NEGATIVE WHEN denominator (HOR) negative
#rest all case remainder will be +ve
