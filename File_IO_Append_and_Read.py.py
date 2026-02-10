# Open players.txt in append mode ('a') to add new players. [cite: 4, 6]
    outfile = open('players.txt', 'a')

    print("Enter data for three additional players:")
    # Loop three times to get input for three players. [cite: 7]
    for i in range(3):
        print(f"\n--- Player {i + 1} ---")
        number = input("Enter player's number: ")
        name = input("Enter player's name: ")
        hrs = input("Enter home runs: ")

        # Write the player's data as a new line in the file. [cite: 8]
        outfile.write(f"{number} {name}  {hrs}\n")

    # Close the file to ensure the data is saved. [cite: 9]
    outfile.close()
    print("\nSuccessfully added 3 players to players.txt.")
    print("==========================================")

    # --- PART 2: Reading and printing the file ---

    print("\nReading all data from players.txt:\n")
    # Reopen the file, this time in read mode ('r'). [cite: 10]
    infile = open('players.txt', 'r')

    # Read and print each line from the file. [cite: 11]
    for line in infile:
        # .strip() removes any leading/trailing whitespace, including the newline character.
        print(line.strip())

    # Close the file after you are done reading from it.
    infile.close()

main()