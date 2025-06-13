# file = open('/Users/felka/Documents/Python/Udemy Course/Section 24 - Improved Snake/File Playground/test_file.txt')
# contents = file.read()
# file.close()
# print(contents)

# Makes sure you don't need to rememeber to close the file after you're done
with open('/Users/felka/Documents/Python/Udemy Course/Section 24 - Improved Snake/File Playground/test_file.txt', mode="a") as file:
    # contents = file.read()
    file.write("\nNew text.")
    # print(contents)