# This program will take the user input, and try to find the label corresponding to the integer by finding the middle
# label, getting the value of the middle label with cget, then checking if the value equals the user
# input. It will repeat this until the value is found or not found. I've also found that if I search for the first number
# (top left) that I won't be able to find it even though it exists (unless there are two repeating numbers)
# because I'm unable to loop one more time. Unsure if this could be fixed with my code.

from tkinter import *
from tkinter import simpledialog
import math
import random

root = Tk()
root.title("Searching")
root.geometry("600x600")
numbers = []
labels_list = []

def label_creator():
  global numbers
  global labels_list

  #Randomizing the integers
  numbers = []
  for i in range(100):
    numbers.append(random.randint(1,300))
    numbers = sorted(numbers)

  #Creating the labels with the randomized integers
  labels_list = []
  for i in range(10):
    for j in range(10):
      x = Label(root, text = numbers.pop(0), background = "white", height = 2, width = 4, font = ("Roboto", 12))
      x.place(x = 50 + (50 * j), y = 50 + (i * 50))
      labels_list.append(x)

def searching():
  #Asking user what to search for
  usr_inp = simpledialog.askinteger("Input", "Please enter an integer", parent = root, minvalue = 1, maxvalue = 300)
  #Returns if no value
  if not usr_inp:
    return

  #Updating label and disabling buttons
  search_but.configure(state = DISABLED)
  reset_but.configure(state = DISABLED)
  search_lab.configure(text = "Integer: {}".format(usr_inp))
  candidate = labels_list

  def update_colors():
    #Updating colors
    for label in labels_list:
      label.configure(background = "white")
    for label in candidate:
      label.configure(background = "green")

  while True:
    #Find label in middle of list (rounding up) and get the value
    index_slice = math.ceil(len(candidate) / 2)
    mid_lab = candidate[index_slice]
    mid_val = mid_lab.cget("text")
    print(mid_val) #testing
    mid_lab.configure(background="yellow")
    root.update()
    root.after(250)

    #Split the list in half based on if the val is > or < the search value, if = then found
    if mid_val > usr_inp:
      candidate = candidate[:index_slice]
    elif mid_val < usr_inp:
      candidate = candidate[index_slice:]
    elif mid_val == usr_inp:
      candidate = [mid_lab]
      update_colors()
      #Updating label and enabling buttons
      search_lab.configure(text="Found {}!".format(usr_inp))
      search_but.configure(state = NORMAL)
      reset_but.configure(state = NORMAL)
      break

    #If <=1, couldn't find number in list
    print(len(candidate)) #test
    if len(candidate) <= 1:
      for x in labels_list:
        x.configure(background="red")
      #Updating label and enabling buttons
      search_lab.configure(text="Did not find {}.".format(usr_inp))
      search_but.configure(state=NORMAL)
      reset_but.configure(state=NORMAL)
      break

    update_colors()
    root.update()
    root.after(250)

#Creating the buttons
search_but = Button(root, text = "Search", command = searching)
search_but.place(x = 50, y = 550)
search_lab = Label(root, text = "...", font = ("Roboto", 12))
search_lab.place(x = 150, y = 550)
reset_but = Button(root, text = "Reset", command = label_creator)
reset_but.place(x = 100, y = 550)

label_creator()
root.mainloop()