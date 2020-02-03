Daniel Hwang
Alexander Swanson
CSCI345 HW 1

how to run:
I'd recommend you to run this python file with pycharm. 
if you want to test out with your custom password file, just change
PASSWORD_LIST = open('file_name','r').read() file name to your password file. 


place all files in the same folder. There are should be 
a python file
password_list.txt
password_ans.txt
and words file.

password_list.txt file contains list of usernames and hashed in username:hashedpasswords format
password_ans.txt file contains list of usernames and actual passwords before it's hashed. 
word file is the word list file that Dr.Xenia has posted on oaks. 

In program, it will compare if it's password of 5 digit number, and then will compare with wordlist,
and finally, will compare if it's 7 digit number. 

The reason why I did in this order is, 4 digit number + 4 random character is possibility of 40000 cases.
the word file contains approximately 120,000 + substituted words, and 7 digit number contains possibility of
1,000,000. I thought finding from lower possibility to higher possibilty would take less time. So cracking 
passwords from 5 digit, words to 7 digit number is much faster than finding passwords from 7th digit number
to 5 digit, and words. 