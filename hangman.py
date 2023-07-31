import random 
word_list = ['ardvark', 'baboon', 'camel', 'love', 'happy']
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)

while '_' in display:
  guess = input('Choose letter: ').lower()
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)

if '_' not in display:
    print('You Win!')
  



  
