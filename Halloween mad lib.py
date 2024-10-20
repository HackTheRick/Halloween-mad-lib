
def mad_lib_game():
    """plays a mad lib game with the user."""



print('''Halloween mad libs
      
    
  /\   /\                          
 /  \-/  \ --------------_________
 [(,) (,)] Bl@ck c@t      _______[)
 >(__W__)< _________(    0)       []
 (M_)u(M_)-------{_________)       []
                                      
                                            Created by: HackTheRick 
      ''')

print('Welcome to Mad Libs!')

#user input
name = input('enter a name:')
adjective1 = input('Enter an adjective:')
adjective2 = input('Enter another adjective:')
noun4 = input('Enter another noun:')
noun1 = input('Enter a noun:')
noun2 = input('enter another noun:')
noun3 = input('enter another noun:')
animal = input('enter a animal:')
verb = input('enter a verb:')
food = input('enter a food:')

story = f'''
I was worried my Halloween was off to a bad start when a black {animal} 
crossed my path, but it turned out ok. My best friend {name} and
I went trick-or-treating the minute it started getting dark. 
I dressed as a {adjective1} {noun1} and my friend was a {adjective2} {noun2}. 
The first few houses gave out their traditional {noun3} 
instead of candy. When we reached the end of the block, my friend dared me
to ring the doorbell on the spooky house at the top of the hill. I tip-toed 
to the door and just when I was going to push the button (a) {noun4} answered
the door. I screamed tried to {verb} until I realized it was just a mask. 
The old lady behind the mask gave me {food} candy bars since she didn't have many visitor
'''
#print story
print('heres your mad libs story:')
print(story)


