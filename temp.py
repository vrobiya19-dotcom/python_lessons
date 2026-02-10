# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#LISTS LESSON 3

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'audi']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# print(sorted(cars, reverse = True))

# son = [12, 34, 67, 87, 32, 78, 21, -65, 100, -1.3]
# print(sorted(son, reverse = True))

# cars.reverse()
# print(cars)

# print(len(cars))

# uzunlik = len(son)
# print(uzunlik)

# sonlar = list(range(0, 11))
# print(sonlar)

# toq = list(range(1, 20, 2))
# print(toq)

# juft = list(range(0, 20, 2))
# print(juft)

# num = list(range(0, 101, 10))
# print(num)

# maxqiy = max(toq)
# print(maxqiy)

# minqiy = (321, 54365, 6353, 1213, 745, 7643)
# print(min(minqiy))

# print(sum(minqiy))

# print(cars[0])

# print(cars[3])

# print(cars[0:3])

# print(cars[:3])

# print(cars[1:])

# my_cars = cars
# print(cars)
# print(my_cars)

# my_cars.remove('volvo')
# print(my_cars)

# my_cars[0] = 'lacetti'
# print(my_cars)

# print(cars)
# print(my_cars)

# cars.append('bmw')
# print(cars)


# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'audi']
# my_cars = cars[:]
# print(my_cars)

# my_cars.remove('bmw')
# print(my_cars)
# print(cars)

# #TUPLE

# toys = ('bus', 'car', 'bear', 'dino')
# print(toys[0])

# print(toys[2:5])
# toys = list(toys)
# print(type(toys))

# davlat = ['London', 'USA', 'Uzbekistan', 'Russia', 'Japan']
# print(len(davlat))

# print(sorted(davlat))

# print(sorted(davlat, reverse = True))

# print(davlat)

# davlat.reverse()
# print(davlat)

# davlat.sort()
# print(davlat)

# davlat.sort(reverse = True)
# print(davlat)

# jufts = list(range(120, 1201))
# print(jufts)

# print(sum(jufts))


# j = min(jufts)
# k = max(jufts)
# print(k-j)

# print(k+j)

# print(len(jufts))

# print(jufts)
# print(jufts[20])

# print(jufts[-20])

# print(jufts[530:550])


# taomlar = ['somsa', 'shorva', 'osh', 'sushi', 'pizza']

# nonushta = taomlar[:]
# print(nonushta)

# nonushta.remove('shorva')
# nonushta.remove('osh')
# nonushta.remove('sushi')
# nonushta.remove('pizza')
# nonushta.append('saryoqli non')
# nonushta.append("tuxum")
# print(nonushta)

# taomlar = nonushta
# print(taomlar)
# print(nonushta)

# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq'
# print(nonushta)


#Lesson 2

# mehmonlar = ['Ali', 'Vali', 'Olim', 'Hasan', 'Husan']
# for i in mehmonlar:
#     print("Salom,", i)
#     print("Hayr,", i)

# sonlar = list(range(1,11))
# for i in sonlar:
#     print(f"{i} sonning kvadrati {i**2}!") 
    
# dostlar = []
# print("5 ta emg yaqin dostingizni ismingiz kim?")
# for i in range(5):
#     dostlar.append(input(f"{i+1}-dostingizning ismini kiriting: "))
# print(dostlar)


# ismlar = ['Robiya', 'Sabina', 'Diyora', 'Muslima', 'Hadicha']
# for i in ismlar:
#     print("hello,", i)

# print("kod", len(ismlar), 'marta takrorlandi')

# sonlar = list(range(1, 101, 2))
# for s in sonlar:
#     print(s**2)
    
# kinolar = []
# print("5 ta sevimli kinolaringizni kiriting: ")
# for i in range(5):
#     kinolar.append(input(f"{i+1}-kinoning nomini kiriting: "))
    
# print(kinolar)

# n_people = int(input("Bugun nechi kishi bilan suhbat qildizngiz?>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qurgan odamingiz kim?:"))
# print(ismlar)


#LESSON 3 

# avtolar = ['audi', 'bmw', 'porsche', 'ferrari', 'bugatti', 'pagani']
# for avto in avtolar:
#      if avto == 'bmw':
#          print(avto.upper())
#      else:
#          print(avto.title())


# javob = float(input("12 x 6 nechiga teng?>>>>"))
# if javob != 72:
#     print("javob xato")
# else:
#     print("Togri")

