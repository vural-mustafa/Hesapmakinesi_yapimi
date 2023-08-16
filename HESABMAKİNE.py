def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y != 0:
        return x / y
    else:
        return "Bölme işlemi için sıfıra bölünemez!"

while True:
    print("İşlem seçenekleri:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçiniz (1/2/3/4/5): ")

    if secim == '5':
        print("Hesap makinesi kapatılıyor...")
        break

    sayi1 = float(input("Birinci sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    if secim == '1':
        print("Sonuç:", topla(sayi1, sayi2))
    elif secim == '2':
        print("Sonuç:", cikar(sayi1, sayi2))
    elif secim == '3':
        print("Sonuç:", carp(sayi1, sayi2))
    elif secim == '4':
        print("Sonuç:", bol(sayi1, sayi2))
    else:
        print("Geçersiz bir seçenek girdiniz.")
