print('===================')
print('Rock Paper Scissors Lizard Spock')
print('===================')


print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')

player = int(input('Select A Number (1-5):  '))

if player == 1:
  print('You chose: ✊')

elif player == 2:
  print('You chose: ✋')

elif player == 3:
  print('You chose: ✌️')

elif player == 4:
  print('You chose: 🦎')

elif player == 5:
  print('You chose: 🖖')
  
else:
  print('Wrong input')

import random

num = random.randint(1,5)

if num == 1:
  print('CPU chose: ✊')

elif num == 2:
  print('CPU chose: ✋')

elif num == 3:
  print('CPU chose: ✌️')

elif num == 4:
  print('CPU chose: 🦎')

else:
  print('CPU chose: 🖖')

if player == 1 and num == 2:
  print('The player lost!')

elif player == 2 and num == 3:
  print('The player lost!')

elif player == 3 and num == 1:
  print('The player lost!')

elif player == 4 and num == 1:
  print('The player lost!')

elif player == 5 and num == 4: 
  print('The player lost!')

elif player == 3 and num == 5: 
  print('The player lost!')

elif player == 4 and num == 3: 
  print('The player lost!')

elif player == 2 and num == 4: 
  print('The player lost!')

elif player == 5 and num == 2: 
  print('The player lost!')

elif player == 1 and num == 5: 
  print('The player lost!')

elif player == 1 and num == 3:
  print('The player won!')

elif player == 2 and num == 1:
  print('The player won!')

elif player == 3 and num == 2:
  print('The player won!')

elif player == 1 and num == 4:
  print('The player won!')

elif player == 4 and num == 5:
  print('The player won!')

elif player == 5 and num == 3:
  print('The player won!')

elif player == 3 and num == 4:
  print('The player won!')

elif player == 4 and num == 2:
  print('The player won!')

elif player == 2 and num == 5:
  print('The player won!')

elif player == 5 and num == 1:
  print('The player won!')
  
elif player == 1 and num == 1:
  print('Its a tie!')

elif player == 2 and num == 2:
  print('Its a tie!')

elif player == 3 and num == 3:
  print('Its a tie!')

elif player == 4 and num == 4:
  print('Its a tie!')

else:
  print('Its a tie!')