# yosh = int(input("yosh?>>>"))
# if yosh >= 18:
#     print('Ke')
# else:
#     print("yoqol")
    
    
# login = input("Yangi login kiriting: ")
# if len(login)<5:
#     print("login 5 ta harfdan uzun bolishi shart!")
# else:
#     print("Hush kelibsiz!")
    
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2026-yil<18:
#     print(f"sizning yoshingiz {2026-yil}da ekan")
#     print("Kirish mumkin emas")
# else:
#     print("Xush kelibsiz!")
    

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz covid riskdasiz")


# x, y = 25, 50
# print("x>y") if x>y else print("x<y")

 
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for i in cars:
#     if i != 'gm':
#         print(i.upper())
#     else:
#         print(i.title())
        

# name = input("What is your name?>>")
# if name == 'admin':
#     print("Welcome admin! do you want to see the menu?")
# else:
#     print(f"Welcome, {name}!")
    
# son1 = input("Birinchi sonni kiriting>>")
# son2 = input("Ikkinchi sonni kiriting>>")
# if son1 == son2:
#     print("Sonlar bir xil")
# else:
#     print("Sonlar teng emas!")
    

# manfiy = int(input("Istalgan sonni kiriting>>"))
# if manfiy < 0:
#     print("Maxfiy son")
# else:
#     print("Musbat son")
    
    
# son = float(input("Istalgan sonni kiriting: "))
# print(son**(1/2) if son>0 else print('Musbat son kiriting!'))


#LESSON 4
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat >=30:
#     print("cho'milgani kettik")
# elif kun.lower()=='yakshanba' and harorat <=30:
#     print("Uyda dam olamiz!")
 
    
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi!')
# else:
#     print('Afsuski bizda bunday ovqat yoq!')
    

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
# if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#              print(f"Menuda {taom} bor!")
#        else: 
#              print(f"Kechirasiz, menuda {taom} yo'q!")

# juft = float(input("Juft son kiriting>>"))
# if juft %2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu juft son emas!")
    


# yosh = int(input("Yoshingizni kiriting>>"))
# if yosh <= 4 or yosh >=60:
#     print("Bepul")
# elif yosh <= 18:
#     print("10.000")
# else:
#     print("20.000")


# son1 = int(input("1-sonni kiriting>>"))
# son2 = int(input("2-sonni kiriting>>"))
# if son1 == son2:
#     print("teng")
# elif son1 > son2:
#     print("1-son 2-sondan katta")
# elif son1 < son2:
#     print("2-son 1-sondan katta")


# mahsulotlar = ['olma', 'olcha', 'gilos', 'tuxum', 'non', 'sut', 'suv', 'kartoshka', 'anor']
# savat = []
# for i in range(5):
#     savat.append(input(f"savatga {i+1}-mahsulotni qoshing>>"))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Dokonimizda {mahsulot} bor")
#     else:
#         print(f"Dokonimizda {mahsulot} yoq")



# mahsulotlar = ['olma', 'olcha', 'gilos', 'tuxum', 'non', 'sut', 'suv', 'kartoshka', 'anor']
# savat = []
# for i in range(5):
#     savat.append(input(f"savatga {i+1}-mahsulotni qoshing>>"))

# bor_mahsulotlar = []
# mavjud_emas = []
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
        
# if mavjud_emas:
#     print(f"Dokonimizda quyidagi mahsulotlar yoq:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz soragan barcha mahsulotlar bor")



# foydalanuvchilar = ["user1", 'user2', 'user3', 'user4', 'user5']
# user = input("login yarating>>")
# if user in foydalanuvchilar:
#     print("Login band, yengi yarating>>")
# else:
#     print("Xush kelibsiz")
    

# son = int(input("Son kiriting: "))
# for i in range(2, 11):
#     if not (son%i):
#         print(f"{son} soni {i} ga qoldiqsiz bolinadi")



#DICTIONARY

# car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# mevalar = {'olma':10000,'tarvuz':8000,'qovun':10000}
# print(f"olmalar narxi {mevalar['olma']} som")

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()}, \
# {talaba_0['t_yil']}-yilda tug'ilgan, \
# {talaba_0['yosh']} yoshda")

# talaba_0['kurs'] = 4
# talaba_0['fakultitet'] = 'Informatika'
# print(talaba_0)


# print(talaba_0['yosh'])

