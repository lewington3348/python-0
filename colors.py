orange =  '\033[1;31m'
violet = '\033[0;35m'
green  = '\033[0;32m'
cyan   = '\033[0;36m'
base03  =  '\033[0;30m'
yellow = '\033[0;33m'
blue = '\033[0;34m'
red = '\033[0;31m'
base01  = '\033[0;32m'
magenta = '\033[0;35m'
base1 = '\033[1;36m'
base0 = '\033[1;4m'
base00 = '\033[1;33m'
base2 = '\033[0;7m'
base3 = '\033[7;37m'
base02 = '\033[0;30m' 





import random
def random_color():
   
   return random.choice([green, violet, cyan, yellow])

if __name__ == "__main__":
    print(yellow + 'Yellow')
