import sys

keyword1 = ["doesn't"]
keyword2 = ["don't"]
def main():
    count1 = 0
    count2 = 0
    for line in sys.stdin:
        for keyword in keyword1:
            if keyword.lower() in line.lower():
                count1 += 1
                print(line, end='')
                break
        for keyword in keyword2:
            if keyword.lower() in line.lower():
                count2 += 1
                print(line, end='')
                break
    print(f"found doesn't:{count1} times")
    print(f"found don't:{count2} times")

if __name__ == "__main__":
    main()