import base64
import sys
import os

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=6, cols=42))

def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

program=input('''
Enter the name of the program:

''')

clr()

rec=int(input('''
How many recursions?

Tip:
1 Recursion\t = Weak
2 Recursions\t = Good
3 Recursions\t = Best
4+ Recursions\t = Crazy Ass
'''))
clr()

with open(program, 'r') as f:
    file=f.read()

file=file+'#'*1000

def b64(file):
    encodedBytes = base64.b64encode(file.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

def b32(file):
    encodedBytes = base64.b32encode(file.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

def b16(file):
    encodedBytes = base64.b16encode(file.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

encodedStr=file
for r in range(rec):
    encodedStr=b64(encodedStr)
    encodedStr=b32(encodedStr)
    encodedStr=b16(encodedStr)
    encodedStr="import base64;exec(base64.b64decode((base64.b32decode((base64.b16decode('"+encodedStr+"'))))))"
    print(f"{(r+1)/rec*100:.3f} %", end="\r")

p=program.find('.py')
program=program[:p]+'_encrypted.py'
with open(program, 'w') as f:
    f.write(encodedStr)
