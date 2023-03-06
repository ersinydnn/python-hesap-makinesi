def toplama(): #toplama fonksiyonunu tanımlıyoruz
 sonuc=sayi1+sayi2
 print(sonuc)
def cikarma(): #çıkarma fonksiyonunu tanımlıyoruz
    sonuc=sayi1-sayi2
    print(sonuc)
def carpma():
    sonuc=sayi1*sayi2 #çarpma fonksiyonunu tanımlıyoruz
    print(sonuc) 
def bolme():
    sonuc=sayi1/sayi2 #bölme fonksiyonunu tanımlıyoruz
    print(sonuc)     

print("hosgeldiniz!lutfen hesaplamak istediginiz sayilari giriniz.")
sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))
while True:
 islem=input("1-toplama\n2-cikarma\n3-carpma\n4-bolme\n")
 if islem=="1":
    toplama()
    break
 elif islem=="2":
    cikarma()
    break
 elif islem=="3":
    carpma()
    break
 elif islem=="4":
    bolme()
    break
 else:
    break

     
   
    
 