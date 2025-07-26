# Ultrasound Morse Code

This project implements a Python-based sender and receiver for transmitting Morse code using ultrasound. Due to limitations in the testing environment, the implementation uses a file-based approach for communication instead of actual audio devices.

## Prerequisites

- Python 3
- NumPy
- PyAudio
- SciPy

You can install the dependencies using pip:

```bash
pip install numpy pyaudio scipy
```

## How to Run

1.  **Send a message:**

    To send a message, run the `main.py` script with the `send` mode and provide a message using the `-m` or `--message` argument.

    ```bash
    python3 main.py send -m "hello world"
    ```

    This will create a file named `morse_audio.raw` in the same directory, containing the audio data for the Morse code message.

2.  **Receive a message:**

    To receive a message, run the `main.py` script with the `receive` mode.

    ```bash
    python3 main.py receive
    ```

    This will read the `morse_audio.raw` file and decode the message.

## How to Test

To test the implementation, you can run the sender and receiver in sequence:

```bash
python3 main.py send -m "hello world" && python3 main.py receive
```

This will first send the message "hello world" to the `morse_audio.raw` file, and then the receiver will read the file and print the decoded message to the console.
