# # Single inheitance
# # class parent:
# #     def house (self):
# #         print ("Parent has house")

# # class Child (parent):
# #     def car (Self):
# #         print("son has a car")

# # c = Child()
# # c.house ()  

# #Multilevel Inheritance       

# # class parent1:
# #     def house (self):
# #         print ("parent1 has house")
# # class parent2 (parent1):
# #     def land (self):
# #         print("parent2 has land")
# # class child (parent2):
# #     def car (self):
# #         print ("son has car")

# # c = child()
# # c.car()

# #Multiple inheritance
# # class parent1:
# #     def house (self):
# #         print ("parent1 has house")
# # class parent2 (parent1):
# #     def land (self):
# #         print("parent2 has land")
# # class child (parent2):
# #     def car (self):
# #         print ("son has car")

# # c = child()
# # c.car()
# # c.land()
# # c.house()

# # hybrid inheritance

# class Grandparent:
#     def land(self):
#         print("Grandparent has land")

# class Parent1(Grandparent):
#     def house(self):
#         print("Parent1 has house")

# class Parent2:
#     def business(self):
#         print("Parent2 runs business")

# class Child(Parent1, Parent2):
#     def car(self):
#         print("Child has car")

# # c = Child()
# # c.land()
# # c.house()
# # c.business()
# # c.car()

# # # Hirechical Inheritance

# # Parent class (Bank Branch Head Office)
# class HeadOffice:
#     def policy(self):
#         print("Head Office defines policies")

# # Child classes (different branches)
# class BranchSurat(HeadOffice):
#     def services(self):
#         print("Surat Branch provides loan services")

# class BranchMumbai(HeadOffice):
#     def services(self):
#         print("Mumbai Branch provides investment services")

# class BranchDelhi(HeadOffice):
#     def services(self):
#         print("Delhi Branch provides insurance services")

# # Object creation
# s = BranchSurat()
# m = BranchMumbai()
# d = BranchDelhi()

# # Method calls
# s.policy()
# s.services()

# m.policy()
# # m.services()

# # d.policy()
# # d.services()

# class Calculator:
#     def add (self, *arg):
#         return sum (arg)
# obj = Calculator()

# print (obj. add (10, 20)) 
# print (obj.add (10, 20, 30, 40, 50))

class Math:
    def study(self):
        print("We have to practice math")

class Physics:   # Class names usually start with capital letters
    def study(self):
        print("We have to learn physics")

p = Math()
p.study()   # <-- add parentheses to actually call the method
