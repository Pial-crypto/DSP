import matplotlib.pyplot as plt

def basic_convolution(signal_x, signal_h):
    len_x = len(signal_x)
    len_h = len(signal_h)
    len_result = len_x + len_h - 1
    result_y = [0] * len_result
    for n in range(len_result):
        for k in range(len_h):
            if 0 <= n - k < len_x:
                result_y[n] += signal_x[n - k] * signal_h[k]
    return result_y

# Get user input for signals
signal_x = list(map(float, input("Enter the input signal x[n] (comma-separated): ").split(',')))
signal_h = list(map(float, input("Enter the impulse response h[n] (comma-separated): ").split(',')))

# Perform convolution
result_y = basic_convolution(signal_x, signal_h)

# Print results
print("\nInput Signal x[n]:", signal_x)
print("Impulse Response h[n]:", signal_h)
print("Convolution Result y[n]:", result_y)

# Create plots
plt.figure(figsize=(12, 8))

# Plot input signal x[n]
plt.subplot(3, 1, 1)
plt.stem(range(len(signal_x)), signal_x, basefmt=" ", use_line_collection=True)
plt.title("Input Signal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Plot impulse response h[n]
plt.subplot(3, 1, 2)
plt.stem(range(len(signal_h)), signal_h, basefmt=" ", use_line_collection=True)
plt.title("Impulse Response h[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Plot convolution result y[n]
plt.subplot(3, 1, 3)
plt.stem(range(len(result_y)), result_y, basefmt=" ", use_line_collection=True)
plt.title("Convolution Result y[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Show plots
plt.tight_layout()
plt.show()
