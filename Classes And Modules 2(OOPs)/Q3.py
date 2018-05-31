# Q3.

class Cop:
	def __init__(self):
		self.name='abc'
		self.age=20
		self.workexp=5
		self.desig='CBI'

	def addDetails(self,name,age,workexp,desig):
		self.name=name
		self.age=age
		self.workexp=workexp
		self.desig=desig

	def Display(self):
		print("Cop Details Are:")
		print("Name of the Cop: ",self.name)
		print("Age of the Cop: ",self.age)
		print("Work Experience of the Cop: ",self.workexp)
		print("Designation of the Cop: ",self.desig)


class Mission(Cop):
	basicObjective='To Protect and defend the United States against Terrorist and Foreign Intelligence Threats'
	def add_mission_details(self):
		print("Mission Details: ")
		print(self.basicObjective)

m1=Mission()
name=input("Enter Name Of Cop: ")
age=int(input("Enter Age Of Cop: "))
workexp=int(input("Enter Work Experience Of Cop: "))
desig=input("Enter Designation Of Cop: ")
m1.addDetails(name,age,workexp,desig)

m1.Display()
m1. add_mission_details()

'''
OUTPUT:
Enter Name Of Cop: Charlie
Enter Age Of Cop: 28
Enter Work Experience Of Cop: 5
Enter Designation Of Cop: Commando
Cop Details Are:
Name of the Cop:  Charlie
Age of the Cop:  28
Work Experience of the Cop:  5
Designation of the Cop:  Commando
Mission Details: 
To Protect and defend the United States against Terrorist and Foreign Intelligence Threats
'''