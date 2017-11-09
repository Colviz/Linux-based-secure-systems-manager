with open('output','r') as f: #File opening in read mode
    next(f) #Going to the next line (skipping the header row)
    for line in f: #Fetching content line by line
        print(line.split(' ')[0]) #Prints the first word of line