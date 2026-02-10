#Write a program that takes as input how many hours and minutes a person worked in a day. Then call a function that calculates (and returns) how many seconds they worked

def calculate_seconds(hours, minutes):
    total_seconds = (hours * 3600) + (minutes * 60)
    return total_seconds
def main():
    hours = int(input("Enter the number of hours worked: "))
    minutes = int(input("Enter the number of minutes worked: "))
    seconds = calculate_seconds(hours, minutes)
    print(f"You worked a total of {seconds} seconds.")

main()

    