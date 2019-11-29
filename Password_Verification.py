password = input("provide your password")
calp=0
csalp=0
cn=0
cspl=0
alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
salp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
spl=['_','@','$']
n=['0','1','2','3','4','5','6','7','8','9']
capflag=1
smaflag=1
numberflag=1
spflag=1
for i in password:
    if i in alp and capflag==1:
        calp=calp+25
        capfalg=0
    elif i in spl and spflag==1:
        cspl=cspl+25
        spflag=0
    elif i in salp and smaflag==1:
        csalp=csalp+25
        smaflag=0
    elif i in n and numberflag==1:
        cn=cn+25
        numberflag=0
score=csalp+calp+cn+cspl
print("strength score ",score)