# talaba_0['ism'] = 'Sabina'
# print(talaba_0)

# talaba_1 = {}
# talaba_1['kurs'] = 3
# talaba_1['ism'] = 'Mubina'
# talaba_1['yosh'] = 20

# print(talaba_1)

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)

# print(talaba_1)
# del talaba_1['kurs']
# print(talaba_1)

# user = talaba_1.get('Mubina', 'Bunday student mavjud emas')
# print(user)


# otam = {'ism':'Rahmatjon', 'tug_y': 1887, 'tug_sh':'Fargona'}
# print(f"Otamning ismi {otam['ism']}, {otam['tug_y']}-yilda, {otam['tug_sh']} viloyatida tug'ilganlar")

# taom = {
#         'Muhammad Ali':'Pizza',
#         'Muslima':'Donar',
#         'Mubina':'Lavash',
#         'Hadicha':'Chips',
#         'Nigina':'Pyure suvi'
#         }

# print(f"Muhammad Alining sevgan taomi {taom['Muhammad Ali']}")
# print(f"Muslimaning sevgan taomi {taom['Muslima']}")
# print(f"Hadichaning sevgan taomi {taom['Hadicha']}")

# py = {
#       'int':'butun son',
#       'str':'soz',
#       'bool':'True yoki False',
#       'float':'kasrli son',
#       }

# print(py['int'])
# print(py['str'])
# print(py['bool'])
# print(py['float'])

# user = input("soz kiriting - tarjimasini biling:>>").lower()
# tarjima = py.get(user)
# if user == None:
#     print('Bunday soz mavjud emas')
# else:
#     print(f"{user.title()} sozi {tarjima} deb tarjima qilinadi")
    
    

# talaba_0 = {
#     'ism':'Alijon',
#     'familiya':'Shamsiyev',
#     'yosh':22,
#     'fakultitet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n") 
    
    
# mahsulotlar = {
#        'olma':10000,
#        'anor':20000,
#        'ananas':50000,
#        'gilos':50000,
#        }
# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
    
# print("Dokondagi mahsulotlar:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())   

# print(mahsulotlar.keys())
# print(mahsulotlar.values())


# for m in mahsulotlar.values():
#     print(m)
    
# print("*****************")
    
# for ma in set(mahsulotlar.values()):
#     print(ma)



# py_keys = {
#     'int':'butun son',
#     'bool':'True, False',
#     'str':'soz',
#     'float':'kasrli son'
#     }

# for keys, values in sorted(py_keys.items()):
#     print(f"{keys.title()} - {values}")


# dav = {
#        'Uzbekistan':'Tashkent',
#        'Russia':'Moskva',
#        'USA':'Washington',
#        'Tajikistan':'Dushanbe',
#        'Kyrgizystan':'Bishkek',
#        'Kazakystan':'Nursultan'
#        }

# for d in sorted(dav):
#     print(d)
    
# print("``" * 10)
    
# for d in sorted(dav.values()):
#     print(d)



# country = input("Qaysi davlatni poytaxtini bilishni xohlaysiz?")
# capital = dav.get(country)
# if country == None:
#     print('Davlat topilmadi!!')
# else:
#     print(f"{country.title()}ning poytaxti {capital}")


# taomlar = {
#     'Pizza':60000,
#     'Lavash':25000,
#     'KFC':30000,
#     'Hot Dog':20000,
#     'Sezr':30000,
#     'Sushi':35000,
#     'Shashlik':15000,
#     'Burger':30000,
#     'Donar':35000,
#     'Free':15000,
#     'Pepsi':25000,
#     'Cola':25000,
#     'Cherry Juice':25000
#     }

# buyurtmalar = []
# for i in range(3):
#     buyurtmalar.append(input(f"{i+1}-ovqatni buyurtma bering>>"))
    
#     for b in buyurtmalar:
#         if b in taomlar:
#             print(f"{b.title()} {taomlar[b]} som")
#         else:
#             print(f"Kechirasiz, bizda {b} yoq")



#NESTING

# car0 = {
#         'model':'Lacetti',
#         'rang':'qora',
#         'yil':1998
#         }

# car1 = {
#         'model':'Mazda',
#         'rang':'qizil',
#         'yil':2003
#         }

# car2 = {
#         'model':'Lamborghini',
#         'rang':'sariq',
#         'yil':2009
#         }


# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, {car['rang']} rang, {car['yil']}-yil")

