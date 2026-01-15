print() is a built-in Python function
    Its main purpose is to send output to the console (standard output)
    We use it to see the result of our code, debug, or display messages to the user

Why Do We Need print()?

    See program output:
        Python runs code in memory, but without print() we won’t see anything on the screen.
    Debugging:
        we can print variables or expressions to check if our program is working correctly.

What Happens When You Call print()?
    When we write print(some_value), here’s what happens internally:

    Python evaluates the expression inside print()
    x = 5
    print(x + 10)  # Python calculates 5 + 10

    15 # Output

    Converts the value to a string using the str() function (so it can be displayed).
    Sends the string to standard output (sys.stdout):

Important Parameters of print()
    sep   -> Separator between multiple values
    end   -> What to print at the end (default \n)
    file  -> Where to send output (default sys.stdout)
    flush -> Force immediate output


Behind the Scenes

    Think of print() like this:
        you call print(value)
        Python internally does:
            text = str(value)          # convert value to string
            sys.stdout.write(text)     # write to terminal
            sys.stdout.write("\n")     # add newline
    The user sees output on the console

    print() is basically a bridge between your program and the system’s console.


Key Points
    print() is not mandatory, but without it, your program won’t show output
    Converts values to strings and sends to stdout
    Default behavior: separate values by space + newline at the end
    Can be customized using sep, end, file, flush


you can see some examples, in the folder structures...