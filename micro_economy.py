#Model of the economy
import random as rand

#State variables people

#Types of componets of economy

class econ:
    def __init__(self,label,P,G):
        self.label = label
        self.P = P
        self.G = G
        self._time = 0
        self._av_money = 0
        self._av_profit = 0
        self._gdp = 0
    def __str__(self):
        return '{}'.format(self.label)

    def get_owners(self):
        O = []
        for people in self.P:
            if isinstance(people, owner):
                O.append(people)
        return O
    def get_workers(self):
        W = []
        for people in self.P:
            if isinstance(people, worker):
                W.append(people)
        return W
    def total_spending(self):
        sum = 0
        for people in self.P:
            sum += people.spent
        return int(sum)
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self,year):
        self._time = year
    @property
    def av_money(self):
        sum = 0
        for person in self.P:
            sum += person.money
        return int(sum/len(self.P))
    @property
    def av_profit(self):
        sum = 0
        for comp in self.G:
            sum += comp.profit
        return int(sum/len(self.G))
    

    @property
    def gdp(self):
        sum = 0
        for person in self.P:
            sum += person.salary
        for comp in self.G:
            sum += comp.profit
        return int(sum)
    def forecast(self,year) :
        a = 0.50/len(self.get_owners())
        b = 0.25/len(self.get_workers())
        c = 0.25
        for time in range(self._time,year):
            #shuffle list of companies
            set = self.G.copy()
            rand.shuffle(set)
            for group in self.G:
                # Amount of G+S on offer by company
                GS = group.prod
                P_money = []
                for person in self.P:
                    P_money.append(person._money)
                    # prob person buy and % of G+S the person will buy
                    r = rand.random()
                    #People get paid by their company and buy G+S from other company
                    if  group.ID != person.ID:
                        if person.money*0.01 >  GS*r:
                            person.money -= GS*r
                            GS -= GS*r
                #Profit made
                profit = group.prod - GS
                i = 0
                for person in self.P:
                    person.spent = int(P_money[i] - person.money)
                    i += 1
                    if group.ID == person.ID:
                        if isinstance(person,owner):
                            person.salary = profit*a 
                            person.money += profit*a
                        elif isinstance(person,worker):
                            person.salary = group.val*b
                            person.money += group.val*b
                group.val += profit*c 
                group.profit = int(profit)
        self.time = year


class comp:
    def __init__(self,label,val):
        self.ID = id(self)
        self.label = label
        self.val = val
        self.prod = self.val/10
        self.profit = 0
        @property
        def prod(self):
            return self.val/10
        
        @prod.setter
        def prod(self,appreciation):
            self.prod = appreciation
            
        @property
        def val(self):
            return self.val
        @val.setter
        def val(self,nw_val):
            self.val = nw_val
        @property
        def profit(self):
            return self.profit

        @profit.setter
        def profit(self,profit):
            self.profit = profit
    def __str__(self):
        return '{}'.format(self)
class worker:
    def __init__(self,money,comp):
        self.ID = id(comp)
        self.comp = comp
        self._money = money
        self._salary = 0
        self._spent = 0
        self.assets = 0
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,change):
        self._salary = change
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self,change):
        self._money = change
    @property
    def spent(self):
        return self._spent
    @spent.setter
    def spent(self,nw_spent):
        self._spent = nw_spent
    def __str__(self):
        return '{}'.format(self)

class owner:
    def __init__(self,money,assets,comp):
        self.ID = id(comp)
        self.comp = comp
        self.assets = assets
        self._money = money
        self._salary = 0
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,change):
        self._salary = change
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self,change):
        self._money = change
    @property
    def spent(self):
        return self._spent
    @spent.setter
    def spent(self,nw_spent):
        self._spent = nw_spent

    def __str__(self):
        return '{}'.format(self)

def CrePop(O,W,compLabels):
    f = open('c:\\Users\\Sena\\Documents\\Python Scripts\\vmpy\\population.txt','w')
    
    #print('Comp', file=f)
    for i in range(16):
        t= i +1
        val = 60000 + -1*(t % 4)*3000
        print("G{} {} {}".format(i,compLabels[i],val),file=f)
    print('',file=f)

    total = O+W
    for i in range(total):
        t = i +1
        j = rand.randint(0,len(compLabels))
        a = 500*t
        if i <= O:   
            b = 550*t
            print("p{} {} {} G{}".format(i,b,a,j),file=f)
        else:
            
            print("p{} {} G{}".format(i,a,j),file=f)
    f.close()
    

def readPop(compLabels):
    G = []
    P = []
    with open('c:\\Users\\Sena\\Documents\\Python Scripts\\vmpy\\population.txt','r') as f:
        lines = f.readlines()
    
    i = 0
    L = len(compLabels)
    
    for line in lines:
        if len(line.split()) == 0:
            i+=1
            break
        else:
    
            #print(len(line.split()))
            #print(i,'Line length: {}'.format(len(line)))
            #i = (j % L)+1
            l = line.split()
            l[0] = comp(l[1],int(l[2]))
            G.append(l[0])
        i+=1

    for line in lines[i:]:
        l = line.split()
        if len(l) == 4:
            l[0] = owner(int(l[1]),int(l[2]),l[3])
            P.append(l[0])
        elif len(l) == 3:
            l[0] = worker(int(l[1]),l[2])
            P.append(l[0])
    return P,G


def main():
    compLabels = ['Woolworths','Napster','Myspace','AOL','Blockbuster','Smyths','IBM','Verizon','AT&T','Comcast','Apple','Sony','Disney','Netflix','Amazon','Google']
    #CrePop(20,50,compLabels)
    P,G = readPop(compLabels)

    UK = econ('UK',P,G)
    
    with open('c:\\Users\\Sena\\Documents\\Python Scripts\\vmpy\\GDP.txt','w') as f:
        print('{} {:>10} {:>10} {:>10}'.format('Time','GDP', 'Average money','Average profit'), file=f)
        for i in range(100):        
            UK.forecast(i)
            print('{} {:>15} {:>15} {:>15}'.format(i,UK.gdp, UK.av_money, UK.av_profit), file=f)
        pass


if __name__ == "__main__":
    main()





