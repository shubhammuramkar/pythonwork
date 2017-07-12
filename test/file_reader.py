with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())    # The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line. If you want to remove the extra blank line, you can use rstrip() in the print statement:

