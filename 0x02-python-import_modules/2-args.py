#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for length in range(len(sys.argv)):
        print(f"{length}: {sys.argv[length]}")
