yosh = int(input("yoshingizni kiriting "))
if yosh<=8 and yosh>=0:
    print("chegirma 80 %")
elif yosh >8 and yosh <=18:
    print("chegirma 30 %")
elif yosh>18 and yosh <=60:
    print("chegirma 0 %")
elif yosh > 60 and yosh<=100:
    print("100% chegirma")
yosh2 = int(input("yoshingizni kiriting "))
if yosh2 <=18:
    print("kid")
elif yosh2 >18 :
    print("adult")
son1= int(input("yoshingizni kiriting "))
son2 = int(input("yoshingizni kiriting "))
result = son1-son2
if result :
    print(result)
else:
    print("son kiriting")