opilane = "eveli"
if opilane == "Mariin":
   print "Eksam:5"
elif opilane == "Timo":
   print "Eksam:4"
else:
   print "Eksam:3"
   
x=0
while x<10:
   print "x=" +str(x)
   x=x+1
print "valmis. x=" +str(x)

massiiv = ["a", "b", "c"]
for element in massiiv:
	print element

massiiv = ["a", "b", "c"]
for element in massiiv:
	if element == "b":
		continue
	print element
	if element == "c":
		break
print "valmis"

x=0
while x<9:
	x=x+1
	x=str(x)
	print ((x).zfill(2))
	x=int(x)

	
