
class human:
    def log(self):
        print(self)

class footballer(human):
    def __init__(self,name,goalScored,):
        self.goalScored = goalScored
        self.name = name
    
    def liveScore():
        print("Live Score = 3 : 2" )

    def __str__(self) : #This string function has to return a string
        return self.name + " Goal scored is " + str(self.goalScored)
    
    def __eq__(self, other):
        if self.name == other.name :
            return True
        else :
            return False

    __repr__ = __str__

f1 = footballer("Ronaldo",10)
print(f1.name)
f2 = footballer("Messi",9)
print(f2.name)

f = [f1,f2]

#Calling a function not tied to an obj
footballer.liveScore()

#Testing __str__
print(f1)

#testing __eq__
print(f1 == f2)

print(f)

print("inheritance print")
f2.log()