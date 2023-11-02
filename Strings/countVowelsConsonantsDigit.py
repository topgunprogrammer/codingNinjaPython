
s = "abcdefghijklmnopqrstuvwzyx1234567890!@#$%^ &*()-="
v = 0
c = 0
d = 0
z = 0
for x in s :
    if x.isalpha() :
        if x in ["a","e","i","o","u"] :
            v +=1
        else:
            c +=1
    elif x.isdigit() :
        d +=1
    else:
        z +=1

print(v,c,d,z)