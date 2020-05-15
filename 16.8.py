'''
Inteager to English
input: 1,000
output: One Thousand
'''

f = open('input.txt','r')

integer = f.readline()

Hundredlist = ['Hundred','ty','']
numlist = ['Thousand','Million','Billion']
numinEng = dict({1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'})
numinEng_ty = dict({2:'Twen', 3:'Thir', 4:'Four', 5:'Fif',6:'Six',7:'Seven',8:'Eight',9:'Nine'})
numinEng_ten = dict({10: 'Ten', 11:'Eleven', 12: 'Twelve'})


def HundredPart(intg):
    if len(intg) < 3:
        intg = '0'*(3-len(intg))+intg

    check = False

    for i in range(3):
        digit = int(intg[i])
        if digit:
            check = True
            if i == 1:
                last = int(intg[i+1])
                if digit == 1:
                    if digit*10+last in numinEng_ten:
                        print(numinEng_ten[digit*10+last], end = ' ')
                    else:
                        print(numinEng_ty[last]+ 'teen', end=' ')
                    break

                else:
                    print(numinEng_ty[digit]+'ty', end=' ')
            else:
                print(numinEng[digit], end = ' ')
                if i < 2: print(Hundredlist[i], end = ' ')

    return check


remain = len(integer)%3
totalsize = len(integer)//3
if remain:
    HundredPart(integer[:remain])
    if totalsize > 0: print(numlist[totalsize-1], end=' ')

for i in range(totalsize):
    check = HundredPart(integer[remain+i*3:remain+(i+1)*3])
    if totalsize - i - 2 >= 0 and check: print(numlist[totalsize - i - 2], end=' ')


