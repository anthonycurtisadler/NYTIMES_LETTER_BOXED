import os


about = """

             LETTER BOXED SOLVER
         by Anthony Curtis Adler 2019

    
     
     LETTER BOXED SOLVER FINDS SOLUTIONS
          TO THE 'LETTER BOXED'
     PUZZLE in THE NEW YORK TIMES.

          I'VE INCLUDED words.txt from:
      https://github.com/dwyl/english-words.

     THIS, HOWEVER, INCLUDES MANY
     WORDS THAT WILL NOT BE ACCEPTED
     BY THE NEW TIMES PUZZLE ENGINE.
     
     OTHER WORDS CAN BE USED. \n\n\n"""

print(about)

filename = 'words.txt'
# GET TEXT FILE 
while True:
     print('GETTING TEXT FILE!')
     try:
          textfile = open(filename,'r', encoding='utf-8')
          textfile=textfile.read()
          print(filename+' OPENED! \n')
          break
     except:
          print(textfile+' NOT FOUND\n')
          print('ENTER NEW WORD FILE!')
          filename= input('textfile')


# FIND THE CHARACTER DIVIDING THE WORDS
for x in textfile:
     if x not in 'abcdefghijklomnopqrstuvwxyz0123456789':
          split = x
          break

words = textfile.split(x)
print('NUMBER OF WORDS: '+str(len(words)))
sides = {}
validwords = {}
forming_chains = {}
starts_with = {}
print()

while True:
     try:
          number_of_sides = int(input('HOW MANY SIDES DOES THE LETTER BOXED HAVE?'))
          print()
          shortest_word = int(input('WHAT IS THE SHORTEST LENGTH OF A WORD?'))
          print()
          longest_chain = int(input('LONGEST CHAIN?'))
          print()
          number_to_find = int(input('NUMBER OF CHAINS TO FIND?'))
          break
     except:
          print('VALUES MUST BE INTEGERS!')

all_letters = ''
for side in range(0,number_of_sides):
     x = input('WHAT ARE THE LETTERS FOR SIDE '+str(side+1)+'?')
     sides[side] = x
     all_letters += x
print('THE TOTAL NUMBER OF LETTERS ARE '+str(len(all_letters)))
print('LETTERS: '+all_letters)



# initialize dictionaries for results
for z in range(0,10):
     forming_chains[z] = []

# initialize dictionary to sort by first letter 
starts_with = {}

for letter in all_letters:
     starts_with[letter] = []


# find all the valid words 

for word in words:

     newword = word
     for side in range(0,number_of_sides):
          for x in sides[side]:
               newword=newword.replace(x,str(side))
     newword_copy = newword

     for side in range(0,number_of_sides):
          newword_copy = newword_copy.replace(str(side),'')
     if not newword_copy:
          is_valid = True
          for side in range(0,number_of_sides):
               if str(side)*2 in newword:
                    is_valid = False
          if is_valid:
               if len(word)>shortest_word:
                    try:
                         starts_with[word[0]].append(word)
                    except:
                         pass


if input('DO YOU WANT TO SHOW THE VALID WORDS?') in ['yes','y','sure','ok']:
     
     for letter in starts_with:
          print()
          print()
          print('STARTING WITH :'+letter)
          print(', '.join(starts_with[letter]))

found_list = []

print('\n\n')

 
for z in range(0,longest_chain):

     print('CHECKING FI CHAIN of LENGTH '+str(z+1))
     if z == 0:

          for letter in all_letters:
               
               for word in starts_with[letter]:
               
                    all_letter_copy = all_letters
                    for x in word:
                         all_letter_copy = all_letter_copy.replace(x,'')
                    if not(all_letter_copy):
                         found_list.append('['+word+']')
                    else:
                         forming_chains[z].append('['+word+'/')
                              
     else:
          counter = 0
          for word in forming_chains[z-1]:

               for word2 in starts_with[word.replace('/','').replace('[','')[-1]]:

                    if word2 not in word:

                         combined_word = word+word2
               
                         all_letter_copy = all_letters
                         for x in combined_word.replace('/','').replace('[',''):
                              all_letter_copy = all_letter_copy.replace(x,'')
                         if not(all_letter_copy):
                              found_list.append(combined_word+']')
                         else:
                              forming_chains[z].append(combined_word+'/')
               counter+=1
               if counter % 1000 == 0:
                    print(counter,len(found_list))
               if len(found_list) > number_to_find:
                    break
                                                

print(str(len(found_list))+' VALID CHAINS HAVE BEEN FOUND!')
for counter, chain in enumerate(found_list):
     print(str(counter+1)+chain)

input('')
                    
          
          


          
               
          
          





          
          


