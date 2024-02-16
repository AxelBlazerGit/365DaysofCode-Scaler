def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm', 'allows', 'community', 'phase', 'single']

    # List comprehension to create a new list 'my_list' with strings of odd length
    my_list = [s for s in str_list if len(s) % 2 != 0]

    print(my_list)
    return 0

if __name__ == '__main__':
    main()
