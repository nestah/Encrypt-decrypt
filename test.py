# this file can be used to generate a secret key if it wasnt generated during running of the backend file

import backend

def main():
    print("Generating and saving key...")
    key = backend.load_key()
    print("Key loaded:", key)

if __name__ == "__main__":
    main()
