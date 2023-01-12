# Park Run Timer

print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")

total_runners = 0
total_time = 0
fastest_time = None
slowest_time = None
fastest_runner = None

while True:                           # To END the runner program using 'END' keyword
    line = input()
    if line.upper() == "END":
        break

    # Split the line into runner number and time
    parts = line.split("::") 
    if len(parts) != 2:
        print("Error in data stream. Ignorning. Carry on.")
        continue

    # Get the runner number and time
    runner_number = parts[0]
    time = parts[1]

    # Check if the time is a valid number
    if not time.isdigit():
        print("Error in data stream. Ignorning. Carry on.")
        continue

    # Convert the time to an integer
    time = int(time)

    # Update the statistics
    total_runners += 1
    total_time += time
    if fastest_time is None or time < fastest_time:
        fastest_time = time
        fastest_runner = runner_number
    if slowest_time is None or time > slowest_time:
        slowest_time = time

# Calculate the average time
average_time = total_time / total_runners

# Convert the times to minutes and seconds


def to_minutes_seconds(time):
    minutes = time // 60
    seconds = time % 60
    return f"{minutes} minutes, {seconds} seconds"


fastest_time = to_minutes_seconds(fastest_time)
slowest_time = to_minutes_seconds(slowest_time)
average_time = to_minutes_seconds(average_time)

# Print the results
print(f"Total Runners: {total_runners}")
print(f"Average Time:  {average_time}")
print(f"Fastest Time:  {fastest_time}")
print(f"Slowest Time:  {slowest_time}")
print(f"\nBest Time Here: Runner #{fastest_runner}")
