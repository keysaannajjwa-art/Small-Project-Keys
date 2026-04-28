banner = """
    "============================================================"
      SELAMAT DATANG
      Mari hitung pendapatan bersih Usaha mu disini!
    
      [!] INSTRUKSI:
      ● Hitung Dengan Akurat Dan aman
      ● Pastikan Tidak Memakai koma/titik
       (Contoh: 10000)
      ● ketik "Sudah selesai" Apabila Sudah selesai menghitung!!
    
      Terimakasih!
    "============================================================"
    """

print(banner)

while True :
	Harga_Jual_Bungkus = int(input("Masukkan Harga Jual Perbungkus:"))
	Harga_Modal_Bungkus = int(input("Masukkan Harga Modal:"))
	JumLah_Terjual = int(input("Masukkan Jumlah barang terjual:"))

	ToTal_Bersih = Harga_Jual_Bungkus - 			Harga_Modal_Bungkus
	Bersih_Ny = JumLah_Terjual*ToTal_Bersih
	print("""
    "------------------------------------------------------------"
      HASIL PERHITUNGAN:
      Rp""" , Bersih_Ny,"""
    
      " Ini total pendapatan bersih mu, semangat terus! "
    "------------------------------------------------------------"
    """)
  
	BerHenti = input("Apakah Kamu Sudah Selesai Menghitung?")
	if BerHenti == "Sudah selesai":
		print("Kamu Menyelesaikan Perhitungan, Silahkan kembali nanti!")
		exit()
	
	
#CONTOH INPUT

#Harga jual perbungkus = 5.000
#Harga modal nya = 4.000
#jumalah terjual 10 pcs
#5000-4000 = 1000 #keuntungan
#1000 x 10pcs = 10.000