# Baseball players program - appending and reading data

def main():
    # Open the output file in append mode
    outfile = open("players.txt", "a")

    # Ask for information about 8 additional players
    for count in range(8):
        number = int(input("Enter the player number: "))
        name = input("Enter the player name: ")
        hrs = int(input("How many home runs did he hit: "))


        # Store each player's data in the output file
        outfile.write(f"{number:2d} {name} {hrs:2d}\n")

    # Close the output file
    outfile.close()

    # Reopen the file for input (reading)
    infile = open("players.txt", "r")

    print("\nUpdated Player List:")
    # Print out the data for each player
    for line in infile:
        print(line.strip())

    # Close the input file
    infile.close()


main()

