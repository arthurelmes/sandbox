"""This is a hello world program.
Author: Arthur Elmes
2020-08-08"""
#Goof Troop
Goof_Troop = ["Pete", "Josh", "Arthur", "Bily"]

#Wake Up
print('Hello, World!')
name = input('May I ask who woke me up this morning?:')


#print(name)

if 'Pete' in name:
    print('Guten Morgen Pete')
elif 'Josh' in name:
    print('Oh, hi Josh!')
elif 'Arthur' in name:
    print('Good morning Captain!')
elif 'Bily' in name:
    print('Good morning Mr. Astronaut')
else:
    print('Hello? Anybody?')


