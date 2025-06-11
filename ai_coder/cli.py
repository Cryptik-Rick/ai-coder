import argparse

def main():
    parser = argparse.ArgumentParser(description="Echo CLI")
    parser.add_argument("text", help="Text to echo")
    args = parser.parse_args()
    print(args.text)

if __name__ == "__main__":
    main()