# print(cars[0]['model'])


# print(f"{cars[2]['rang'].title()} {cars[2]['model']}")


# malibus = []
# for n in range(10):
#     newcar = {
#         'model':'Malibu',
#         'rang':None,
#         'yil':2020,
#         'narx':None,
#         'km':0,
#         'karobka':'avto'
#         }
#     malibus.append(newcar)
    
# # for m in malibus:
# #     print(m)

# for m in malibus[:3]:
#     m['rang'] = 'qizil'
    
# print(malibus)

# for m in malibus[3:6]:
#     m['rang'] = 'qora'
#     m['korobka'] = 'mexanika'
    
# print(malibus)


# for m in malibus[6:]:
#     m['rang'] = 'qora'
#     m['korobka'] = 'mexanika'
    
# print(malibus)  


# for m in malibus:
#     if m['karobka'] == 'avto':
#         m['narx'] = 40000
#     else:
#         m['narx'] = 35000
        
        
# dasturchilar = {
#     'ali':['python', 'c++'],
#     'vali':['html', 'css', 'js'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['css', 'c++']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()}", end = '')
        

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':2001,
#            'malumot':'orta-maxsus',
#            'tillar':['html', 'css', 'js']
#         },
#     'vali':{'familiya':'aliyev',
#             'tyil':2002,
#             'malumot':'oliy',
#             'tillar':['python', 'php']
#         },
#     'hasan':{'familiya':'husanov',
#              'tyil':2003,
#              'malumot':'orta-maxsus',
#              'tillar':['python', 'css']
#         }
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, {info['tyil']}-yilda tugilgan. Malumoti {info['malumot']}. \nQuyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())


# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil', 
#     'tyil':810,
#     'vyil':870,
#     'tjoy':'Buxoro',
#     'asarlari': ['Al-Jome as sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir', 'At-tarix as-sagir']
#     }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Buxoro',
#            'asarlari': ['Otgan kunlar', 'Mehrobdan chayon', 'Obid ketmon']
#     }

# vohidiy = {'ism':'Erkin Vohidov',
#            'tyil':1894,
#            'vyil':2016,
#            'tjoy':'Toshkent',
#            'asarlari': ['Tong Nafasi', 'Qoshiqlari sizga', 'Ozbegim', 'Qiziquvchan Matmusa']
#            }

# navoiy = {'ism':'Alisher Navoiy',
#           'tyil':1441,
#           'vyil':1501,
#           'tjoy':'Xirot',
#           'asarlari': ['Xamsa', 'Lison ut-Tayir', 'Mahbub al-qulub', 'Munojot']
#     }

# shaxslar = [buxoriy, qodiriy, vohidiy, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlari']
#     print(f"* * * * * * * * * * * * * * *\n{ism}ning mashxur asarlari:")
#     for asar in asarlar:
#         print(asar)


# sev_kinolar = {
#     'Muslima': ['Cruella', 'My Demon', 'Head over Heels'],
#     'Mubina': ['Love in the Clouds', 'Speed and Love', 'Deep Affection Eyes'],
#     'Hadicha': ['Only for Love', 'The first frost', 'Twinkling watermelon'],
#     'Nigina': ['Study Group', 'Descendance of the sun', 'When I fly towards you'],
#     'Omina': ['Lighter and princess', 'Falling into your smile', 'Hidden Love']
#     }
# for ism, kinolar in sev_kinolar.items():
#     print(f"{ism}ning sevgan kinolari:")
#     for k in kinolar:
#         print(k)


# davlatlar = {
#     'Ozbekiston':{'poytaxti':'Toshkent',
#                   'maydon':448978,
#                   'aholi':33_000_000,
#                   'pul birligi':'som'
#         },
    
#     'Rossiya':{'poytaxti':'Moskva',
#                'maydon':17_098_256,
#                'aholi':144_000_000,
#                'pul birligi':'rubl'
#         },
    
#     'aqsh':{'poytaxti':'Washington',
#             'maydon':9_631_418,
#             'aholi':327_000_000,
#             'pul birligi':'dollar'
#         },
    
#     'Malayziya':{'poytaxti':'Kuala-Lumpur',
#                  'maydon':329750,
#                  'aholi':25_000_000,
#                  'pul birligi':'rinngit'
#         }
#     }

