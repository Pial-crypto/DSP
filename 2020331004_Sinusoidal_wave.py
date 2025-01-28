import math
import matplotlib.pyplot as plt

# Parameters for the sinusoidal wave
wave_amplitude = 1.0    # Amplitude of the wave
wave_frequency = 5.0    # Frequency in Hertz
wave_phase = 0.0        # Phase shift in radians
wave_duration = 2.0     # Duration of the wave in seconds
wave_sample_rate = 1000 # Samples per second

# Calculate the time step and number of points
step_time = 1 / wave_sample_rate
total_points = int(wave_sample_rate * wave_duration)

# Generate the time and wave values
time_values = []
wave_values = []

for index in range(total_points):
    current_time = index * step_time
    time_values.append(current_time)
    value_wave = wave_amplitude * math.sin(2 * math.pi * wave_frequency * current_time + wave_phase)
    wave_values.append(value_wave)

# Plot the sinusoidal wave
plt.figure(figsize=(10, 4))
plt.plot(time_values, wave_values, label=f'{wave_frequency} Hz Sine Wave')
plt.title('Sinusoidal Wave (Manual Calculation)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
