"""
---------------------------------
Ninety One Python Code Submission
---------------------------------
Jerome Leibovici
25 October 2020
--------------------------------
"""

import sys

"""
num2words takes an integer and returns it in word form, e.g., given the number
1234 as an input, it returns the outpout "one thousand, two hundred, 
and thirty-four"

- Case 1: When num < 20, we return the number directly as it is the index in 
  the list object "less_20"
   
- Case 2: When the number is less than 100: We return the index of the 
  the second digit (i.e., in the case of 20, this is 2), minus 2 (since first
  value in "tens" is 'twenty'), plus whatever the digit left is. E.g., 67 
  returns the 6-2=4th index of the list object "tens"; and, if the number is 
  not a multiple of 10 (which it is not in this case) then you return the 
  remaining digit as previously described in case 1

- Case 3: When the number is larger than 99 we solve the problem by enacting 
  recursion in the formula. For example, the number 543,202 is two sub-problems 
  543 and 202. We look for the largest "pivot" in the number, which in this 
  case is 'thousand', divide it by the pivot to give us 543, which has largest 
  "pivot 'hundred', and so we return five hundred, and fourty-three using case 
  2, two-hundred and 2 comes from another instance of the the recursion 
  done similarly
  
Case 3 requires us to also correctly place commas and 'and' in their 
appropriate points in the returned text. Numbers greater than 99, which contain 
numbers 99 or less must have 'and' before them, there is an if-else statement 
which does this by identifying numbers less than 100 in case 3
"""

def num2words(num): 
    #Define list objects and dictionary for pivots
    less_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
               'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 
               'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 
               'nineteen'] 

    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
            'ninety'] 
    
    more_100 = {100:'hundred', 1000:'thousand', 1000000:'million', 
                1000000000:'billion'} 
     
    if num < 20: 
        return less_20[num] 
    	 
    if num < 100: 
        return tens[(int)(num/10)-2] + ('' if num%10==0 else '-' + less_20[num%10]) 
    # Find the appropriate pivot,e.g, 'thousand'
    pivot = max([key for key in more_100.keys() if key <= num]) 

    if num%pivot==0:
        return num2words((int)(num/pivot)) + ' ' + more_100[pivot] + ' '
    else:
        return num2words((int)(num/pivot)) + ' ' + more_100[pivot] + (' and ' if num%pivot < 100 else ', ') + num2words(num%pivot) 

"""
Whilst num2word can convert integers to words, text2nums2words takes text as an 
input and extracts the valid numbers (i.e., numbers with no improper 
characters). Although not specified in the task, the function can handle more 
than one valid number to convert to word
- Step 1: Split the text into individual strings using text.split() into a list
  object "word_list"
- Step 2: Create empty list, "num_list", to append valid numbers to
- Step 3: Define list object "improper_char", which contains improper 
  characters that could be discovered in individual strings containing numbers 
  in them. This list is not definitive and can be evolved to include further 
  possibile improper characters
- Step 4: For loop through strings in "word_list". If number is a valid number, 
  append to num_list; if string contains any improper characters, check if it 
  also contains any numbers - if yes than an invalid number has been found and 
  throw error
- Step 5: If num_list does contain valid number(s) and no invalid numbers have 
  been found, then convert numbers to words using num2word() function above
"""

def text2nums2words(text):     
    #Split the text into individual strings
    word_list = text.split()    
    #List object to append valid numbers in text to
    num_list = []
    #Define improper characters
    improper_char = [',','.','$','£','€','¥','#']
    for w in word_list:
        #If element is a valid number, append to num_list
        if w.isnumeric():
            num_list.append(int(w))
        #Identify if there are numbers containing improper characters 
        #and issue error
        elif 1 in [c in w for c in improper_char]:
            w_split = [char for char in w]
            w_split_num = [c for c in w_split if c.isnumeric()]
            if len(w_split_num) != 0:
                return sys.stdout.write('number invalid'+'\n')
    #Assuming num_list not empty, for each valid number convert it to word form
    if len(num_list) == 0:
        return sys.stdout.write('no numbers found'+'\n')
    for num in num_list:
        sys.stdout.write(num2words(num)+'\n')

"""
file2text2nums2words() - excuse the long function name! - is akin to 
text2nums2words() but takes a file path to .txt file as an input
"""

def file2text2nums2words(file_path):
    file = open(file_path,"r")
    text = file.read()
    return text2nums2words(text)

"""
Examples
"""

test_input_1 = 'The pump is 536 deep underground'
test_input_2 = 'We processed 9121 records'
test_input_3 = 'Variables reported as having a missing type #65678'
test_input_4 = 'Interactive and printable 10022 ZIP code'
test_input_5 = 'The database has 66723107008'
test_input_6 = 'I received 23 456,9 KGs'
test_input_7 = 'South Africa is 122000000 square kiolmetre with a population of 57780000'

text2nums2words(test_input_1)
text2nums2words(test_input_2)
text2nums2words(test_input_3)
text2nums2words(test_input_4)
text2nums2words(test_input_5)
text2nums2words(test_input_6)
text2nums2words(test_input_7)
