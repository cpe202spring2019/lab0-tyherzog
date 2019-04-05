def weight_on_planets():
   # write your code here
   person_weight = input('What do you weigh on earth? ') #asks user for their weight
   person_weight = int(person_weight) #casts the string into an integer
   print ("\nOn Mars you would weigh", (person_weight*.38), "pounds.\nOn Jupiter you would weigh", (person_weight*2.34), "pounds.") #Prints various weights for different planets
if __name__ == '__main__': #When called will run function
   weight_on_planets()
