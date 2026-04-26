import sys
import time
	
def jalanin_Lirik() :
	lirik = [ 
				( "Don't be afraid to stand alone", 0.09), 
				( "Don't be afraid to stand outside your comfort zone", 0.09), 
				( "I know it's hard to work from home", 0.09), 
				( "And it ain't easy all alone", 0.1), 
				(" Relationships over the phone", 0.1), 
				( "Talking to your significant other all night long", 0.06),
				( "Sometimes it's hard to face reality", 0.09),
				("Oh... Oh..", 0.3),
				( "Even though you might get mad at 	me",0.09),
				("Oh.. Oh..", 0.3),
				("Sometimes it's hard to face reality", 0.1), 

]

	delay = [0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.04, 0.04, 0.04, 0.04, 0.3]
	print("\n == Hard To face reality ==") 
	time.sleep(0.1) 
	for i, (baris_lagu, delay_karacter) in enumerate(lirik):
		for karakter in baris_lagu:
			print(karakter, end='') 
			sys.stdout.flush() 
			time.sleep(delay_karacter) 
		time.sleep(delay[i]) 
		print(' ')
		
		
jalanin_Lirik()

print("\n// coding by Keymut + gemini dikit \\!!")