# quantity of alphabates in a word or sentence
user=input('enter your name : ')
i=0
v=''
while i<len(user):
    if user[i] not in v:
        v+=user[i]
        print(v)
        print(f'{user[i]} : {user.count(user[i])}')
    i+=1
    # boht hard boht hard