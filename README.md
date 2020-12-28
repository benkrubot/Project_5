# Create a collection of 100 int values,
I used a for loop to append to my numbers list the 100 integers using the random module. After that I used the sorted function to sort the numbers list.

![alt text](https://i.imgur.com/IBLvRBn.png)

# Create a GUI to display the collection of int values as rectangles,
To display my collection of int values as rectangles, I used a for loop in a for loop to create a 10x10 grid that creates the rectangles using labels, and by using the pop method I am able to take the first value out of the numbers list and place that as the text on the label. This loops until all 100 rectangles are created.

![alt text](https://i.imgur.com/pKankoH.png)

# Include a text box in your GUI to allow a user to enter a value to search for,
I used simpledialog to ask the user for an integer.

![alt text](https://i.imgur.com/2FHGQML.png)

# Include a button to start the search process,
I created a button that when pressed will call the searching function.

![alt text](https://i.imgur.com/LYG5fpT.png)

# Highlight the candidate value at each step of the searching process,
In my while True section, I take the length of the candidate (contains all of the labels) and I divide by 2 and store into index_slice. I store the candidate[index_slice] into mid_lab and then I use cget to get the text or int value at that label, which I then store into mid_val. Then I change the label background of mid_lab which highlights the candidate label yellow.

![alt text](https://i.imgur.com/Oq7CL0R.png)

# Pause after highlighting the candidate value but before moving on,
Here I just used root.after(250) to slightly pause after the highlighting process. Can be seen in above photo.

# Make it obvious when it has either found the value it is searching for or knows that the value is not in the data set. (perhaps the candidate is turned yellow, the non-matches are turned to red, and matches are turned to green?)
I have a label that updates when the value is found or not found, but I also have a section where if the mid_val == usr_inp then the candidate = [mid_lab] which essentially gets rid of the other candidate green labels and only highlights the correct label green. I also have a section where if the length of candidate is <= 1, then it will run a for loop in the range of labels_list to turn all of the labels red indicating the search could not find the value. 

![alt text](https://i.imgur.com/N21HK9I.png)

# What kinds of tests would be useful for this?  How could we test some of it to verify that it was working properly?
I only used simple print statements to check whether the mid_value was getting updated correctly, as well as another to check whether the length of candidate was getting smaller as well.

# Implement some of those tests in PyTest!
I’m still unsure how to use PyTest, as well as how to create tests for methods or functions being used in a GUI.
