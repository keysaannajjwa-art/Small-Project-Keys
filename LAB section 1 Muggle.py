#jika nomor yang di input user berbeda dengan secret number , print "Ha ha ! You're stuck in my loop" dan ada inputan lagi, 
#jika nomor yang di input user sama dengan secret number ptint " Well done, muggle You are free now"

SeCret_Num = 1110
print( 
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


Number_inpUt = int(input())

while Number_inpUt != SeCret_Num:
	print ("Ha ha ! You stuck in my loop")
	Number_inpUt = int(input("try again"))
print("Well done muggle! You free now")

