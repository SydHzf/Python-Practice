# Sum of digit
digit=input('enter a psitive number having more than one digit: ').replace(' ','')
if int(digit)<10:
    print('"error,please write a positive no. having atleast 2 digits"')
else:
    total=0
    i=0
    while i<len(digit):
        total+=int(digit[i])
        i+=1
    print(f'total of each digit in your number is: {total}')