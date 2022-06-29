import turtle
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tools.constanta import *
from tools.fungsi_simulasi import *


#Insialisasi Posisi Awal Setiap mobil
beda = 30
for a in range(N):
    x0.append(-500 + beda)
    beda += 30
x0.sort()

#membuat objek turtle
turtle.color('black')
style = ('Calibri', 15, 'normal')
turtle.write('                 Simulasi Pergerakan Mobil\n======================================', font=style, align='center')
turtle.bgcolor("white")
turtle.Screen().setup(1000,400,0,0)
turtle.Screen().delay(1)

#membuat mobil
for j in range(N) :
    arr_mobil.append(turtle.Turtle())

#Set posisi mobil
for i in range (N) :
    arr_mobil[i].color(warna[i])
    arr_mobil[i].penup()
    arr_mobil[i].goto(x0[i],-30)

#Mulai Simulasi
kepadatan = [0]*(tmax+1)
while t <= tmax:
    inx = [0]*20
    for mobil in range(N):

       
        arr_mobil[mobil].forward(update_kecepatan(mobil))
        arr_mobil[mobil].speed(N)
        

        #Mobil berputar kembali ke titik awal
        if (arr_mobil[mobil].xcor() >= 500):
            arr_mobil[mobil].ht()
            arr_mobil[mobil].goto(-500,-30)
            arr_mobil[mobil].st()
            
        #menghitung waktu mobil melewati posisi semula
        if (x0[mobil] >= arr_mobil[mobil].xcor()):
            if (0 <= x0[mobil] - arr_mobil[mobil].xcor() <= 50):
                t_kembali[mobil] += t
                total_putaran[mobil] += 1

        #menghitung kepadatan pada selang x80 dan x 90
        if ((350) <= arr_mobil[mobil].xcor() <= ((450))):
            kepadatan[t]+=1

        #menghitung kepadatan maksimum per satuan waktu tiap 5 unit posisi & menentukan posisi kendaraan pada interval
        if ((-500) <= arr_mobil[mobil].xcor() < (-450)): # Interval x1 - x5
            inx[0]+=1
        elif((-450) <= arr_mobil[mobil].xcor() < (-400)): # Interval x5 - x10
            inx[1]+=1
        elif((-400) <= arr_mobil[mobil].xcor() < (-350)): # Interval x11 - X15
            inx[2]+=1
        elif((-350) <= arr_mobil[mobil].xcor() < (-300)):  # Interval x16 - X20
            inx[3]+=1
        elif((-300) <= arr_mobil[mobil].xcor() < (-250)):  # Interval x21 - X25
            inx[4]+=1
        elif((-250) <= arr_mobil[mobil].xcor() < (-200)):  # Interval x26 - X30
            inx[5]+=1
        elif((-200) <= arr_mobil[mobil].xcor() < (-150)):  # Interval x31 - X35
            inx[6]+=1
        elif((-150) <= arr_mobil[mobil].xcor() < (-100)):  # Interval x36 - X40
            inx[7]+=1
        elif((-100) <= arr_mobil[mobil].xcor() < (-50)):  # Interval x41 - X45
            inx[8]+=1
        elif((-50) <= arr_mobil[mobil].xcor() < (0)):  # Interval x46 - X50
            inx[9]+=1
        elif((0) <= arr_mobil[mobil].xcor() < (50)):  # Interval x51 - X55
            inx[10]+=1
        elif((50) <= arr_mobil[mobil].xcor() < (100)): # Interval x56 - X60
            inx[11]+=1
        elif((100) <= arr_mobil[mobil].xcor() < (150)):  # Interval x61 - X65
            inx[12]+=1
        elif((150) <= arr_mobil[mobil].xcor() < (200)):  # Interval x66 - X70
            inx[13]+=1
        elif((200) <= arr_mobil[mobil].xcor() < (250)):  # Interval x71 - X75
            inx[14]+=1
        elif((250) <= arr_mobil[mobil].xcor() < (300)):  # Interval x76 - X80
            inx[15]+=1
        elif((300) <= arr_mobil[mobil].xcor() < (350)):  # Interval x81 - X85
            inx[16]+=1
        elif((350) <= arr_mobil[mobil].xcor() < (400)): # Interval x86 - X90
            inx[17]+=1
        elif((400) <= arr_mobil[mobil].xcor() < (450)):  # Interval x91 - X95
            inx[18]+=1
        elif((450) <= arr_mobil[mobil].xcor() < (500)):  # Interval x96 - X100
            inx[19]+=1
        
    for index in range(len(interval)):
        if(interval[index] < inx[index]):
            interval[index] = inx[index]

    t+=1


print("\n")
# Kepadatan setiap pada selang x80 dan x 90
plt.plot(range(tmax+1), kepadatan)
plt.xlim([])
plt.title('Kepadatan Mobil')
plt.xlabel('iterasi')
plt.ylabel('Banyak Mobil')
plt.figure(num=0, dpi=120)
plt.show
print("\n")

# Kepadatan maksimum per satuan waktu tiap 5 unit posisi
plt.plot(range(1,M,5), interval)
plt.title('Kepadatan Maksimum Tiap 5 unit Posisi')
plt.xlabel('Iterasi')
plt.ylabel('Total Kepadatan')
plt.figure(num=0, dpi=120)
plt.show
print("\n") 


print("Waktu rata-rata mobil kembali ke posisi awal:")  
for x in range(N):
    print('Rata - rata waktu mobil ',x,' adalah ',t_kembali[i]/total_putaran[x], 'satuan waktu')
