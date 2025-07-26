import argparse
from sender import play_morse_code
from receiver import listen_for_morse_code

def main():
    parser = argparse.ArgumentParser(description="Send and receive morse code messages using ultrasound.")
    parser.add_argument('mode', choices=['send', 'receive'], help="Whether to send or receive a message.")
    parser.add_argument('-m', '--message', type=str, help="The message to send.")
    parser.add_argument('-f', '--file', type=str, default="morse_audio.raw", help="The file to write to or read from.")
    args = parser.parse_args()

    if args.mode == 'send':
        if not args.message:
            print("Please provide a message to send with the -m/--message argument.")
            return
        print(f"Sending message: {args.message}")
        play_morse_code(args.message, args.file)
        print("Message sent to file.")
    elif args.mode == 'receive':
        listen_for_morse_code(args.file)

if __name__ == '__main__':
    main()
