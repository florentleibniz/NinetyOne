# Ninety One Python Code Submission


Python script contains three functions that convert number(s) into words.

**1. num2words():** Takes an integer input and returns it in word form, e.g., given the number 1234 as an input, it returns the outpout "one thousand, two hundred, and thirty-four". This problem can be broken down into three cases:

**Case 1:** When num < 20, we return the number directly as it is the index in the list object _less_20_
   
**Case 2:** When the number is less than 100, we return the index of the second digit (i.e., in the case of 20, this is 2), minus 2 (since first value in _tens_ is _twenty_), plus whatever the digit left is. E.g., 67 returns the 6-2=4th index of the list object _tens_; and, if the number is not a multiple of 10 (which it is not in this case) then you return the remaining digit as previously described in case 1

**Case 3:** When the number is larger than 99 we solve the problem by enacting recursion in the formula. For example, the number 543,202 is two sub-problems 543 and 202. We look for the largest _pivot_ in the number, which in this case is _thousand_, divide it by the pivot to give us 543, which has largest pivot _hundred_, and so we return five hundred, and forty-three using case 2, two-hundred and 2 comes from another instance of the the recursion done similarly. Case 3 requires us to also correctly place commas and 'and' in their appropriate points in the returned text. Numbers greater than 99, which contain numbers 99 or less must have 'and' before them, there is an if-else statement which does this by identifying numbers less than 100 in case 3

**2. text2nums2words():** While _num2word()_ can convert integers to words, _text2nums2words()_ takes text as an input and extracts the valid numbers (i.e., numbers with no improper 
characters). Although not specified in the task, the function can handle more 
than one valid number to convert to word

**3. file2text2nums2words():** Akin to 
_text2nums2words()_ but takes a file path to .txt file as an input

## Usage

```python
import sys
num2word(536) # returns 'five hundred and thirty-six'	num2word(536) # returns 'five hundred and thirty-six'
text2nums2words('The pump is 536 deep underground') # returns 'five hundred and thirty-six'