# davlat = input('Bilmoqchi bolgan davlatizngizni nomini kiriting>>')
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxti'].title()}"
#           f"\nHududi:{info['maydon']}"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlatning infosi mavjud emas!")
        
    

#WHILE

# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son += 1


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)


# print('Kiritilgan sonning kvadratini qaytaruvchi dastur.')
# savol = 'Istalgan son kiriting'
# savol += '(dasturni toxtatish uchun "exit" deb yozing.)'
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi')


# print('Kiritilgan sonni kvadratini hisoblovchi dastur!')
# savol = 'Istalgan sonni kiritng'
# savol += '(dasturni toxtatish uchun "exit" dev yozing)>>'
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(int(qiymat)**2)


# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son}ning kvadrati {son**2}")


# son = 0
# while son < 10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)


# kit = 'Yaxshi korgan kitobilarimgizni kiriting (toxtash uchun "exit"ni bosing)>>'
# kito = True
# while kito:
#     kir = input(kit)
#     if kir == 'exit':
#         break
#     else:
#         print(kir)


# ask = 'yoshingizni kiriting: '

# while True:
#     qiymat = input(ask)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh <= 7:
#         narx = 2000
#     elif 7<= yosh < 18:
#         narx = 3000
#     elif 18<= yosh < 65:
#         narx = 10000
#     else: narx = 0
    
