try:
    f = open("simple.txt", 'r')
    f.write("Test write to simple text!")
except IOError:
    print("Could not find file or read data")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("I ALWAYS WORK < NO MATTER WHAT!")
