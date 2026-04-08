import numpy as np
import soundfile as sf

# 1. Create a 3-second test signal at 8kHz
sr = 8000
t = np.linspace(0, 3, 3 * sr)

# 2. Add a 440Hz "Infant Cry" simulation and 1000Hz "Noise"
signal_440 = 0.5 * np.sin(2 * np.pi * 440 * t)
noise_1000 = 0.2 * np.sin(2 * np.pi * 1000 * t)
test_signal = signal_440 + noise_1000

# 3. Save it to your research folder
sf.write("test_8khz_signal.wav", test_signal, sr)
print("✅ Test signal generated: test_8khz_signal.wav")
