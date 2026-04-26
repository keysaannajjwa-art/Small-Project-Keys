#jika no 1 dan 2 lebih besar
#maka nomor 3 false
#jika no 3 lebih besar, nomor
#1 dijumlahkan dan hasilnya True
number1 = int(input("mazukkan nomor 1"))
number2 = int(input("masukkan nomor2"))
number3 = int(input("masukkan nomor3"))
number4 = number1 + number2

Largest_number = number1
Largest_number = number2
Largest_number3 = number3
Largest_number12 = number4

if number1 > Largest_number3:
    Largest_number = number4
if number2 > Largest_number3:
    Largest_number = number4
    
#jadi otomatis ngambil number 4 yang dimana 
#penjumlahan antara number 1+2
#kalo semua largest number nanti yang 3 bakalan ikut dianggap largest number jadi di 
#bedakan saja biar pythonnya ga bingung jugak

if number3 > Largest_number:
    Largest_number = number3
print("the lager number is" , Largest_number)
#outputnya akan tetap meng out kan Largest_number sesuai ketetuan input diatas,kalo semunya var  largest number var seperti 3 (largest_number3) akan otomatis dianggap juga dan mempengaruhi hasil dari number1 dan number2 yang dimana mereka adalah largest_number juga makanya d bedakan.
