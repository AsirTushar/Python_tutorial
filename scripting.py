'''
Three quotations begins/ends a multi-line comment to be used for documenation 
(also known as a doc string).
Include one of these at the beginning of every py file to give a brief description
of what the code contains, who wrote it, etc. Also include one of these at the 
beginning of every function definition to explain what the function does.

This script shows some very basic parts of Python. Run it using the command
"python basics.py" in a terminal.

Created on Tues Jun 4 2019

Author: Christopher Strickland
Email: cstric12@utk.edu
'''

# This is a single line comment. Use it very often.
# You will save yourself untold amounts of grief if you remember these words:
#   "We write code to be read by humans, not machines."

# Place all imports at the top of your script. Import only the stuff you need.

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng # you can import specific things



# Here are some more examples of flow control, using a while loop and if/elif/else.
done_flag = False
while not done_flag:
    your_number_txt = input('Input an even number greater than 6: ') # get some user input
    # input returns a string. turn it into an integer
    your_number = int(your_number_txt)
    if your_number > 6 and your_number % 2 == 0: # % is the modulus operator
        print('Happy land!')
        done_flag = True # this will cause us to break out of the while loop
        # could also have done a "while True" loop, and used "break" to break out
    elif your_number > 6 and not your_number % 2 == 0:
        print('The number {} is not even.'.format(your_number))
    else:
        # Note that to get the word It's, I use double quotations around the string
        print("{} is a silly number. It's just not large enough!".format(your_number))



# Now let's do an example where we plot something based on user input
print('Plotting B + Asin(wt).')
B = float(input('B: '))
A = float(input('A: '))
w = float(input('w: '))

xmesh = np.linspace(-10,10,200) # Use linspace to quickly get an evenly spaced
                                 #   mesh of values.
ymesh = B + A*np.sin(xmesh) # All happens elementwise on the array xmesh

plt.plot(xmesh,ymesh,label='sine')
plt.legend() # Create a legend using the label entered in the plot command
plt.title('Plot of sine')
plt.xlabel('t')
plt.show() # This must be there to show the plot and stop the program while
           #    you examine it.
