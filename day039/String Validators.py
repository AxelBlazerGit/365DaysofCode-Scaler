def main():
    S = raw_input()
    #You code goes here
    print(any(char.isalnum() for char in S))
    print(any(char.isalpha() for char in S))
    print(any(char.isdigit() for char in S))
    print(any(char.islower() for char in S))
    print(any(char.isupper() for char in S))
    return 0

if __name__ == '__main__':
    main()
