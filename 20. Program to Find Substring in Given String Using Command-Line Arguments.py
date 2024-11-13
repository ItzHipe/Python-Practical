import sys

if len(sys.argv) == 3:
    main_string = sys.argv[1]
    substring = sys.argv[2]
    if substring in main_string:
        print(f"The substring '{substring}' is found in '{main_string}'.")
    else:
        print(f"The substring '{substring}' is not found in '{main_string}'.")
else:
    print("Usage: python script.py <main_string> <substring>")