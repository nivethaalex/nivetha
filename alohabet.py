# taking user input
ch = input("Enter a character: ")
if((ch>='n' and ch<= 's') or (ch>='N' and ch<='S')):
    print(ch, "is an Alphabet")
else:
    print(ch, "is not an Alphabet")
