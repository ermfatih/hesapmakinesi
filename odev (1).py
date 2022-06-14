def topla(num1,num2):
    return num1+num2
def cikar(num1,num2):
    return num1-num2
def carp(num1,num2):
    return num1*num2
def bol(num1,num2):
    return num1/num2

listele={
    "Topla":1,
    "Çıkar":2,
    "Çarp":3,
    "Böl":4
}

islemAl=int(input("İstediğiniz İşlemin Numarasını Giriniz (1-4)..."))
num1=int(input("İslem için ilk sayıyı giriniz..."))
num2=int(input("İşlem için ikinci sayıyı giriniz..."))

if(islemAl==1):
    print(topla(num1,num2))
elif(islemAl==2):
    print(cikar(num1-num2))
elif(islemAl==3):
    print(carp(num1,num2))
elif(islemAl==4):
    print(bol(num1,num2))
else:
    print("Lütfen geçerli değer giriniz(1-4)...")
