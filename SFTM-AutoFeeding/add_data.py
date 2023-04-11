import csv
import random

# Open the CSV file for appending
with open('fish_autofeeding.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(["day_of_week", "time_of_day",
                    "temperature", "light", "prediction"])

    # Generate 100 new rows
    for i in range(1000):
        # Generate random values for each column
        day_of_week = random.choice(
            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        h = random.randint(0, 23)
        m = random.randint(0, 59)
        time_of_day = f"{h}:{m}"
        temperature = random.randint(0, 35)
        light = random.choice(['low', 'medium', 'high'])
        prediction = True if (5 <= h < 8 or 11 <= h < 13 or 17 <= h < 19) and (
            light in ['medium', 'high']) and (20 <= temperature <= 30) else False

        # Write the new row to the CSV file
        writer.writerow([day_of_week, time_of_day,
                        temperature, light, prediction])
