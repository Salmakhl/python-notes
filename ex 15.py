a=float(input("enter the first note: "))
while a<0 or a>20:
    a=float(input("please re-enter the note: "))
b=float(input("enter the second note: "))
while b<0 or b>20:
    b=float(input("please re-enter the note: "))
c=float(input("enter the third note: "))
while c<0 or c>20:
    c=float(input("please re-enter the note: "))
d=(a+b+c)/3
s=str
if d>=16 :
    print("your note:",d,"very good")
elif d<16 and d>=14:
    print("your note:",d,"good")
elif d<14 and d>=12:
    print("your note:",d,"quite-good")
elif d<12 and d>=10:
    print("your note:",d,"passable")
else :
    s=="insufficient"



