#This program
#will print hello
#world

#this function tells the 
#computer to print 
#"Hello World"
def PrintHelloWorld ():
	print ("HelloWorld")

	#This defines our main ()
	#function for our program
	def main ():
		PrintHelloWorld()

		#When we run the program 
		#this executed first
		if __name__== "__main__":
			main ()