Blacklist_User = ["Bahlil", "Bjorka", "Rehan", "Dimas", "Tono", "Wawan"]
InpUt_Nam = input("siapa namamu\nama lengkap,\ndan pastikan tidak TERDAFTAR BLACKLIST.")

if InpUt_Nam in Blacklist_User:
	print(Blacklist_User, InpUt_Nam, "××\nADA DI BLACKLIST DILARANG MASUK")
	exit()
	
Input_Um = int(input("Berapa umur mu?"))

if Input_Um <18:
	print("Dibawah Umur, Dilarang Masuk!")
	exit()

if InpUt_Nam != Blacklist_User:
		print("buat password yuk!") 
		print("""×××  KETENTUAN MEMBUAT PASSWORD ×××\ntidak boleh memakai\n××× NAMA SENDIRI ×××\nHarus berupa\n☆☆ 8 KARAKTER ☆☆
	""") 

Pasw_1 = input("masukkan passwordnya!")

while len(Pasw_1) <8 and Pasw_1 != InpUt_Nam:
			print("INVALID 8 KARAKTER")
			Pasw_1 = input("Masukkan Password lagi,")
if Pasw_1 == InpUt_Nam:
	print("INVALID SAMA DENGAN NAMA!")

if len(Pasw_1) >8 and Pasw_1 != InpUt_Nam:
			print("password mu direverse untuk keamaanan ●\nini dia password mu", Pasw_1[::-1]) 
			
Id_Unic = InpUt_Nam[0:5]
Valid_Pw = Pasw_1[::-1]
			
if InpUt_Nam not in Blacklist_User and Input_Um >= 18 and Pasw_1 != InpUt_Nam:
	 print("☆ AKUN MU ☆  ✨ TERDAFTAR ✨\nDENGAN ID UNIC,", "@", Id_Unic, "@",
	 "PASSWORD VALID", "~" ,Valid_Pw, "~",)
	 
#Input Nama: User input nama.
#​Syarat: Nama GAK BOLEH ada di list Blacklist_User.
#​Proses: Ambil 3 huruf pertama dari namanya pake Slicing buat dijadiin kode ID unik.
#​Input Password: User bikin password.
#​Syarat 1: Panjang password harus lebih dari 8 karakter (Pake len(password)).
#​Syarat 2: Password GAK BOLEH sama dengan nama user.
#​Input Umur: Pake variabel Batas_Umur = 18.
#​Syarat: Harus di atas atau sama dengan 18.
#​Final Logic (Gunakan and, or, dan not sekaligus):
#​User cuma bisa "Terdaftar" kalau: (Umur cukup AND Password valid) AND NOT (Nama ada di Blacklist).	 
     
