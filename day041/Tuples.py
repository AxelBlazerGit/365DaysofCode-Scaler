def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    
    tuple1_list = list(tuple1)
    tuple1_list[0] = "number"
    tuple1 = tuple(tuple1_list)

    tuple2_list = list(tuple2)
    tuple2_list[0] = "number"
    tuple2 = tuple(tuple2_list)
    
    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()
