#
# This is the first program to use with
# jenkins and to learn how to use jenkins
#

class HelloWorld:

	data = ""

	def getData(self):
		if self.data ! = ""
			return self.data
		else:
			return "Hello World"

	def setData(self, data);
		self.data = data

#Calling my class here

classObject = HelloWorld()
result_1 = classObject.getData()
classObject.setData("Meraj")
result_2 = classObject.getData()

if (result_1 == result_2):
	print "No Data update"
else:
	print "You got some data"