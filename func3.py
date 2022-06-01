class A:
    a = 'A'
    def __init__(self,name):
        self.name=name

    def getname(self):
        print("Name:",self.name)
        print("Called from class",self.a)    

class B:
    b = 'B'
    def __init__(self,name):
        self.name=name

    def getname(self):
        print("Name:",self.name)
        print("Called From class",self.b)    

class C(B,A):
#class C(A,B):  
    pass

obj = C("Nilay")
obj.getname()