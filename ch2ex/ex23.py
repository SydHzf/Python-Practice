username,character=input('user name and write a letter from user name split by comma:').split(',')
print(f'length of username is {len( username.replace(' ','') )}')
print(f'no. of given character from user name {username.lower().strip().count(character.lower().strip())}')
