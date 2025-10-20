import random
import statistics
from datetime import datetime


randomTemp = random.randint(-5,35)
print(randomTemp)

readings = []

for i in range(4):
    readings.append(random.randint(-5,35))

print(readings)

date_today = datetime.now()
print(date_today)

average = statistics.mean(readings)
minimum = min(readings)
maximum = max(readings)

print(average, minimum, maximum)