# a = 5
# b = 4
# a = b

# c='Fatima'
# d='Aliyeva'
# c=d

# x=4.5
# y="Backend Fatima"
# y=x

# print(a)
# print(b)
# print(c)
# print(d)
# print(y)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(x))
# print(type(y))





# ad = input('Adinizi qeyd edin:')
# soyad = input('Soyadinizi qeyd edin:')
# yas = input("Yasinizi qeyd edin:") 

'''
print-den istifade etmediyimiz zaman bu netice qeyd edilir

Soyadinizi qeyd edin:ALIYEVA
Yasinizi qeyd edin:19
Adiniz Fatima 
Soyadiniz: ALIYEVA
Yasiniz 19

'''
'''
print-den istifade etdiyimiz zaman bu netice qeyd edilir.
Adinizi qeyd edin:Fatima
Soyadinizi qeyd edin:Aliyeva
Yasinizi qeyd edin:19
Adiniz Fatima 
Soyadiniz: Aliyeva
Yasiniz 19
'''

# print(f'Adiniz {ad} ')
# print(f"Soyadiniz: {soyad}")
# print(f"Yasiniz {yas}")

# a = input("Qiymeti daxil edin:")
# b = input ("Qiymeti daxil edin:")
# print(type(a))
# print(type(b))
# print(f'a*b = {a*b}')

'''
Qiymeti daxil edin:29
Qiymeti daxil edin:2001
<class 'str'>
<class 'str'>
Traceback (most recent call last):
print(f'a*b = {a*b}')
TypeError: can't multiply sequence by non-int of type 'str'
---------------------------------------------
Error yaranir sebeb ise input deyeri string formatinda.
Bildiyimiz kimi stringleri bir birine vurmaq olmaz!

'''


# a = int(input("Qiymeti daxil edin:"))
# b = int(input ("Qiymeti daxil edin:"))
# print(type(a))
# print(type(b))
# print(f'a*b = {a*b}')

'''
Casting metodan istifade etmek lazimdir. 
casting(float,boolean, int)
Erroru aradan qaldrimaq ucun deyerleri int,floata cevirmet lazimdir! 
Verilene qiymetleri vurdugumuz zaman error yaranmayacaq.
Sebeb ise deyerlerimiz artiq string formatinda yox int formatinda qeyd etdik.
--------
Qiymeti daxil edin:29
Qiymeti daxil edin:2001
<class 'int'>
<class 'int'>
a*b = 58029
'''

# a = float(input("Deyeri qeyd edin:"))
# b = int(input("2-ci Deyeri qeyd edin:"))
# print(f'Netice:{a**4}')

'''
Biz burda float tipinden istifade etdik.
eger deyerimiz kesrli ededdirse onu float ile qeyd etmek lazimdir.
Eks halda int-den istifade etsek error olacaq sebeb tam eded deyil
'''

'''
x-=3 // x=x-3
x+=3 // x=x+3
x*=3 // x=x*3
x/=3 // x=x/3
x**=4 // x=x**4
--------------------------
'''

# a = 5
# b = 6
# a != b

'''
codu run etdim netice vermedi yalniz bu misalda
codlabda netice verdi true olaraq.
'''
# a = int(input("Ededi daxil edin:"))
# eded = a//10
# eded1 = a%10
# print(eded,eded1)

# a = int(input("Ededi daxil edin:"))
# # print(f'Netice: {a//10}')
# # print(f'Netice: {a%10}')


# a = int(input('1-ci terefi qeyd edin:'))
# b = int(input('2-ci terefi qeyd edin:'))
# print(f'Duzbucaqlinin parametri: {(a+b)*2}')


# a, b = map(int,input().split())
# paramert = (a+b)*2
# print(paramert)


# a = int(input('Ededi daxil edin:'))
# b = int(input('Ededi daxil edin:'))
# eded= (a+b)//2
# print(eded) 


# a1 = int(input('Ededi daxil edin:'))
# b1 = int(input('Ededi daxil edin:'))
# eded1= (a1+b1)//2
# print(eded1)

# a2, b2 = map(int,input().split())
# ededi_orta = (a2+b2)//2
# print(ededi_orta)

'''
If ,ELIF,ELSE
IF-eger/Meselen  eger(IF) yagis yagmasa men derse gedecem(Sert). Sertimiz dogru olsa true, yalnsi ise false
BIR KODDA Max 1 IF 1 ELSE
'''

# a = 65
# b = 29
# if a==b :
#     print("A")
# elif a<b:
#     print("B")
# else:
#     print("D")

# a = 65
# b = 29
# print("A")if a==b else print("B")

# a = 65
# b = 29
# if a!=b and a>b :
#     print("A")




# a = 91
# b = 81
# c = 71
# d = 51
# if a>b :
#     print("A")
# elif a<b:
#     print("B")
# elif a<c:
#     print("C")
# else:
#     print("D")

# a= input("Adinizi qeyd edin:")
# b = input("Soyadinizi qeyd edin:")
# c = int(input("Yasinizi qeyd edin:"))
# d = float(input("Gpa balinizi qeyd edin:"))
# e= float(input("Gpa tapilmasi Biologiya:"))
# print(f"Adiniz: {a}")
# print(f"Soyadiniz: {b}")
# print(f"Yasiniz: {c}")
# print(f"GpaBiologiya: {d}")
# print(f"Gpa Umumi: {(e+e)/2+10+10}")


