if __name__ == '__main__':
    N = int(input())
    my_list = []  # Initialize the list

    for _ in range(N):
        command = input().split()

        if command[0] == 'insert':
            # insert i e: Insert integer e at position i
            position = int(command[1])
            element = int(command[2])
            my_list.insert(position, element)

        elif command[0] == 'print':
            # Print the list
            print(my_list)

        elif command[0] == 'remove':
            # remove e: Delete the first occurrence of integer e
            element = int(command[1])
            my_list.remove(element)

        elif command[0] == 'append':
            # append e: Insert integer e at the end of the list
            element = int(command[1])
            my_list.append(element)

        elif command[0] == 'sort':
            # Sort the list
            my_list.sort()

        elif command[0] == 'pop':
            # Pop the last element from the list
            my_list.pop()

        elif command[0] == 'reverse':
            # Reverse the list
            my_list.reverse()
        
