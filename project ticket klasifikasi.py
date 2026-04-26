#​Alur: Program nanya Nama, Umur, dan apakah punya Tiket (True/False).
#​Logika:
#​Pake and buat ngecek: Kalau umur di atas 18 DAN punya tiket, boleh masuk.
#​Pake or buat pengecualian: Kalau dia nggak punya tiket TAPI namanya ada di list_tamu_vips, dia tetep boleh masuk.
#​Tantangan: Pake Slicing buat nampilin cuma 3 nama pertama dari daftar antrean tamu di layar.

print("""╔═════════════════════════════════════════════╗
║         🎟️  VIP CONCERT GATE SYSTEM  🎟️   ║
║      ✨ Powered by keysa  ✨           
╚═════════════════════════════════════════════╝""")

print("""╔═════════════════════════════════════════════╗
║         🎟️  Pastikan Kamu berumur 18+ dan       ||         memiliki Ticket Yang masih aktif [opsi1] 
║
║      ✨ Jika kamu Masuk List Vip [opsi2]   ✨        
╚═════════════════════════════════════════════╝""")

Tny_Nama = input("siapa nama kamu?")
Tny_Opzsi = input("kamu memakai opsi yang mana?")
Tny_Umur = int(input("umur kamu berapa?"))

if Tny_Umur <18:
	print("kamu dibawah umur, dilarang masuk")
	exit()

elif Tny_Opzsi == "opsi 1" :
	print("baiklah kamu boleh masuk")
	exit()


elif Tny_Opzsi == "opsi 2":
	print("biar kita cek dulu nama mu ya..")
	print("█▒▒▒▒▒▒▒▒▒ 10%")
	print("██████████ 100%")
	Pabrik_Tamu_vips = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jinbe"]
	Pabrik_Slice = Pabrik_Tamu_vips[:5]
	print(Pabrik_Slice)

if Tny_Nama in Pabrik_Tamu_vips:
	print(Tny_Nama, "☆☆☆")
else: print(Tny_Nama, "#%#^@^")

if Tny_Nama in Pabrik_Tamu_vips:
	print("baiklah nama mu ada silahkan mazuk")
else: print("nama mu gaada, dilarang masuk")