#     if narx == 0:
#         print('Sizga kirish bepul')
#     else:
#         print(f"chipta {narx} som")
        

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     elif int(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
    

 
#WHILE 2

# ismlar = []
# n = 1
# while True:
#     ism = input(f'{n}-dostingizni ismin kiriting: ')
#     ismlar.append(ism)
#     takrorlash = input('Yana dostingizni ismini qoshishni hohlaysizmi? (ha/yoq)>>')
#     n+=1
#     if takrorlash != 'ha':
#         break
    
# print('Dostlaringizni royxati:')
# for ism in ismlar:
#     print(ism.title())


# dostlar = {}
# ishora = True
# while ishora:
#     ism = input('dostingizni ismini kiriting>>')
#     yosh = int(input('dostingizni yoshini kiritin>>'))
#     dostlar[ism] = int(yosh)
#     takr = input('yana qaytadan dostingiz haqida malumot kiritishni hohlaysizmi? (ha/yoq)')
    
#     if takr != 'ha':
#         ishora = False
        
# for ism, yosh in dostlar.items():
#     print(f'dostingizni ismi:{ism.title()}, yoshi {yosh}')
    

# cars = ['nexia', 'lacetti', 'toyota', 'nexia', 'lamborghini', 'nexia']
# car = 'nexia'
# while car in cars:
#     cars.remove(car)
# print(cars)


# talabalar = ['hasan', 'husan', 'fotima', 'zuhra']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f'{talaba.title()}ning bahosini kiriting: ')
#     print(f'{talaba} baholandi!')
#     baholangan_talabalar[talaba] = int(baho)
    
# print(baholangan_talabalar)


# mah = []
# ishora = True
# while ishora:
#     mahi = input('Mahsulot nomini kiriting (toxtatish uchun "stop"ni bosing)>>>')
#     mahs = mah.append(mahi)
#     if mahi == 'stop':
#         ishora = False
        
#         for m in mah:
#             print(m)
    
# eboz = {}
# ishora = True
# while ishora:
#     mahsulot = input('Mahsulot nomini kiriting>>')
#     narx = int(input('Narxni kiriting>>'))
#     eboz[mahsulot] = int(narx)
    
#     stoppie = input("Toxtatish uchun 'stop' ni yozing!, davom ettirish uchun enterni>")
    
#     if stoppie == 'stop':
#         ishora = False
        
# for m in mah:
#     if m in eboz:
#         print(f'{m} korzinkada bor!!!')
        
# for mahsulot, narx in eboz.items():
#     print(f'mahsulot: {mahsulot}, narxi:{narx}')
    


#DEF FUNCTION

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print('Assalomu alaykum')
    
# salom_ber()


# def salom_ber(ism):
#     #foydalanuvchini ismini qabul qilib salom beruvchi funksiya!
#     print(f"Assalomu alaykum, xurmatli {ism.title()}")
    
# salom_ber('Hasan')
# salom_ber('Sabina')


# def toliq_ism(ism, familiya):
#     print(f'foydalanuvchining ismi: {ism}, familiyasi: {familiya}')

# toliq_ism('hasan', 'olimov')


# def yosh_hisobla(ism, tugilgan_yil):
#     print(f"foydalanuvcining ismi: {ism}, yoshi: {2026-tugilgan_yil}")
    
# yosh_hisobla(tugilgan_yil=2007, ism='Sabina')


# def yosh_hisobla(tugilganyil, joriyyil=2026):
#     print(f"Mubina {tugilganyil}da tugilgan, va u {joriyyil-tugilganyil} yoshda!")
    
# yosh_hisobla(2007, 2026)


# def yoshhisobla(ism, yil):
#     print(f"Foydalanuvchi: {ism}, yoshi {2026-yil}da")
    
# yoshhisobla('Mubina', 2007)


# def kvadratvakub(kvadrat, kub):
#     print(f'sonning kvadrati: {kvadrat**2}, kubi: {kub**3}')
    
# kvadratvakub(5, 4)


# def blahhh(son):
#     if son %2 == 0:
#         print(f'{son} bu juft son!!')
#     else:
#         print(f'{son} bu toq son!')

# blahhh(19)


# def foff(son1, son2):
#     if son1>son2:
#         print(f'{son1} kotta {son2} dan!')
#     else:
#         print(f'{son1} kichkina {son2} dan!')

# foff(8, 5)


# def wha(x, y=2):
#     print(f'{x}ning {y}-inchi darajasi: {x**y} ga teng!')

# wha(99)


# def getthefoff(son):
#     for i in range(2, 11):
#         if son%i == 0:
#             print(f'{son} {i} ga qoldiqsiz bolinadi!')

# getthefoff(4)



#DEF FUNCTION PART 2

# def toliq_ism_yasa(ism, familiya):
#     toliq_ism = f'{ism} {familiya}'
#     return toliq_ism

# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# print(talaba1)
    

# def toliqismyasa(ism, familiya, otasiningismi=''):
#     if otasiningismi:
#         toliq_ism = f'{ism} {otasiningismi} {familiya}'
#     else:
#         toliq_ism = f'{ism} {familiya}'
#     return toliq_ism.title()
    
# ism1 = toliqismyasa('olim', 'xolmetov')
# ism2 = toliqismyasa('ravshan', 'olimovich', 'hakimov')

# print(f'bugun darsga {ism1} va {ism2} lar kelmadi')


# def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narx':narxi}
#     return avto
# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Lacetti', 'Oq', 'Avtomat', 2020, 50000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud moshinalar:')
# for avto in avtolar:
#     if avto['narx']:
#         narxi = avto['narx']
#     else:
#         narxi= 'Nomalum'
#         print(f'{avto['rang']} {avto['model']}. Narxi: {narxi}') 


# # def oraliq(min, max):
# #     sonlar = []
# #     while min<max:
# #         sonlar.append(min)
# #         min += 1
# #     return sonlar
    
# # print(oraliq(0, 10))
# # print(oraliq(10, 20))

# # sonlar = oraliq(20,30)
# # print(sonlar)

# def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narx':narxi}
#     return avto
# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Lacetti', 'Oq', 'Avtomat', 2020, 50000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud moshinalar:')
# for avto in avtolar:
#     if avto['narx']:
#         narxi = avto['narx']
#     else:
#         narxi= 'Nomalum'
#         print(f'{avto['rang']} {avto['model']}. Narxi: {narxi}') 

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input(" Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break



# def toliqismyasa(ism, familiya, otasiningismi=''):
#     if otasiningismi:
#         toliq_ism = f'{ism} {otasiningismi} {familiya}'
#     else:
#         toliq_ism = f'{ism} {familiya}'
#     return toliq_ism.title()
    
# ism1 = toliqismyasa('olim', 'xolmetov')
# ism2 = toliqismyasa('ravshan', 'olimovich', 'hakimov')

# print(f'bugun darsga {ism1} va {ism2} lar kelmadi')


# print('Onlayn bozordagi mavjud moshinalar:')
# for avto in avtolar:
#     if avto['narx']:
#         narxi = avto['narx']
#     else:
#         narxi= 'Nomalum'
#         print(f'{avto['rang']} {avto['model']}. Narxi: {narxi}') 



# def userinfo(ism, familiya, yil, joy, email=None , tel=None):
    
#     user = {'ism':ism,
#             'familiya':familiya,
#             'yil':yil,
#             'joy':joy,
#             'email':email,
#             'tel':tel
#         }
#     return user

# user1 = userinfo('Muslima', 'Vaxobova', 2009, 'Yangiyol', 'vaxobova_03@gmail.com', 998987463663)
# user2 = userinfo('Hadicha', 'Vaxobova', 2020, 'Yangilyol') 
# users = [user1, user2]
# print('User malumotlar')
# for user in users:
#     if user['email']:
#         email = user['email']
#     else:
#         email = 'Nomalum'
#     if user['tel']:
#         tel = user['tel']
#     else:
#         tel = 'Nomalum'
    
        
#     print(f"{user['ism']} {user['familiya']} {user['yil']} {user['joy']} {user['email']} {user['tel']}")
        
        
# def mijozlarwithdiction(ism, familiya, tyil, tjoy, email=None, tel=None):
#     mijozlar = {'ism':ism,
#                 'familiya':familiya,
#                 'tyil':tyil,
#                 'tjoy':tjoy,
#                 'email':email,
#                 'tel':tel
#         }        
#     return mijozlar

# print('Mijozlar haqida malumotlar:')
# user = []
# while True:
#     ism = input('Ismingizni kiriting>>')
#     familiya = input('Familiyangizni kiriting>>')
#     tyil = input('Tugilgan yilingizni kiriting>>')
#     tjoy = input('Tugilgan joyingizni kiriting>>')
#     email = input('Emailingizni kiriting (xohishiy)>>')
#     tel = input('Tel raqamingizni kiriting (xohishiy)>>')
#     user.append(mijozlarwithdiction(ism, familiya, tyil, tjoy, email, tel))
#     javob = input('Davom etasizmi? (ha/yoq)')
#     if javob != 'ha':
#         break
        
# for us in user:
#     print(f'mijoz ismi {us["ism"]}, familiyasi: {us["familiya"]}, tugilgan yili: {us["tyil"]}, tugilgan joy: {us["tjoy"]}, email:{us["email"]}, tel:{us["tel"]}')
         

# def numbers(a, b, c):
#     sonlar = [a, b, c]
#     return max(sonlar)
    
# son1 = int(input('Birinchi sonni kiriting>>'))
# son2 = int(input('Ikkinchi sonni kiriting>>'))
# son3 = int(input('Uchinchi sonni kiriting>>'))

# numberall = numbers(son1, son2, son3)
# print(numberall)


# def aylana_info(radius, pi=3.14159):
#     aylana = {'radius':radius,
#               'diametr':2*radius,
#               'perimetr':2*radius*pi,
#               'yuza':pi*radius**2
#         }
#     return aylana

# circle = aylana_info(3)
# print(circle)


# def tub_xabar(n):
#     if n < 2:
#         return f"{n} tub son emas!"
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return f"{n} tub son emas!"
    
#     return f"{n} bu tub son!"

# result = tub_xabar(4)
# print(result)
            

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))



