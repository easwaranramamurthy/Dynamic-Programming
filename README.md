Dynamic Programming Examples
==========================

These are some solutions to basic dynamic programming problems that I implemented in Python

###Subset Sum:
The code randomly generates an input set and solves the Subset Sum Problem with integer bound W using dynamic programming. It prints out the dynamic programming matrix and outputs the weights of the particular objects that have been selected for inclusion in the maximum weight subset within the bound W. 

###Command:
```python subsetSum.py```


###String Alignment:
Uses dynamic programming to align two input strings using user provided match, mismatch and gap scores. Uses similarity scoring, so match scores must be less than mismatch and gap scores (e.g match = 0, gap = 5, mismatch = 4). Prints out the dynamic programming matrix and outputs the best posible sequence alignment based on the scoring function input by the user.

###Command:
```python stringAlignment.py```
