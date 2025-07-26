import numpy as np
import time
from morse import encrypt

# Audio settings
FREQUENCY = 20000  # 20kHz frequency
SAMPLING_RATE = 44100
DURATION_DOT = 0.1
DURATION_DASH = 0.3
AMPLITUDE = 0.5

def generate_tone(frequency, duration, sampling_rate=SAMPLING_RATE):
    t = np.linspace(0, duration, int(sampling_rate * duration), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    return (tone * AMPLITUDE).astype(np.float32)

def play_morse_code(message, filename="morse_audio.raw"):
    morse_code = encrypt(message)
    with open(filename, "wb") as f:
        for symbol in morse_code:
            if symbol == '.':
                tone = generate_tone(FREQUENCY, DURATION_DOT)
                f.write(tone.tobytes())
                silence = np.zeros(int(SAMPLING_RATE * DURATION_DOT), dtype=np.float32)
                f.write(silence.tobytes())
            elif symbol == '-':
                tone = generate_tone(FREQUENCY, DURATION_DASH)
                f.write(tone.tobytes())
                silence = np.zeros(int(SAMPLING_RATE * DURATION_DOT), dtype=np.float32)
                f.write(silence.tobytes())
            elif symbol == ' ':
                # In a real scenario, this would be silence.
                # For file-based testing, we can write zeros.
                silence = np.zeros(int(SAMPLING_RATE * DURATION_DOT), dtype=np.float32)
                f.write(silence.tobytes())
            elif symbol == '/':
                silence = np.zeros(int(SAMPLING_RATE * DURATION_DASH), dtype=np.float32)
                f.write(silence.tobytes())

if __name__ == '__main__':
    message = "hello world"
    play_morse_code(message)