#DEF PART 3
# def bahola(talabalar):
#     baholar={}
#     while talabalar:
#         ism = talabalar.pop()
#         baho = int(input(f'{ism}ga baho qoying>>'))
#         baholar[ism] = int(baho)
#     return baholar

# talabalaree = ['Ali', 'Usmon', 'Umar', 'Hasan', 'Husan']
# result = bahola(talabalaree)

# print(result)

# print('Baholangan talabalar:')
# for i in result:
#     print(i)


# def kattaxarf(katta):
#     users = []
#     while True:
#         user = input('Dostlaringizni ismini kiriting>>')
#         users.append(user.capitalize())
        
#         ask = input('Yana dostingizni ismini kiritishni hohlaysizmi? (ha/yoq)')
#         if ask != 'ha':
#             break
        
#     return users

# result = kattaxarf()
# print(result)


# def kattaharf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):  
#         matnlar[i] = matnlar[i].title()
#     return matnlar
        
# ismlar = ['ali', 'bobur', 'hasan', 'husan', 'fotima']
# kattaharf(ismlar)
# print(ismlar)
# yangiismlar = kattaharf(ismlar)
# print(yangiismlar)


# talabalar = ['Ali', 'Hasan', 'Husan', 'Eshmat', 'Toshmat']

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f'{ism.title()}ning bahosini kiriting>>')
#         baholar[ism] = int(baho)
#     return baholar

# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)


# talabalar = ['Ali', 'Hasan', 'Husan', 'Husan', 'Eshmat', 'Toshmat']

