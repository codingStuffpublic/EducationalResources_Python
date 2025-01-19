try:
    file = open("a.txt")
    # dictionary = {"key": "value"}
    # value = dictionary["non_existing_key"]
except FileNotFoundError:
    print("File Error")
    file = open("a.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"Key error {error_message}")
else: # only if no exception
    content = file.read()
    print("else")
finally:
    file.close()
    print("File was closed")