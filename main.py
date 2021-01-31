from tkinter import *
import random

computer_guess = random.randint(1, 100)


def check():
    # get an integer value from user
    user_guess = int(guess_box.get())
    # To determine higher,lower or correct
    if user_guess < computer_guess:
        msg = 'Higher!'
    elif user_guess > computer_guess:
        msg = 'Lower!'
    elif user_guess == computer_guess:
        msg = 'Correct!'
    else:
        msg = 'Something went wrong..'

    # show the result
    lbl_result['text'] = msg

    # clear text guess
    # delete(int start_point, int end_point)
    # start_point – beginning index and is included in the count.
    # end_point – ending index and is excluded from the count.
    guess_box.delete(0, 5)


def reset():
    # Declare a global variable
    # a global variable is defined outside the function,we can access it inside the function.
    global computer_guess
    # Get a random number
    computer_guess = random.randint(1, 100)
    # Change the lbl_result text
    lbl_result['text'] = 'Game Reset!Guess Again!'


# create a window
window = Tk()

# change root background color
window.configure(bg='white')

# create a title
window.title('Guess The Number')

# Change window size (Width x Height)
window.geometry('270x100')

# create widgets
# The pack() manager is a simple layout manager.It can be used to do simple layout tasks
lbl_title = Label(window, text='WELCOME TO GUESSING GAME!', bg='yellow')
lbl_title.pack()

lbl_result = Label(window, text='GOOD LUCK!', bg='pink')
lbl_result.pack()

btn_check = Button(window, text='Check', fg='blue', bg='white', command=check)
btn_check.pack(side='left')

btn_reset = Button(window, text='Reset', fg='green', bg='white', command=reset)
btn_reset.pack(side='right')

guess_box = Entry(window, width=3, fg='purple')
guess_box.pack()

# start the main events loop
# It allows that red x button to be present in the window
# if we don't mentioned this, window disappears in a secs after we run the output
window.mainloop()
# end or quit the main events loop
window.destroy()
