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
    def gdp(self):
        sum = 0
        for person in self.P:
            sum += person.money
        for comp in self.G:
            sum += comp.val
        return int(sum)
    def forecast(self,year) :
        a = 0.50/len(self.get_owners())
        b = 0.25/len(self.get_workers())
        c = 0.25
        for time in range(self._time,year):
            #shuffle list of companies
            rand.shuffle(self.G)
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
                        if person.money >  GS*r:
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
                            person.money += profit*a
                        elif isinstance(person,worker):
                            person.money += profit*b
                group.val += profit*c 
        self.time = year


class comp:
    def __init__(self,label,val):
        self.ID = id(self)
        self.label = label
        self.val = val
        self.prod = self.val/10
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

    def __str__(self):
        return '{}'.format(self)
class worker:
    def __init__(self,money,comp):
        self.ID = id(comp)
        self._money = money
        self._spent = 0
        self.assets = 0
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
        self.assets = assets
        self._money = money
        self._spent = 0
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

#proportion of profits from G+S made by each party
a = 0.75
b = 0.125  

def CrePop():
    f = open('c:\\Users\\Sena\\Documents\\Python Scripts\\vmpy\\text.txt','w')
    name = ['Woolworths','Napster','Myspace','AOL','Blockbuster','Smyths','IBM','Verizon','AT&T','Comcast','Apple','Sony','Disney','Netflix','Amazon','Google']
    print('Comp', file=f)
    for i in range(16):
        t = i+1
        val = 5000*t
        print('G{} {} {}'.format(t,name[i],val),file=f)

    print('\n','Population', file=f)
    for i in range(50):
        t = i+1
        a = 500*t
        if i <= 20:   
            b = 550*t
            print('p{} {} {}'.format(t,b,a),file=f)
        else:
            print('p{} {}'.format(t,a),file=f)
    print('Done!')
    f.close()

def main():
    G1 = comp('Amazon',50000)
    p1 = owner(50000,10000,G1)
    p2,p3 = worker(5000,G1), worker(3000,G1)

    G2 = comp('Apple',100000)
    p4 = owner(30000,5000,G2)
    p5, p6 = worker(2500,G2), worker(5750,G2)

    G3 = comp('Google',700000)
    p7,p8 = owner(50000,1000,G3), owner(15000,4000,G3)
    p9, p10, p11, p12 = worker(5000,G3), worker(7250,G3), worker(6000,G3), worker(3000,G3)

    P = []
    G = [G1,G2,G3]
    Pi = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
    UK = econ('UK',Pi,G)
    
    for i in range(10):        
        UK.forecast(i)
        #print('the year is {}'.format(UK.time)) 
        #print('{} value in year {} is '.format(G2.label,i),G2.val)
        print('Total spending is {}'.format(UK.total_spending()))
        pass


if __name__ == "__main__":
    main()





