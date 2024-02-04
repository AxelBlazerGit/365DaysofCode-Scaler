def main():
    num = int(raw_input())
    if num >= 90:
        grade = "A"
    elif num >= 80:
        grade = "B"
    elif num >= 70:
        grade = "C"
    elif num >= 60:
        grade = "D"
    elif num >= 50:
        grade = "E"
    else:
        grade = "F"
    print(grade)
    # YOUR CODE GOES HERE
    
    return 0

if __name__ == '__main__':
    main()
