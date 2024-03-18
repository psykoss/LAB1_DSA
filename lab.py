from dlist import DList
from dlist import DNode
class Patient:
	"""Class to represent a Patient"""
	def __init__(self,name,year,vaccine):
		self.name=name
		self.year=year #Birth year (for example, 1974)
		self.vaccine=vaccine #1 or 0 (Yes or no)
class HealthCenter(DList):
"""Class to represent a Health Center"""
	def addPatient(self,patient):
		pass
	def searchPatients(self,year,vaccine=None):
		pass
	def minus(self,other):
		pass
if __name__ == '__main__':
	
