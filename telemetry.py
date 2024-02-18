import pandas as pd
import matplotlib.pyplot as plt

# Assume you have a CSV file 'telemetry.csv' with columns 'time', 'altitude', 'velocity'
data = pd.read_csv('telemetry.csv')

# Plot altitude over time
plt.figure(figsize=(10, 5))
plt.plot(data['time'], data['altitude'])
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Altitude over Time')
plt.grid(True)
plt.show()

# Plot velocity over time
plt.figure(figsize=(10, 5))
plt.plot(data['time'], data['velocity'])
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity over Time')
plt.grid(True)
plt.show()
