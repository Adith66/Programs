s1='ram'
s2='garm'
if len(s1)!=len(s2):
    print(False)
else:
    for i in s1:
        if i not in s2:
            print(False)
            break
    else:
        print(True)
