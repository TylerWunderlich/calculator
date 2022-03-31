# Import the math, tkinter, sympy, and sympy.abc modules
from math import *
from tkinter import *
from sympy import diff, integrate, symbols, init_printing, cos, sin, tan, log, exp, Pow, sqrt, asin, acos, atan
from sympy.abc import x, y, z

# Create the calculator object
class Calculator:
    
    # Declare string that changes based on button input
    global expression
    
    # Declare StringVar() variable that represents output in text window
    global equation

    # Initialize expression as empty string
    expression = ""

    # Create window for calculator
    gui = Tk()

    # Set dimensions of calculator
    gui.geometry("500x230")

    # Set title
    gui.title("Calculator")

    # Make the background white
    gui.configure(background='white')

    # Prevent the window size from being altered
    gui.resizable(0,0)

    # Initialize equation as StringVar() object
    equation = StringVar()

    # Create text field that takes equation as the input variable
    expression_field = Entry(gui, textvariable=equation, font=(24))

    # Arrange the calculator in a grid-like format
    expression_field.grid(ipadx=300, ipady=10, columnspan=100)

    # Function that displays 7 in text field when button is pressed
    def press_seven():
        global expression
        expression = expression + "7"
        equation.set(expression)

    # Function that displays 8 in text field when button is pressed
    def press_eight():
        global expression
        expression = expression + "8"
        equation.set(expression)

    # Function that displays 9 in text field when button is pressed
    def press_nine():
        global expression
        expression = expression + "9"
        equation.set(expression)
    
    # Function that displays 4 in text field when button is pressed
    def press_four():
        global expression
        expression = expression + "4"
        equation.set(expression)

    # Function that displays 5 in text field when button is pressed
    def press_five():
        global expression
        expression = expression + "5"
        equation.set(expression)

    # Function that displays 6 in text field when button is pressed
    def press_six():
        global expression
        expression = expression + "6"
        equation.set(expression)

    # Function that displays 1 in text field when button is pressed
    def press_one():
        global expression
        expression = expression + "1"
        equation.set(expression)

    # Function that displays 2 in text field when button is pressed
    def press_two():
        global expression
        expression = expression + "2"
        equation.set(expression)

    # Function that displays 3 in text field when button is pressed
    def press_three():
        global expression
        expression = expression + "3"
        equation.set(expression)

    # Function that displays a decimal point in text field when button is pressed
    def press_period():
        global expression
        expression = expression + "."
        equation.set(expression)

    # Function that displays 0 in text field when button is pressed
    def press_zero():
        global expression
        expression = expression + "0"
        equation.set(expression)

    # Function that displays a plus sign in text field when button is pressed
    def press_plus():
        global expression
        expression = expression + "+"
        equation.set(expression)

    # Function that displays a minus sign in text field when button is pressed
    def press_minus():
        global expression
        expression = expression + "-"
        equation.set(expression)

    # Function that displays a multiplication sign in text field when button is pressed
    def press_multiply():
        global expression
        expression = expression + "*"
        equation.set(expression)

    # Function that displays a division sign in text field when button is pressed
    def press_divide():
        global expression
        expression = expression + "/"
        equation.set(expression)

    # Function that uses the eval() function to evaluate the string as a mathematical expression
    # Returns nan (not a number) if the input is invalid
    def press_equal():
        try:
            global expression
            total = str(eval(expression))
            equation.set(total)
            expression = total
        except:
            equation.set(nan)
            expression = ""

    # Function that displays a right paranthesis in text field when button is pressed
    def press_right_paren():
        global expression
        expression = expression + ")"
        equation.set(expression)

    # Function that displays a left paranthesis in text field when button is pressed
    def press_left_paren():
        global expression
        expression = expression + "("
        equation.set(expression)

    # Function that clears everything in the text field when button is pressed
    def press_clear():
        global expression
        expression = ""
        equation.set("")

    # Function that displays a minus sign in text field when button is pressed
    def press_negate():
        global expression
        expression = expression + "-"
        equation.set(expression)

    # Function that displays 'sin(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_sin():
        global expression
        expression = expression + "sin("
        equation.set(expression)

    # Function that displays 'cos(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_cos():
        global expression
        expression = expression + "cos("
        equation.set(expression)

    # Function that displays 'tan(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_tan():
        global expression
        expression = expression + "tan("
        equation.set(expression)

    # Function that displays 'asin(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_arcsin():
        global expression
        expression = expression + "asin("
        equation.set(expression)

    # Function that displays 'acos(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_arccos():
        global expression
        expression = expression + "acos("
        equation.set(expression)

    # Function that displays 'atan(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_arctan():
        global expression
        expression = expression + "atan("
        equation.set(expression)

    # Function that displays '/100' in text field when button is pressed
    def press_percent():
        global expression
        expression = expression + "/100"
        equation.set(expression)

    # Function that displays 'factorial(' in text field when button is pressed
    def press_factorial():
        global expression
        expression = expression + "factorial("
        equation.set(expression)

    # Function that displays an e in text field when button is pressed
    def press_e():
        global expression
        expression = expression + "e"
        equation.set(expression)

    # Function that displays 'pi' in text field when button is pressed
    def press_pi():
        global expression
        expression = expression + "pi"
        equation.set(expression)

    # Function that deletes the last character of string in text field when button is pressed
    def press_delete():
        global expression
        expression = expression[:-1]
        equation.set(expression)

    # Function that displays 'sqrt(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_sqrt():
        global expression
        expression = expression + "sqrt("
        equation.set(expression)

    # Function that displays 'log(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_ln():
        global expression
        expression = expression + "log("
        equation.set(expression)

    # Function that displays 'log10(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_log():
        global expression
        expression = expression + "log10("
        equation.set(expression)

    # Function that displays 'exp(' in text field when button is pressed
    # Enter number as a double or the function won't evaluate the expression
    def press_exp():
        global expression
        expression = expression + "exp("
        equation.set(expression)

    # Function that displays 'Pow(' in text field when button is pressed
    def press_pow():
        global expression
        expression = expression + "Pow("
        equation.set(expression)

    # Function that displays a comma in text field when button is pressed
    def press_comma():
        global expression
        expression = expression + ","
        equation.set(expression)

    # Function that displays an x in text field when button is pressed
    def press_x():
        global expression
        expression = expression + "x"
        equation.set(expression)

    # Function that displays a y in text field when button is pressed
    def press_y():
        global expression
        expression = expression + "y"
        equation.set(expression)

    # Function that displays a z in text field when button is pressed
    def press_z():
        global expression
        expression = expression + "z"
        equation.set(expression)

    # Function that displays 'diff(' in text field when button is pressed
    def press_derive():
        global expression

        # Initialize x, y, z so the diff() function can understand them
        symbols('x, y, z')

        init_printing(use_unicode=True)
        expression = expression + "diff("
        equation.set(expression)

    # Function that displays 'integrate(' in text field when button is pressed
    def press_integrate():
        global expression

        # Initialize x, y, z so the integrate() function can understand them
        symbols('x, y, z')

        init_printing(use_unicode=True)
        expression = expression + "integrate("
        equation.set(expression)

    # Create the 7 button
    seven_button = Button(gui, text="7", width=10, fg='black', bg='yellow', command=press_seven)
    seven_button.grid(row=1, column=0)

    # Create the 8 button
    eight_button = Button(gui, text="8", fg='black', bg='yellow', width=10, command=press_eight)
    eight_button.grid(row=1, column=1)

    # Create the 9 button
    nine_button = Button(gui, text="9", fg='black', bg='yellow', width=10, command=press_nine)
    nine_button.grid(row=1, column=2)

    # Create the 4 button
    four_button = Button(gui, text="4", fg='black', bg='yellow', width=10, command=press_four)
    four_button.grid(row=2, column=0)

    # Create the 5 button
    five_button = Button(gui, text="5", fg='black', bg='yellow', width=10, command=press_five)
    five_button.grid(row=2, column=1)

    # Create the 6 button
    six_button = Button(gui, text="6", fg='black', bg='yellow', width=10, command=press_six)
    six_button.grid(row=2, column=2)

    # Create the 1 button
    one_button = Button(gui, text="1", fg='black', bg='yellow', width=10, command=press_one)
    one_button.grid(row=3, column=0)

    # Create the 2 button
    two_button = Button(gui, text="2", fg='black', bg='yellow', width=10, command=press_two)
    two_button.grid(row=3, column=1)

    # Create the 3 button
    three_button = Button(gui, text="3", fg='black', bg='yellow', width=10, command=press_three)
    three_button.grid(row=3, column=2)

    # Create the period button
    period_button = Button(gui, text=".", fg='black', bg='yellow', width=10, command=press_period)
    period_button.grid(row=4, column=0)

    # Create the 0 button
    zero_button = Button(gui, text="0", fg='black', bg='yellow', width=10, command=press_zero)
    zero_button.grid(row=4, column=1)

    # Create the equal sign button
    equal_button = Button(gui, text="=", fg='black', bg='yellow', width=10, command=press_equal)
    equal_button.grid(row=4, column=2)

    # Create the plus sign button
    plus_button = Button(gui, text="+", fg='black', bg='yellow', width=10, command=press_plus)
    plus_button.grid(row=1, column=3)

    # Create the minus sign button
    minus_button = Button(gui, text="-", fg='black', bg='yellow', width=10, command=press_minus)
    minus_button.grid(row=2, column=3)

    # Create the multiply sign button
    multiply_button = Button(gui, text="*", fg='black', bg='yellow', width=10, command=press_multiply)
    multiply_button.grid(row=3, column=3)

    # Create the division sign button
    divide_button = Button(gui, text="/", fg='black', bg='yellow', width=10, command=press_divide)
    divide_button.grid(row=4, column=3)

    # Create the clear button
    clear_button = Button(gui, text="C", fg='black', bg='yellow', width=10, command=press_clear)
    clear_button.grid(row=5, column=3)

    # Create the left paranthesis button
    left_paren_button = Button(gui, text=")", fg='black', bg='yellow', width=10, command=press_right_paren)
    left_paren_button.grid(row=5, column=2)

    # Create the right paranthesis button
    right_paren_button = Button(gui, text="(", fg='black', bg='yellow', width=10, command=press_left_paren)
    right_paren_button.grid(row=5, column=1)

    # Create the negative sign button
    negate_button = Button(gui, text="(-)", fg='black', bg='yellow', width=10, command=press_negate)
    negate_button.grid(row=5, column=0)

    # Create the sine button
    sin_button = Button(gui, text="sin", fg= 'white', bg= 'black', width=10, command=press_sin)
    sin_button.grid(row=1, column=4)

    # Create the cosine button
    cos_button = Button(gui, text="cos", fg= 'white', bg= 'black', width=10, command=press_cos)
    cos_button.grid(row=2, column=4)

    # Create the tangent button
    tan_button = Button(gui, text="tan", fg= 'white', bg= 'black', width=10, command=press_tan)
    tan_button.grid(row=3, column=4)

    # Create the inverse sine button
    arcsin_button = Button(gui, text="arcsin", fg= 'white', bg= 'black', width=10, command=press_arcsin)
    arcsin_button.grid(row=1, column=5)

    # Create the inverse cosine button
    arccos_button = Button(gui, text="arccos", fg= 'white', bg= 'black', width=10, command=press_arccos)
    arccos_button.grid(row=2, column=5)

    # Create the inverse tangent button
    arctan_button = Button(gui, text="arctan", fg= 'white', bg= 'black', width=10, command=press_arctan)
    arctan_button.grid(row=3, column=5)

    # Create the percent button
    percent_button = Button(gui, text="%", fg= 'white', bg= 'black', width=10, command=press_percent)
    percent_button.grid(row=4, column=4)

    # Create the factorial button
    factorial_button = Button(gui, text="!", fg= 'white', bg= 'black', width=10, command=press_factorial)
    factorial_button.grid(row=4, column=5)

    # Create the e button
    e_button = Button(gui, text="e", fg= 'white', bg= 'black', width=10, command=press_e)
    e_button.grid(row=5, column=4)

    # Create the pi button
    pi_button = Button(gui, text="π", fg= 'white', bg= 'black', width=10, command=press_pi)
    pi_button.grid(row=5, column=5)

    # Create the delete button
    delete_button = Button(gui, text="del", fg= 'white', bg= 'black', width=10, command=press_delete)
    delete_button.grid(row=6, column=0)

    # Create the square root button
    sqrt_button = Button(gui, text="√", fg= 'white', bg= 'black', width=10, command=press_sqrt)
    sqrt_button.grid(row=6, column=1)

    # Create the natural log button
    ln_button = Button(gui, text="ln", fg= 'white', bg= 'black', width=10, command=press_ln)
    ln_button.grid(row=6, column=2)

    # Create the log base 10 button
    log_button = Button(gui, text="log", fg= 'white', bg= 'black', width=10, command=press_log)
    log_button.grid(row=6, column=3)

    # Create the exponential button
    exp_button = Button(gui, text="eⁿ", fg= 'white', bg= 'black', width=10, command=press_exp)
    exp_button.grid(row=6, column=4)

    # Create the power button
    pow_button = Button(gui, text="xⁿ", fg= 'white', bg= 'black', width=10, command=press_pow)
    pow_button.grid(row=6, column=5)

    # Create the comma button
    comma_button = Button(gui, text=",", fg= 'white', bg= 'black', width=10, command=press_comma)
    comma_button.grid(row=7, column=0)

    # Create the x button
    x_button = Button(gui, text="x", fg= 'white', bg= 'black', width=10, command=press_x)
    x_button.grid(row=7, column=1)

    # Create the y button
    y_button = Button(gui, text="y", fg= 'white', bg= 'black', width=10, command=press_y)
    y_button.grid(row=7, column=2)

    # Create the z button
    z_button = Button(gui, text="z", fg= 'white', bg= 'black', width=10, command=press_z)
    z_button.grid(row=7, column=3)

    # Create the derivative button
    derive_button = Button(gui, text="d/dx", fg= 'white', bg= 'black', width=10, command=press_derive)
    derive_button.grid(row=7, column=4)

    # Create the integral button
    integrate_button = Button(gui, text="∫", fg= 'white', bg= 'black', width=10, command=press_integrate)
    integrate_button.grid(row=7, column=5)
    
    # Initiate the calculator loop
    gui.mainloop()

# Create the Calculator() object
operation = Calculator()