# FILE NAME - convert_C_to_F_01.py

# NAME: Yusuf Khan 
# DATE: 02/14/25
# BRIEF DESCRIPTION:  program converts temperature in celsius entered by user to farenheit.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience



    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

def convert_C_to_F():
   c = float(input('Enter a temperature in Celsius: '))
   f = c*9/5+32
   print(c, 'degrees Celsius is', f, 'degrees Fahrenheit.')
convert_C_to_F()


########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?

float means any type of data in python that is represented with a decimal point, so it can output fractional values.



2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

It is important to use float because otherwise you will not be getting exact data, instead you will be getting an estimate that is a whole number. 



'''
