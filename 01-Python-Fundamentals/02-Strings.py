"""
Topic: [Strings, integers, Floats]



Strings = "Strings are a sequence of characters. They can be defined using single quotes, double quotes, or triple quotes. Strings are immutable, meaning they cannot be changed after they are created."
           
           1 ' .... '
           2 " .... "
           3 ''' .... '''

        String methods:

          # lower()
          # upper()
          # replace()
          # split()
          # count()
          # Etc...
          
integers = "Integers are whole numbers, positive or negative, without decimals. They can be defined using the int() function or by simply assigning a whole number to a variable."
          # Whole no. = -2,-1,0,1,2,3,4,5, etc...

floats = "Floats are numbers that have a decimal point. They can be defined using  
        # Decimal no. = 0.1, 1.2, 3.14, 5.0, etc... 
"""  
#String examples:

message = "Hello World"                    
print(message.lower())                      
print(message.upper())                      
print(message[0:8])                         
print(len(message))                         

#Integer and Float examples:

num_1 = 10
num_2 = 2.2
print(num_1 + num_2)
print(num_1 * num_2)
print(num_1 / num_2)


# practice example:

 #write a program to get the first, middle, and last character of a string and print them in uppercase.
 
 #Given input: str1 = 'james'
 #             first_char = str1[0]
 #             last_char = str1[-1]

#output: 'JMS'
         


str1 = 'james'
first_char = str1[0]

# for middle_char divide the length of the string by 2 and use that as the index to get the middle character 
res = len(str1) 
middle_char = str1[res//2]
last_char = str1[-1]
New_str = first_char + middle_char + last_char

print(New_str.upper())


