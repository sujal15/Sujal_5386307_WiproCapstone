from oopsconcept.demoA import A
from oopsconcept.demoB import B

class C(A,B):
    def __init__(self,n1,n2,msg):
        A.__init__(self, n1,n2)
        super().__init__(self, msg)


    def final(self):
        print('Done')

