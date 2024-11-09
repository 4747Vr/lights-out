from random import randint

class Frontend:
    def __init__(self, liste):
        self.liste = liste
    def output(self):
        print ("1 2 3 4 5")
        for i in range(0, 25, 5):
            for v in range (5):
                print("# " if self.liste[i + v] == 1 else "  ", end="")
            print(int((i + 5) / 5))

class ChangeList:
    def __init__(self):
        self.liste = [0 for i in range(25)]
        
 
    def list_refresh(self, ntc):
        li = self.liste
        chli = []
        ntc -= 1
        if ntc >= 0 and ntc <= 24:
            chli.append(ntc)
            if ntc > 4:
                chli.append(ntc - 5)
            if ntc < 20:
                chli.append(ntc + 5)
            if ntc % 5 != 0:
                chli.append(ntc - 1)
            if (ntc + 1) % 5 != 0:
                chli.append(ntc + 1)
        for a in chli:
            if li[int(a)] == 0:
                li[int(a)] = 1  
            else:
                li[int(a)] = 0
        self.liste = li
    
    def program(self):
        for i in range(25):
            if randint(0,1) == 1:
                self.list_refresh(i+1)
        Frontend(self.liste).output()
        while self.liste != [0 for i in range(25)]:
            change = 0
            while not 0 < change < 26:
                try:
                    change = int(input('enter xy: '))
                except ValueError:
                    change = 111
                if not 0 < change % 10 < 6 or not 0 < int(change / 10) < 6:
                    change = 11111
                    print("Wrong Syntax, try again")
                change = int(change / 10) + ((change % 10) - 1) * 5
            self.list_refresh(change)
            Frontend(self.liste).output()
        print("Congratulations, you did it")

ChangeList().program()