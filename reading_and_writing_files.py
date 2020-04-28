def create_cast_list(filename): #Defining the function
    cast_list = [] #Create an empty list
    #use with to open the file filename
    with open('C:/Users/radio/Desktop/ANDRÉS R. BUCHELI - SOFTWARE ENGINEER/COMPUTER SCIENCE/INTRODUCTION TO PYTHON PROGRAMMING/flying_circus_cast.txt') as f:
    #use the for loop syntax to process each line
        for line in f:
            name = line.split(",")[0]
    #and add the actor name to cast_list
            cast_list.append(name) #adding elements to the list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt') #calling the function 
for actor in cast_list: #Loop through the cast_list to extract the name of the actor and print it.
    print(actor)