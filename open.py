from traceback import print_tb


try:
    open('config.txt')
except FileNotFoundError:
    print("Couldnt find the config.txt file! ")