# a = 6
# b = 5
# a=b
# print(a)
# print(type(a))

# eded=int(input())
# if eded%2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# x=int(input())
# if x<5:
#     y= x**2-3*x+4
# elif x>=5:
#     y=x+7
# print(y)

# x=int(input())
# if x<5:
#     y= x**2-3*x+4
# else:
#     y=x+7
# print(y)

# x, a, b = map(int,input().split())
# if a<=x<=b:
#     x=[a,b]
#     print("Yes")
# else:
#     print("NO")

# x, a, b =map(int,input().split())
# if a<=x<=b:
#     print("Yes")
# else:
#     print("No")


# x, a, b = map(int,input().split())
# if a<=x and x<=b:
#     print("Yes")
# else:
#     print("No")

# i = 0
# while i<10:
#     print("Backend Fatima Aliyeva")
#     i+=1
# #10 defe Backend Fatima Aliyeva Cap etdi.

# a = "Hello"
# for i in a:
#     print(a)
# Hello sozu 5 defe cap edilecek sebeb ise 5 herfden ibaret olmasidir.

# for i in range(5):
#     print(i)
# for i in range(5,12): # Istediyimiz  5,12 cap edecek/
#      print(i)
# for i in range(7, 30, 4):  #7-den  30-a qeder 4 vahid artirmaq.
#     print(i)
# for i in range(10, 56, 10): #10-dan  56-a qeder 10 vahid artirmaq.
#     print(i)

# a= int(input())
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")


# eded = int(input())
# say = 0
# while eded>0:
#     eded//=10
#     say+=1
# if say == 0:
#     say+=1
# print(say)


# for i in range(1):
#     i+=1
#     print(i)
# a= [1,2,2,3,4,5,6,7]
# print(a)
# a.remove(2)
# print(a)
# a.pop()
# print(a)
# a.pop(2)
# print(a)


# a=[1,2,3,4,5,6,7,8,9]
# a_1=a
# print("evvel")
# print(a_1,a)
# a_1[1]=1001
# print("sonra")
# print(a_1)
# a_1.append("Fatima Aliyeva Backend")
# print ("sonra1")
# print(a_1,a)

# a=[1,2,3,4,5,6,7,8,9,10]
# a1=a.copy()
# print("evvel")
# print("a =" , a  )
# print("a1=",a1)

# a1.append(100)
# print("Sonra")
# print("a =" , a )
# print("a1=",a1)
# for i in range(5):
#     print(i*5)

# metn=input("Zəhmət olmasa istədiyiniz söz və ya cümlə daxil edin: ");
# saitlər=0
# samitlər=0
# for i in metn:
#     if(i == 'A'or i == 'a'or i == 'I'or i == 'ı'or i == 'O' or
#        i == 'o'or i=='U' or i=='u' or i == 'E'or i == 'e'or i == 'Ə'or i == 'ə' or 
#        i == 'Ö' or i =="ö" or i =='Ü' or i =='ü' or i == 'İ' or i =='i'):
#            saitlər=saitlər+1;
#     else:
#         samitlər=samitlər+1;

# print("Saitlərin sayı:",saitlər);
# print("\nSamitlərin sayı:",samitlər);
# say_01=int(input("eded-1:"))
# say_02=int(input("eded-2:"))
# say_03=int(input("eded-3:"))
# if say_01<say_02<say_03:
#     print(say_02)
# elif say_02<say_03:
#     print(say_03)

# a='Fatima Aliyeva'
# print(len(a)) #Uzunlugunu gosterir yeni nece charekterden istifade oldugunu qeyd edir bosluqlarida sayir.
# print(a[-1])
# b=[]
# c=[1,2,3,4,5,6]
# print(b,c)
# print(len(b))
# print(len(c))
# print(f'B:{b[5]}-dir')
# a=["Fatima",20,5, ('Fatima',555),['Aliyev Kamran'],5] 
# #Listin icersinde her sey qeyd edile biler. Tuple,string int
# print(a)
# print(len(a))
# print(a[3][0])
# print(a[3][1])
# print(a[3])
# print(a[4])
# a.append(100) #Ancaq sona elave edir 
# a.insert(2,666) # istediyimiz yere elave etmek ucun istifade edilir. index vasitesile #2 burda index #666 reqem

# print(a)

# def PrintReverseOrder(N):
     
#     # if N is less than 1
#     # then return void function
#     if (N <= 0):
#         return;
#     else:
#         print(N, end = " ");
 
#         # recursive call of the function
#         PrintReverseOrder(N - 1);
         
# # Driver Code
# N = 5;
# PrintReverseOrder(N);
 
# # This code is contributed by Nidhi_biet

# Multiplication table (from 1 to 10) in Python

# num = 12

# # To take input from the user
# # num = int(input("Display multiplication table of? "))

# # Iterate 10 times from i = 1 to 10
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)
n=int(input())
reska=0
gerb=0
for i in range(n):
  qepik=int(input())
  if qepik==1:
      reska+=1
  else:
    gerb+=1
print(min(reska,gerb))






