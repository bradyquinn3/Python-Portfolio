import random  # Import the random module to generate random numbers

class Dice:
    """
    A class to represent a single Die with a face value between 1 and 6.
    """

    def __init__(self):
        """
        The initializer method.
        Sets the default faceValue to 1 when a new Dice object is created.
        """
        self.faceValue = 1

    def roll(self):
        """
        Generates a random number between 1 and 6 and updates faceValue.
        """
        # randint includes both endpoints (1 and 6)
        self.faceValue = random.randint(1, 6)

    def getFaceValue(self):
        """
        Returns the current value of faceValue.
        """
        return self.faceValue

def main():
    """
    Main function to execute the program logic.
    """
    print("--- Rolling the Dice ---")

    # 1. Create 2 dice objects
    die1 = Dice()
    die2 = Dice()

    # 2. Call the roll() method for each object
    die1.roll()
    die2.roll()

    # 3. Call getFaceValue() for each object to retrieve the numbers
    num1 = die1.getFaceValue()
    num2 = die2.getFaceValue()

    # 4. Add the two rolls together and display the results
    total = num1 + num2

    print(f"Die 1 rolled: {num1}")
    print(f"Die 2 rolled: {num2}")
    print("-" * 20)
    print(f"Total score:  {total}")

# Standard boilerplate to call the main() function when the script is executed
if __name__ == "__main__":
    main()
