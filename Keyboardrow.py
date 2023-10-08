import sys
s='asvd'
arr=['zxcvbnm','asdfghjkl','qwertyuiop']
for j in arr:
    for i in range(len(s)):
        if i!=len(s)-1:
            if s[i] in j and s[i+1] not in j:
                print(False)
                sys.exit()
else:
    print(True)
