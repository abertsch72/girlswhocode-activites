# Annie Gao
# 10/5/2019

'''Welcome to: You can't have your cake and eat it, too!

Let's say Eliza is fill one bucket full of fruits. This bucket 
can only hold one type of fruit. Eliza loves oranges, but we 
can offer other suggestions. We have the statement below:'''

fruit = input('What type of fruit does Eliza pick (only put ' +
              'singular fruit names)? ')
if (fruit == 'orange'):
  print('Eliza agrees with you, and filled her bucket with oranges.')
elif (fruit == 'strawberry'):
 print('Eliza is okay with strawberries, so she reluctantly fills her bucket ' +
        'with them.')
else:
  print('Eliza disagrees with you, and filled her bucket with oranges.')
  

'''What is the error above? Look closely at each indent.'''

# Why is this comment green? Why are the other comments red? 
# Tell a facilitator what you think!

'''More conditional debugging below:'''

fav_color = input('Enter your favorite color! ')

if (fav_color == 'blue'):
  print('My favorite color is blue, too!')
if (fav_color == 'blue'):
    print('Blue is a weird color. I like pink more!')
else if (fav_color == 'red'):
  print('What's the meaning of red?')
  

  
  
  
  
  
