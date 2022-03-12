# Use , (comma) for getting the answer. Press , again after the completion of the answer to avoid getting an error.
import sys
from msvcrt import getch
default = 'Please answer my question' #length of ans should not be greater than default
answer = ''
i = 100
print('Press ENTER key to submit your petition and your question.')
print('Hint >> Write \'Please answer my question\' in petition column')
print('Enter Your Petition Here: ', end='')
#"flush" the buffer, meaning that it will write everything in the buffer to the terminal,
# even if normally it would wait before doing so
sys.stdout.flush()
while 1:
    #read the keypress and return the resulting character as bytestring
    x = getch()
    # For backspace key. This works even when you are writing the answer in the petition column.
    if ord(x) == 8:
        print('\b \b', end='')
        sys.stdout.flush()
        i -= 1

    # For enter key
    elif ord(x) == 13:
        break

    elif x.decode() != '.':
        print(x.decode(), end='')
        sys.stdout.flush()
        i += 1

    # For storing the answer
    elif x.decode() == '.':
        while x.decode() == '.':
            y = getch()
            print(default[i-1], end='')
            sys.stdout.flush()
            i += 1
            if y.decode() == '.':
                break
            else:
                answer = answer + y.decode()
print('')

b = input('Ask Your Question: ')
print('\nThe Answer to Your Question Is: ', answer.title())