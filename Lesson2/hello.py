if __name__ == "__main__":
    greeting = "Hello, World!"
    print(greeting)
    with open("greeting.txt", "w") as file:
        file.write(greeting + "\n")
