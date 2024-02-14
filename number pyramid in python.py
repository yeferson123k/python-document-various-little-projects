def generate_number_pyramid(n):
    for i in range(1, n + 1):
#        for j in range(1, n - 1 + 1): left triangle part
#        for j in range(1, n - i + 1): right triangle part
        for j in range(1, n - i + 1):
            print(" ", end=" ")
#        for j in range(1, 0, -1): if you use this give you a  left or right part of the pyramid           
        for j in range(i, 0, -1):
            print(j, end=" ")
        for j in range(2, i + 1):
            print(j, end=" ")
        print()

number_of_rows = int(input("Enter the number of rows: "))
generate_number_pyramid(number_of_rows)