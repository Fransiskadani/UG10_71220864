print ("~~~~~~~~~~~~~~ /('V')\ ~~~~~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~~~~~ /('V')\ ~~~~~~~~~~~~~~")
print ("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya: ")
print ("1. Limas")
print ("2. Bola")
print ("3. Prisma")
print ("4. Kerucut")
a = int(input("Masukkan pilihan Anda: "))
if a == 1:
    x = int(input("Masukkan panjang sisi alas limas: "))
    y = int(input("Masukkan tinggi limas: "))
    limas = (1/3*x**y)
    print ("Volume limas tersebut adalah",limas)
elif a == 2:
    r = int(input("Massukan panjang jari-jari bola: "))
    bola = ((4/3) * 3.14 * r * r *r)
    print = int(input("Volume bola tersebut adalah ",bola))
elif a == 4:
    R = int(input("Masukkan jari-jari kerucut"))
    T = int(input("Masukkan tinggi kerucut"))
    kerucut = (1/3*(3.14)*R*R*T)
    print = int(input("Volume kerucut tersebut adalah ",kerucut))