class Person:
    def __init__(self,FirstName,LastName) :
        self.FirstName=FirstName
        self.LastName=LastName
    def fullname(self):
        return f"{self.FirstName} {self.LastName}"
class employee(Person):
    salery=3000
    def __init__(self, FirstName, LastName,posetion):
        super().__init__(FirstName, LastName)        
        self.posetion=posetion
    def pos(selfe):
        return f"Im {selfe.fullname()} and my pos is {selfe.posetion}"
emp1=employee('ali',"bigdeli","programer")
print(emp1.pos())