def toplama(sy_1, sy_2):
    return sy_1 + sy_2
def çıkarma(sy_1, sy_2):
    return sy_1 - sy_2
def çarpma(sy_1, sy_2):
    return sy_1 * sy_2
def bölme(sy_1, sy_2):
    return sy_1 / sy_2

sayı_1 = int(input("ilk sayıyı giriniz\n"))
sayı_2 = int(input("ikinci sayıyı giriniz\n"))
işlemler = {
    "+": toplama,
    "-": çıkarma,
    "*": çarpma,
    "/": bölme
}
for x in işlemler:
    print (x)
yapılacak_sembol = input("yapılacak işlem nedir \n")
yapılcak_işlemin_fonksiyonu = işlemler[yapılacak_sembol]
cevap = yapılcak_işlemin_fonksiyonu(sayı_1, sayı_2)
print (f"{sayı_1} {yapılacak_sembol} {sayı_2} = {cevap}")
