PoIn = 5


print("""======================================
               🎮 GAME TEBAK KATA SEPUTAR TKJ 🎮")
            ======================================= 
""")
print(" CLUE KATA:")
print(" 1. C****E   5. P*")
print(" 2. R*****R  6. C*U")
print(" 3. S*****H  7. S*****T")
print(" 4. C****D   8. C*****S")
print("----------------------------------------")
print(" ATURAN: POIN 10 buat lo MENANG!")
print(" Poin awal lu:", PoIn)
print("========================================")



Daftar_Kata = ["CABEL","ROUTER","SWITCH","CLOUD","PC","CPU", "STRAIGHT","CROSS"]


for Kata in Daftar_Kata:
	while PoIn >1:
		Tny_KTa = input(f" apa kata lo? ") 
		if Tny_KTa != Kata:
			PoIn-=1
			print("SALAH! poin lu sekarang", PoIn)
		if Tny_KTa == Kata:
			PoIn+=1
			print("EXACTLY!")
			print("poin lu sekarang", PoIn, "Gas lanjot")
			break

		if PoIn == 1:
	            print("""
      
         
         GAME OVER - POIN LU HABIS!❌                 
                  YHAHAHA TETAP SEMANGAT                     
                                                                 
""")


	
	if PoIn == 10:
	                  print("""======================================
                   CONGRATS! POIN LO 10
                                   LU MENANG ! 🏆
            =======================================
""")

		
			
		



		
#selalu menggunakan inputan yg sama kalo keluarnya mau sama 
	