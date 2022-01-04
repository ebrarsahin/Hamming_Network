# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:48:36 2021

@author: shneb
"""

import numpy as np
'''
Güneşe Yakınlık     Uydu Durumu     Güneş Etrafında Dönüş Hızı     Boyut

uzak [-1,-1]        yok [-1,-1]      yavaş[-1,-1]                 küçük[-1,-1]
orta [1,-1]         az [-1,1]        orta[-1,1]                 orta[1,-1]
yakın [1,1]         çok  [ 1,1]      hızlı[1,1]                  büyük[1,1]

'''

#gezegenler -->
merkur=np.array([[1,1,-1,-1,1,1,-1,-1]])
venus=np.array([[1,1,-1,-1,1,1,1,-1]])
dunya=np.array([[1,-1,-1,1,-1,1,1,-1]])
mars=np.array([[1,-1,-1,1,-1,1,-1,-1]])
jupiter=np.array([[1,-1,1,1,-1,-1,1,1]])
saturn=np.array([[-1,-1,1,1,-1,-1,1,1]])
uranus=np.array([[-1,-1,1,1,-1,-1,1,-1]])
#giriş
input_=np.array([[1,0,1,1,-1,-1,1,1]])
threshold=-4 #n/2 -->n=8
weight=np.array([[1,1,1,1,1,-1,-1,
                  1,1,-1,-1,-1,-1,-1,
                  -1,-1,-1,-1,1,1,1,
                  -1,-1,1,1,1,1,1,
                  1,1,-1,-1,-1,-1,-1,
                  1,1,1,1,-1,-1,-1,
                  -1,1,1,-1,1,1,1,
                  -1,-1,-1,-1,1,1,-1]])
weight=weight*0.5
y=(np.dot(input_.reshape(1,8),weight.reshape(8,7))) + threshold

max_index=np.argmax(y)


if max_index==0:
    print("Giriş -->",input_)
    print("Merkur  -->",merkur)
    print(y[0][0]," Hamming uzaklığında Merkür özelliklerini taşımaktadır.")
    
elif max_index==1:
    print("Giriş -->",input_)
    print("Venüs  -->",venus)
    print(y[0][1]," Hamming uzaklığında Venüs özelliklerini taşımaktadır.")
    
elif max_index==2:
    print("Giriş -->",input_)
    print("Dünya  -->",dunya)
    print(y[0][2],"Hamming uzaklığında Dünya özelliklerini taşımaktadır.")
    
elif max_index==3:
    print("Giriş -->",input_)
    print("Mars  -->",mars)
    print(y[0][3]," Hamming uzaklığında  Mars özelliklerini taşımaktadır.")
    
elif max_index==4:
    print("Giriş -->",input_)
    print("Jüpiter  -->",jupiter)
    print(y[0][4],"Hamming uzaklığında jüpiter özelliklerini taşımaktadır.")

elif max_index==5:
    print("Giriş -->",input_)
    print("Satürn  -->",saturn)
    print(y[0][5],"Hamming uzaklığında Satürn özelliklerini taşımaktadır.")
    
elif max_index==6:
    print("Giriş -->",input_)
    print("Uranüs  -->",uranus)
    print(y[0][6],"Hamming uzaklığında Uranüs özelliklerini taşımaktadır.")
  
else:
    print("HATA !")
