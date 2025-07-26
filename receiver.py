import numpy as np
from morse import decrypt

# Audio settings
SAMPLING_RATE = 44100
THRESHOLD = 0.1
CHUNK_SIZE = 1024
DOT_DURATION = 0.1
DASH_DURATION = 0.3

def listen_for_morse_code(filename="morse_audio.raw"):
    print("Listening for morse code from file...")

    morse_code = ""
    current_symbol = ""
    silence_counter = 0

    with open(filename, "rb") as f:
        file_content = f.read()

    data = np.frombuffer(file_content, dtype=np.float32)
    chunks = [data[i:i + CHUNK_SIZE] for i in range(0, len(data), CHUNK_SIZE)]

    for chunk in chunks:
        amplitude = np.sqrt(np.mean(chunk**2))

        if amplitude > THRESHOLD:
            current_symbol += "1"
            silence_counter = 0
        else:
            current_symbol += "0"
            silence_counter += 1

    # Process the recorded signal
    morse_symbols = []
    symbol_started = False
    start_index = 0
    for i, bit in enumerate(current_symbol):
        if bit == '1' and not symbol_started:
            symbol_started = True
            start_index = i
        elif bit == '0' and symbol_started:
            symbol_started = False
            duration = i - start_index
            if duration > (DASH_DURATION * SAMPLING_RATE * 0.5 / CHUNK_SIZE):
                 morse_symbols.append("-")
            else:
                 morse_symbols.append(".")

        if bit == '0' and i > 0 and current_symbol[i-1] == '1':
            silence_duration = 0
            for j in range(i, len(current_symbol)):
                if current_symbol[j] == '0':
                    silence_duration +=1
                else:
                    break
            if silence_duration > (DASH_DURATION * SAMPLING_RATE * 0.5 / CHUNK_SIZE):
                morse_symbols.append("/")
            elif silence_duration > (DOT_DURATION * SAMPLING_RATE * 1.5 / CHUNK_SIZE):
                morse_symbols.append(" ")


    print(f"Morse Symbols: {morse_symbols}")

    try:
        message = decrypt(morse_symbols)
        print(f"Received message: {message}")
    except Exception as e:
        print(f"Could not decrypt morse code: '{morse_symbols}', error: {e}")


if __name__ == '__main__':
    listen_for_morse_code()
