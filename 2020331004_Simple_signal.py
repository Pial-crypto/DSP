import matplotlib.pyplot as plt

# Parameters
total_duration = 10  # Total time duration (samples)
sample_rate = 1      # Samples per unit time
total_points = total_duration * sample_rate  # Total number of points

# Generate signals
signal_impulse = [1 if i == 0 else 0 for i in range(total_points)]  # Impulse at n = 0
signal_step = [1 if i >= 0 else 0 for i in range(total_points)]     # Step from n = 0
signal_ramp = [i if i >= 0 else 0 for i in range(total_points)]     # Ramp from n = 0

# Time axis
time_axis = list(range(total_points))

# Plot signals
plt.figure(figsize=(12, 8))

# Plot unit impulse
plt.subplot(3, 1, 1)
plt.stem(time_axis, signal_impulse, basefmt=" ", use_line_collection=True)
plt.title("Unit Impulse Signal")
plt.xlabel("Time (n)")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot unit step
plt.subplot(3, 1, 2)
plt.stem(time_axis, signal_step, basefmt=" ", use_line_collection=True)
plt.title("Unit Step Signal")
plt.xlabel("Time (n)")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot unit ramp
plt.subplot(3, 1, 3)
plt.stem(time_axis, signal_ramp, basefmt=" ", use_line_collection=True)
plt.title("Unit Ramp Signal")
plt.xlabel("Time (n)")
plt.ylabel("Amplitude")
plt.grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