# def bahola(talaba):
#     baholar = {}
#     for ism in talaba:
#         baho = input(f'{ism}ning bahosini kiriting>>')
#         baholar[ism] = int(baho)
#     return baholar

# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)



#DEF PART 4 *args **kwargs

# def summa(*sonlar):
#     yigindi = 0
#     for i in sonlar:
#         yigindi += i
#     return yigindi

# result = summa(1, 2, 3, 4)
# print(result)
        
     
# def summa(*sonlar):
#     return sum(sonlar)

# print(summa(100, 304, 334))

# def summa(x, y, *sonlar):
#     return x+y+sum(sonlar)

# print(summa(1, 3))


# def avto_info(kompaniya, model, **malumotlar):
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info('GM', 'Lacetti', narxi=20000, rangi='qora')
# print(avto1)


# def yigindiall(*sonlar):
#     yigindi = 1
#     for son in sonlar:
#         yigindi *= son
#     return yigindi
# print(yigindiall(1, 2, 3, 4))


# def hisobla(*kopaytuvchilar):
#     kopaytmalar = 1
#     for kopaytir in kopaytuvchilar:
#         kopaytmalar *= kopaytir
#     return kopaytmalar
# print(hisobla(1,2,3,4,5))


# def talabalarmal(ism, familiya, **malumotlar):
#     malumotlar['ism']=ism
#     malumotlar['familiya']=familiya
#     return malumotlar
# print(talabalarmal('Robiya', 'Vaxobova', yil=2008, oqishdarajasi="A'lo"))



#MODULOS


# import examplepageforspyder

# result = examplepageforspyder.hisobla(1, 2, 3)
# print(result)


# import examplepageforspyder as ex

# result = ex.hisobla(3, 4, 5)
# print(result)


# from examplepageforspyder import hisobla
# print(hisobla(1, 2, 4, 5))


# from examplepageforspyder import hisobla as ha

# print(ha(6, 7, 8))


# from examplepageforspyder import *
# print(hisobla(10, 20, 30))


# import math

# x = 400
# print(math.sqrt(x))
# print(math.pow(5, 2))
# print(math.pi)
# print(math.log2(8))
# print(math.log10(5))


# import random as r
# # son = r.randint(0, 100)
# # print(son)

# # ismlar = ['Muslima', 'Ali', 'Mubina', 'Robiya', 'Nigina', 'Hadicha', 'Omina']
# # ism = r.choice(ismlar)
# # print(ism)

# # x = list(range(10, 30))
# # print(x)
# # print(r.choice(x))


# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)



#LAMBDA

import math


# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi, 10))


# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))


# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)

# print(f'3-ning kvadrati {kvadrat(3)}ga, kubi {kub(3)}ga teng')


from math import sqrt

sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)


# def daraja2(x):
#     return x**2

# print(list(map(daraja2, sonlar)))


# import random as r

# sonlar = r.sample(range(100), 10)

# def juftmi(x):
#     return x%2==0
# juftsonlar = list(filter(juftmi, sonlar))
# print(sonlar)
# print(juftsonlar)


# sonlar = r.sample(range(100), 10)
# juftsonlar = list(filter(lambda son: son%2==0, sonlar))
# print(juftsonlar)


# mevalar = ['anor', 'olma', 'banan', 'ananas', 'olcha', 'gilos']
# mevasarala = list(filter(lambda meva: meva.startswith('a'), mevalar))
# print(mevasarala)

# mevalar = ['anor', 'olma', 'banan', 'ananas', 'olcha', 'gilos']
# mevalar2 = list(filter(lambda meva: len(meva)<=5, mevalar))
# print(mevalar2)


# mevalar3 = list(filter(lambda meva: meva.startswith('a') and meva.endswith('r'), mevalar))
# print(mevalar3)



#CLASS AND OBJECT

# matn = 'Assalomu alaykum'

# class Komputer:
#     def __init__(self, model, cpu, gpu, hdd, ram):
#         self.model = model
#         self.cpu = cpu
#         self.gpu =gpu
#         self.hdd = hdd
#         self.ram = ram
        
#     def info(self):
#         infor = f"{self.model}, CPU: {self.ram}, GPU: {self.gpu}, HDD: {self.hdd}, RAM: {self.ram}"
#         return infor
    
# nitro = Komputer('Acer Nitro', 'i9', 'NVIDIA', 'M1', '16GB')
# print(nitro.info()) 







































