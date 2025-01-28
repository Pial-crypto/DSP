import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def record_audio(duration_sec=5, sample_rate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration_sec * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    print("Recording complete.")
    return audio_data.flatten()  # Convert to 1D array

def audio_to_binary(samples, bit_depth=16):
    # Normalize the audio samples to the range [0, 1] (assuming input range is [-1, 1])
    normalized_samples = np.clip(samples, -1, 1)  # Clamp values to valid range
    scaled_samples = ((normalized_samples + 1) * (2**(bit_depth - 1) - 1)).astype(int)  # Scale to integer range

    # Convert scaled samples to binary format (as strings of bits)
    binary_samples = np.array([f"{value:0{bit_depth}b}" for value in scaled_samples])

    return binary_samples

def plot_audio_and_binary(audio_data, sample_rate=44100, bit_depth=8):
    # Time axis for the audio signal
    time_axis = np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data))

    # Create plots
    plt.figure(figsize=(12, 8))

    # Plot the audio signal
    plt.subplot(2, 1, 1)
    plt.plot(time_axis, audio_data, label='Audio Signal', color='blue')
    plt.title('Audio Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Convert audio data to binary format
    binary_data = audio_to_binary(audio_data, bit_depth=bit_depth)

    # Plot binary representation of audio
    plt.subplot(2, 1, 2)
    sample_indices = np.arange(len(binary_data))
    for bit_index in range(bit_depth):  # Iterate through each bit position
        plt.step(sample_indices, [int(binary_data[i][bit_index]) for i in range(len(binary_data))],
                 label=f'Bit {bit_index + 1}', where='mid', linestyle='-', alpha=0.6)

    plt.title(f'Binary Representation ({bit_depth}-bit Quantization)')
    plt.xlabel('Sample Index')
    plt.ylabel('Bit Value [0 or 1]')
    plt.legend(loc='upper right')
    plt.grid(True)

    # Finalize layout and display
    plt.tight_layout()
    plt.show()

# Record audio for 5 seconds with a sample rate of 44100 Hz
recorded_audio = record_audio(duration_sec=5, sample_rate=44100)

# Visualize the audio signal and its binary representation
plot_audio_and_binary(recorded_audio, sample_rate=44100, bit_depth=8)
