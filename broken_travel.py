# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))
'''
    Corrections made:
        - Changed "==" to "=".
        - Changed "." to "(".
        - Changed the single quotation and the end of the input statement to double quotation. 
'''

if year <= 1900:
    print ("Woah, that's the past!")
    '''
        Corrections made:
            - Removed the spacing between print and the parenthesis.
            - Changed the single quotations inside the print statement parenthesis to double quotations.
    '''
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
    '''
        Corrections made:
            - Changed "&&" to "and".
            - Removed the spacing between print and the parenthesis.
    '''
else:
    print ("Far out, that's the future!!")
    '''
        Corrections made:
            - Changed "elif" to "else" 
            - Removed the spacing between print and the parenthesis.
    '''
