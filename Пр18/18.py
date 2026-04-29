with open("log.txt", "r") as f:
    count = sum(1 for line in f if "ERROR" in line)
    print(count)