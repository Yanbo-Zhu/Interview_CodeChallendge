
def is_palindrome(string):
    n = len(string)
    is_palindrome = True

    for i in range(0, (n+1)//2):
        if string[i] == string[n-i-1]:
            print(string[i])
            print(string[n-i-1])
            is_palindrome = True
            print("True")
        else:
            print(string[i])
            print(string[n-i-1])
            is_palindrome = False
            print("False")
            break

    print(  (n-1)//2 )
    print("palindrome: ", is_palindrome)
    print("") 

if __name__ == "__main__":
    test_string = 'abcdfcba'
    is_palindrome(test_string)


