#how this works: you type stuff in, it edits a file.

doc_path ='doc.txt'

#mode 'WRITE' is write
#mode 'READ' is read
mode=''

while True:
    uIn = input(':> ')
    if uIn == 'help':
        print('welcome to the madkamel daily challenge word processor!')
        print('this program will allow you to edit text files in a command line.')
        print('   to use this program, you will use commands. some examples of')
        print('   commands include:')
        print()
        print('       >help - gets this help screen')
        print('       >mode - gives a prompt to switch mode')
