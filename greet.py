def main(user: str):
    print(f"Welcome Mr/Ms {user} to python learning scope...")

def list_printing():
    data = ["Python","Assembly","React","Database"]

    for x in data:
        print(x, end=' ') # to print details in same line


if __name__ == "__main__":
    main(user="Balaji")
    list_printing()
