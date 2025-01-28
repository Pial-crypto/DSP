import math
import matplotlib.pyplot as plt

# Parameters for the signal
amplitude = 1         # Amplitude of the sine wave
frequency = 1         # Frequency in Hz
samples = 100         # Number of time samples
t_start = 0           # Start time in seconds
t_end = 2             # End time in seconds (2 full cycles for 1 Hz)

# Generate time values
time_vals = [t_start + i * (t_end - t_start) / (samples - 1) for i in range(samples)]

# Signal components:
# 1. Sine wave: A * sin(2*pi*f*t)
sine_wave = [amplitude * math.sin(2 * math.pi * frequency * t) for t in time_vals]

# 2. Unit step function: u[n]
step_function = [1 if t >= 0 else 0 for t in time_vals]

# 3. Unit impulse function: delta[n] (simulated as a spike at t = 0)
impulse_function = [1 if t == 0 else 0 for t in time_vals]

# Composite signal: sum of all components
final_signal = [sine_wave[i] + step_function[i] + impulse_function[i] for i in range(samples)]

# Plotting the composite signal
plt.figure(figsize=(10, 6))

# Plot the composite signal
plt.plot(time_vals, final_signal, label='Final Signal (Sine + Step + Impulse)', color='blue')
plt.title('Final Signal (Sum of Sine Wave, Step, and Impulse)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.show()
