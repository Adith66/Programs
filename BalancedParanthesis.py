st=']]]'
stack=[]
for i in st:
    if stack==[] and (i==']' or i=='}' or i==')'):
        print('unbalanced')
        break
    if i=='[' or i=='{' or i=='(':
        stack.append(i)
        print(stack)
    if stack!=[] and (i==']' or i=='}' or i==')'):
        if (stack[-1]=='[' and i==']') or(stack[-1]=='{' and i=='}') or (stack[-1]=='('and  i==')'):
            stack.pop()
            print(stack)
        else:
            print('unbalanced')
            break
else:
    if stack==[]:
        print('balanced')
    else:
        print('unbalanced')
