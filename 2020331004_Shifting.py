import numpy as np
import matplotlib.pyplot as plt

# Given discrete-time signal signal_x[n] and time samples time_t[n]
signal_x = np.array([2, 3, 0, 2, 1, 3, 1, 1])
time_t = np.array([3, -2, 1, 0, 1, 1, 3, 2])

# Shift operations
delay_x = []  # delayed_x[n] = signal_x[n-1]
for i in range(1, len(signal_x)):
    delay_x.append(signal_x[i - 1])

advance_x = []  # advanced_x[n] = signal_x[n+1]
for i in range(0, len(signal_x) - 1):
    advance_x.append(signal_x[i + 1])

# Plotting the Unit Delay and Unit Advance operations
plt.figure(figsize=(10, 6))

# Plotting the Unit Delay system
plt.subplot(2, 1, 1)
plt.stem(time_t[1:], delay_x, basefmt=" ")
plt.title('Unit Delay System (signal_x[n-1])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotting the Unit Advance system
plt.subplot(2, 1, 2)
plt.stem(time_t[:-1], advance_x, basefmt=" ")
plt.title('Unit Advance System (signal_x[n+1])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
