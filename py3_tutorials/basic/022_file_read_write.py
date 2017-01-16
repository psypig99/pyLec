# fw = open("test.txt", "w")
# fw.write("These are python tutorials for beginner\n")
# fw.write("I Love to make some program \n")
# fw.close()

fr = open("test.txt", "r")
contents = fr.read()
print(contents)
fr.close()