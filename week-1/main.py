# Command-line calculator app.
#   Written by MadKamel

def is_int(string):
    try:
        return type(int(string)) == int
    except:
        return False



if __name__ == '__main__':

    while True:
        # get input, split by spaces.
        uIn = input(':> ').split(' ')

        for i in range(len(uIn)):
            if is_int(uIn[i]):
                
