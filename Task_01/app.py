# '''1) Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən,
# ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.'''
# a=int(input())
# print( f"Kvadratin sahesi= {a**2}")

# a, b, c, d=map(int,input().split())
# print( f"Kvadratin sahesi= {a*b*c*d}")

# a, b, c, d=map(int,input().split())
# print( f"Ededlerin cemi= {a+b+c+d}")

# '''2)Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.'''

# a, b, c, d=map(int,input().split())
# print( f"ededler = {a, b, c, d}")
# max(a, b, c, d)


# ''' 3)Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.'''

# menu = ["alma", "tut", "encir", "nar"]
# print (menu)

# meyve = input("Sevdiyiniz meyvenin adini yazin: ")
# if meyve=="alma":
#     print ("1manat")
# elif meyve=="tut":
#     print ("4manat")
# elif meyve=="encir":
#     print ("2manat")
# elif meyve=="nar":
#     print ("2manat")
# else:
#     print ("qeyd edilien meyve menuda yoxdur")

# '''5)Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.'''



# list_02 = [1,2,3,4]
# sum = 0
# for i in range(0,len(list_02)):
#     sum = sum + list_02[i]

# print(sum)

# "9. Write a Python program to check a list is empty or not."

# list_1 = [1,2,3,4,5]

# if len(list_1) == 0:
#     print("empty")
# else:
#     print(list_1,"no empty list")




# ''' 10) my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.” my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.'''
# my_text = "Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."
# sorted_characters = sorted(my_text)
# my_text = "". join(sorted_characters)
# print(my_text)

# '''4)Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.'''
# name = input("Adinizi daxil edin: ")
# if 3<len(name)<11:
#     surname = input("Soyadinizi daxil edin: ")
#     if 5<len(surname)<15:
#         year = input("Dogum ilinizi daxil edin: ")
#         if len(year) == 4:
#             email = input("Emailinizi daxil edin: ")
#             if 10<len(email)<22 and email.split("@")[1] == "gmail.com":
#                 password = input("Parolunuzu daxil edin: ")
#                 if 6<len(password)<13:
#                     confirm_password = input("Parolunuzu tesdiqleyin: ")
#                     if confirm_password == password:
#                         print("Qeydiyyat tamamlandi!")
#                         question = input("Qeydiyyatin detallarina baxmaq isteyirsiniz?Y/N")
#                         if question == "Y" or question == "y":
#                             print(f'Adiniz: {name}, Soyadiniz: {surname}, Dogum iliniz: {year}, Emailiniz: {email}, Parolunuz: {password}')
#                         else:
#                             print(f'{name}, Ugurlar!')
#                     else:
#                         print("Parol eyni deyil!")
#                 else:
#                     print("Parol min. 6, maks. 13 simvoldan ibaret ola biler!")
#             else:
#                 print("Email min. 10, maks. 22 simvoldan ibaret ola biler ve sonu @gmail.com ile bitmelidir.")
#         else:
#             print("Dogum iliniz 4 simvoldan ibaret olmalidir!")
#     else:
#         print("Soyadiniz min. 5, maks. 15 simvoldan ibaret ola biler!")
# else:
#     print("Adiniz min. 3, maks. 11 simvoldan ibaret ola biler.")

# print("5. Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.")
# ''' 11)Write a Python program to select the odd items of a list.

# '''
# eded=[]
# eded=int(input())
# if eded%2 == 0:
#     print("EVEN")
# else:
#     print("ODD")
# '''12)Write a Python function to sum all the numbers in a list.'''
# def sum(ededler):
#     total = 0
#     for x in ededler:
#         total += x
#     return total
# print(sum((1, 2, 3, 4, 5)))

# list1 = [10, 20, 4, 45, 99]
# list1.sort()
# print("En kicik eded:", *list1[:1])


# '''16. Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.")'''
# gun = int(input("Bir eded yazin: "))
# def heftenin_gunləri(gun):
#     if gun == 1:
#         return "Bazar ertesi"
#     elif gun == 2:
#         return "Çərşənbə axşamı"
#     elif gun == 3:
#         return "Çərçənbə"
#     elif gun == 4:
#         return "Cümə axşamı"
#     elif gun == 5:
#         return "Cümə"
#     elif gun == 6:
#         return "Şənbə"
#     elif gun == 7:
#         return "Bazar"
#     else:
#         return None

# print(heftenin_gunləri(gun))
