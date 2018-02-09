#######################################################################################
# Author: Annie He
# Username: hea
# Date: 3/18/16
# Purpose: 
#   Lab 2
#   Learn about an important application of computer science, the UPC code
#   Work on the design of a larger problem
#   Use lists in an application problem 
########################################################################################
# Acknowledgements:
# Dr. Jan Pearce - the testit function was used from her work
# Dawn Manning - helped with problems in coding during lab hours
# Ashley Aiken - helped with problems in coding during lab hours
# Cody Myers - helped with problems in coding and taught me how to use the pop method
########################################################################################

import turtle
import sys

def testit(did_pass):
    """ The testit function will print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def ask_file():
    '''The ask_file function asks the user for a file to open and read. The text will be returned as content'''
    check_file = raw_input("What file would you like to check?")
    text_file = open(check_file) #opens up the file inputted by the user
    content = text_file.read()  #takes the file and reads it
    text_file.close()   #closes the file
    return content  #returns what was read in the file

def is_barcode(content):
    '''The is_barcode funciton checks to see if the file is 12 digits. 
    If it is, it will return True, if not, it will return False. This funciton also 
    checks whether the content is valid being all numbers, or invalid having 
    spaces or invalid characters'''
    good_content = {}   #creates a dicitonary
    #inside the dicitonary are the numbers 0-9, which are the valid characters allowed in the file
    good_content = {"0": True, "1": True, "2": True, "3": True, "4": True, "5": True, "6": True, "7": True, "8": True, "9": True}
    if len(content) == 12:  #only passes if the length of the content inside the file is equal to 12
        for i in content:
            if good_content[i] == True:     #if the characters in the content are valid, it will return True
                true_modulo = module_num(content)
                if(true_modulo):
                    pass
    else:
        return False
    return True
        
def module_num(content):
    '''The module_num function will calculate the modulo check character. Once it is finished 
    calculating, it will compare the result to the last digit in the content. If the content and 
    result matches, the UPC code is valid and will continue. If the content and result does not 
    match, it will return False'''
    #find the odd positioned of the file numbers and add them together
    odd_sum = 0    
    for i in range(len(content)): 
        if i % 2 == 0: #since computer scientists start counting at 0, the even positioned digits are in the odd position places
            odd_sum += int(content[i]) 
        else:
            pass      
    odd_mult = odd_sum*3     #multiply the sum by 3 
    #add the even positioned numbers, excluding the last number
    even_sum = 0
    for i in range(len(content)-1): 
        if i % 2 != 0: #since computer scientists start counting at 0, the odd positioned digits are in the even position places
            even_sum += int(content[i])
        else:
            pass   
    #add the first sum and the second sum together and find the remainder divided by 10
    total_sum = odd_mult + even_sum
    remainder = total_sum % 10
    #If the result is not zero, subtract the result from ten to yield your check digit 
    if remainder != 0:
        digit = 10 - remainder
    # Otherwise the check digit is zero.
    else:
        digit = remainder
    #compare to see if code is valid
    if digit == int(content[11]):
        return True
    else:
        return False
        
def chunks(content):
    '''The chunk funciton splits the string of numbers into chunks of 6 to
    have a left and right side, and puts them in a list. Then the two lists are combined
    together into one large list'''
    test = []
    whole_barcode = []  
    for i in content:
        whole_barcode.append(i)
    left_bar = whole_barcode[0:6] #takes only the first 6 digits and assigns it to left_bar
    right_bar = whole_barcode[6:] #takes the rest of the digits and assigns it to right_bar
    test.append(left_bar)   #combines the left_bar and the 
    test.append(right_bar)  #right_bar into one list called test
    return test     #returns nested lists
    
def left_digit(left_bar):
    '''The left_digit function takes the digits in the left_bar and compares them to the corresponding 
    binary number, then returns it'''
    left_binary = []
    for i in left_bar:
        if i == '0':
            left_binary.append('0001101')
        elif i == '1':
            left_binary.append('0011001')
        elif i == '2':
            left_binary.append('0010011')
        elif i == '3':
            left_binary.append('0111101')
        elif i == '4':
            left_binary.append('0100011')
        elif i == '5':
            left_binary.append('0110001')
        elif i == '6':
            left_binary.append('0101111')
        elif i == '7':
            left_binary.append('0111011')
        elif i == '8':
            left_binary.append('0110111')
        elif i == '9':
            left_binary.append('0001011')
    return left_binary
            
def right_digit(right_bar):
    '''The right_digit function takes the digits in the right_bar and compares them to the corresponding 
    binary number, then returns it'''
    right_binary = []
    for i in right_bar:
        if i == '0':
            right_binary.append('1110010')
        elif i == '1':
            right_binary.append('1100110')
        elif i == '2':
            right_binary.append('1101100')
        elif i == '3':
            right_binary.append('1000010')
        elif i == '4':
            right_binary.append('1011100')
        elif i == '5':
            right_binary.append('1001110')
        elif i == '6':
            right_binary.append('1010000')
        elif i == '7':
            right_binary.append('1000100')
        elif i == '8':
            right_binary.append('1001000')
        elif i == '9':
            right_binary.append('1110100')
    return right_binary
            
def full_binary(left, right):
    '''The full_binary function combines the binary code for the center and outside guards
    of the barcode to the rest of the code that has already been converted to binary'''
    binary = []
    binary.append("101")    #connects 101 as the beginning guard bar to the binary set
    for chunk in left:
        binary.append(chunk)
    binary.append("01010")  #connects 01010 as the center bars in the barcode
    for chunk in right:
        binary.append(chunk)
    binary.append("101")    #connects 101 as the end guard bar to the binary set
    return binary
    
def test_suite():
    '''The test_suite function tests the different functions to see if they work'''
    #test_suite for is_barcode
    testit(is_barcode('896735849056')==True)
    testit(is_barcode('647284657')==False)
    #test_suite for module_num
    testit(module_num('886971299922')==True)
    testit(module_num('267846393629')==False)
    #test_suite for chunk
    testit(chunks('5673829')==[['5','6','7','3','8','2'], ['9']])
    testit(chunks('284637904675')==[['2','8','4','6','3','7'], ['9','0','4','6','7','5']]) 
    
def error_message(message):
    '''The error_message function will only run if the code is invalid and will display a
    message on the turtle window'''
    message = turtle.Turtle()
    message.color("Red")
    message.penup()
    message.setpos(12,100)
    message.pendown()
    message.write("The file you submitted is either too long/short, \n or contains a character that is invalid.",move=False,align='center',font=("Arial",25,("bold","normal")))
    message.hideturtle()

def draw_lines(numList):
    '''The draw_lines function will draw the valid barcode based on the binary code that was given and 
    combined in the left_digit and right_digit funcitons. It will take the string of code and reverse it. 
    It will eventually use the pop method so that when the UPC code gets printed on the turtle window, 
    it will use the last number first, and complete the loop without that number being repeated. If the
    code was not valid, it will use turtle to display the error message'''
    go_on = is_barcode(numList)
    leftright = chunks(numList)
    leftbinary = left_digit(leftright[0])   #does the left side of the binary code
    rightbinary = right_digit(leftright[1])     #does the right side of the binary code
    full_bar = full_binary(leftbinary, rightbinary)
    numList = numList[::-1]     #reverses the string of code 
    numList = list(numList)     #puts the numbers in a list
    wn = turtle.Screen()    #creates a turtle window
    lines = turtle.Turtle()     #creates a turtle called lines
    if(go_on):
        lines.speed(10)     #controls the speed of the turtle
        x = -200
        y = 90
        lines.penup()   #lifts the turtle pen up
        lines.setpos(-200, 90)     #sets the position of the turtle
        lines.setheading(-90)   #turns the turtle to face south instead of east
        lines.pendown()     #places the turtle pen down
        lines.pensize(1)    #changes the pensize to 5
        for chunk in full_bar:
            length = 40    #normally, the lines will be set to this length
            draw_num = True
            if len(chunk) < 7:  #if the length of chunk is less than 7, it will draw the lines longer
                length = 45
                draw_num = False
            else:
                num = numList.pop()
                initial = True  #this is so the code will only be written once instead of being repeatedly written
            for i in chunk:
                x = x +1    #moves the turtle over so the lines will be side by side on the barcode instead of overlapping
                if i == '0':
                    lines.color("White")    #sets the binary number 0 to draw a white line
                else:
                    lines.color("Black")   #sets the binary number 1 to draw a black line 
                lines.forward(length)   #normally draws a line the length of length(200)
                if draw_num != False:
                    if initial == True:     #if the code is valid, the code will be displayed on the screen
                        lines.color("Black")
                        lines.penup()
                        lines.forward(50)
                        lines.pendown()
                        lines.write(num)
                        initial = False     #stops the code being written once it is done
                lines.penup()
                lines.setpos(x, y)
                lines.pendown()
                lines.hideturtle()
    else:
        error_message(lines)
           
    wn.exitonclick()    #exits the screen on click
        
def main():
    '''The main function either draws a barcode and displays the UPC code when a valid filecode 
    was submitted, or it will display an error message when an invalid code was submitted'''
    numList = ask_file()
    draw_lines(numList)
    test_suite()
    
main()  #call main()