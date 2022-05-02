class Sources:
	'''
	Source Class to define Source Objects
	'''
	def __init__(self,id,name,description,url,category):
		'''
		Function to initialize Source Objects
		It defines the properties each Source object will hold.
		'''
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category
    