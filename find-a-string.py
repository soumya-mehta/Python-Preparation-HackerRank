def count_substring(string, sub_string):
    #initializing the count as 0
    count = 0
    #defining the range of transvering the string
    #for loop to check the string for substring till the last element
    for i in range(len(string) - len(sub_string) + 1):
        #adding if statement to update the count variable if the substring is found in the string
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
