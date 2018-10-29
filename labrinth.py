#x-2 * y-2
import time
import random
from getkey import getkey, keys
a = 50
b = 10
t = 0
cpos = [0,0]
stack =[[0,0],[0,0]]

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp =struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th
x,y = terminal_size()

charToPrint='█'
#charToPrint='@'

x -= x%3
y -= y%3

y -= 2
x -= 2
def xyToPos(a,b,x,y):
    return int((x+1)*(b)+(a))

def printPos(tab,a,b,char,x,y):
    ltab = list(tab)
    ltab[xyToPos(a,b,x,y)] = "" + char
    return "".join(ltab)

def getTabPos(tab,a,b,x,y):
    ltab = list(tab)
    return ltab[xyToPos(a,b,x,y)]

def cleartable():
    tab = charToPrint * x + "\n"
    for i in range(y-3):
        tab += (charToPrint + " " * (x-2) + charToPrint + "\n")
    tab += (charToPrint * x + "\n")
    return tab

tab = cleartable()



visited = 1
pos = [[0,0]]
condition = True
displayConstruct = False
speed = .01 if displayConstruct else 0
current = 0
while (condition):
    #Uncomment to see lab construction
    time.sleep(speed)
    array = ['u','d','l','r']

    if(cpos[0] < 3 or [int(cpos[0]-3),cpos[1]] in pos):
        array.remove('l')
    if(cpos[1] < 3 or [cpos[0],int(cpos[1]-3)] in pos):
        array.remove('u')
    if(cpos[0] > x-6 or [int(cpos[0])+3,cpos[1]] in pos):
        array.remove('r')
    if(cpos[1] > y-7 or [cpos[0],int(cpos[1]+3)] in pos):
        array.remove('d')

    if(len(array) == 0):
        nxt = 'a'
        cpos = stack[-1]
        stack = stack[:-1]
    else:
        visited = visited + 1
        nxt = random.choice(array)


    #nxt = input()

    if(nxt == 'u'):
        cpos[1] -= 3
        tab = printPos(tab,cpos[0],cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1]+2," ",x,y)

    if(nxt == 'l'):
        cpos[0] -= 3
        tab = printPos(tab,cpos[0],cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+1," ",x,y)

    if(nxt == 'r'):
        cpos[0] += 3
        tab = printPos(tab,cpos[0],cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+1," ",x,y)

    if(nxt == 'd'):
        cpos[1] += 3
        tab = printPos(tab,cpos[0],cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0],cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1],charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+1,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+2,cpos[1]+2,charToPrint,x,y)
        tab = printPos(tab,cpos[0]+1,cpos[1]," ",x,y)

    if(nxt != 'a'):
        if([int(cpos[0]-3),cpos[1]] in pos and nxt == 'r'):
            tab = printPos(tab,cpos[0]-1,cpos[1]+1," ",x,y)

        if([cpos[0],int(cpos[1]-3)] in pos and nxt == 'd'):
            tab = printPos(tab,cpos[0]+1,cpos[1]-1," ",x,y)

        if([int(cpos[0]+3),cpos[1]] in pos and nxt == 'l'):
            tab = printPos(tab,cpos[0]+3,cpos[1]+1," ",x,y)

        if([cpos[0],int(cpos[1]+3)] in pos and nxt == 'u'):
            tab = printPos(tab,cpos[0]+1,cpos[1]+3," ",x,y)
        pos.append([cpos[0],cpos[1]])
        stack.append([cpos[0],cpos[1]])

    tab = printPos(tab,cpos[0]+1,cpos[1]+1,"0",x,y)
    if(displayConstruct):
        print("\n"*5)
        print(tab)
    else:
        a =10 * visited/((x+1)*(y+1))
        if(a > .1 * current):
            print("|" + ("="*int(a*10) + "-"*10)[:10] + "|")
            current+=1
    tab = tab.replace('0',' ')
    condition = (cpos != [0,0])
cpos[0] +=1
cpos[1] +=1
goal = random.choice(pos)
goal[0] += 1
goal[1] += 1
tab = printPos(tab,cpos[0],cpos[1],"0",x,y)
tab = printPos(tab,goal[0],goal[1],"+",x,y)
print("\n"*5)

print(tab)
condit = True

while condit:
    mv = getkey()
    if(mv == 'w' and getTabPos(tab,cpos[0],cpos[1] - 1,x,y) != charToPrint):
        tab = printPos(tab,cpos[0],cpos[1]," ",x,y)
        cpos[1] -= 1
        tab = printPos(tab,cpos[0],cpos[1],"0",x,y)
    if(mv == 'a' and getTabPos(tab,cpos[0]-1,cpos[1] ,x,y) != charToPrint):
        tab = printPos(tab,cpos[0],cpos[1]," ",x,y)
        cpos[0] -= 1
        tab = printPos(tab,cpos[0],cpos[1],"0",x,y)
    if(mv == 's' and getTabPos(tab,cpos[0],cpos[1] + 1,x,y) != charToPrint):
        tab = printPos(tab,cpos[0],cpos[1]," ",x,y)
        cpos[1] += 1
        tab = printPos(tab,cpos[0],cpos[1],"0",x,y)
    if(mv == 'd' and getTabPos(tab,cpos[0] + 1,cpos[1] ,x,y) != charToPrint):
        tab = printPos(tab,cpos[0],cpos[1]," ",x,y)
        cpos[0] += 1
        tab = printPos(tab,cpos[0],cpos[1],"0",x,y)
    if(cpos == goal):
        condit = False
    print("\n"*5)
    print(tab)
print("You've reached the goal!!")
input()
