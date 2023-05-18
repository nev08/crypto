q=int(input("Enter the prime number(q): "))
alpha=int(input("Enter the primitive root(alpha): "))
XA=int(input("Enter private key of party1(XA): "))
XB=int(input("Enter private key of party2(XB): "))
YA=(alpha**XA)%q
print ("Public key of party1(YA): ",YA)
YB=(alpha**XB)%q
print ("Public key of party2(YB): ",YB)
K1=(YB**XA)%q
print ("Common Secret key calculated by party1(K1): ",K1)
K2=(YA**XB)%q
print ("Common Secret key calculated by party2(K2): ",K2)
if K1==K2:
   print("Key Exchange Successful")
else:
   print("Data invalid")
