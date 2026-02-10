import os

def histogram(fin):  
    hist = dict()
    # Read every line in fin
    for line in fin:
        # Split() the line into a list of words
        words = line.split()
        
        # Process every word in the list
        for word in words:
            # Convert each word to lower case 
            word = word.lower()
            
            # Check if each word is in the dictionary
            if word in hist:
                # If it is, increment its count
                hist[word] += 1
            # If not, add it with a count of 1
            else:
                hist[word] = 1
                
    return hist


def printHistogram(hist):
    print("Word       Count")
    print("----------------")
    # Loop through every key (word) in the dictionary [cite: 12]
    for word in hist:
        # Print the word and its corresponding count
        print(f"{word:<12}{hist[word]:2d}")

filename= 'Myra.txt'
if not os.path.isfile(filename):
    print(f"Error: {filename} not found.")
else:
    with open(filename) as fin:
        hist = histogram(fin)
        printHistogram(hist)

