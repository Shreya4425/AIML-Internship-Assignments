filename = input("Enter a file name:")
try :
    file = open(filename, "r")
    print(file.read())

except FileNotFoundError:
    print("Oops! That file doesn't exist yet")
    
# finally :
#     file.close()

# finally:
#     try:
#         file.close()
#     except NameError:
#         pass