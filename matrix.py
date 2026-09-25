# # # # # # # # arr = [1, 2, 3, 4, 5]

# # # # # # # # reversed_arr = []

# # # # # # # # for i in range(len(arr) - 1, -1, -1):
# # # # # # # #     reversed_arr.append(arr[i])

# # # # # # # # print(reversed_arr)

# # # # # # # matrix1 = [
# # # # # # #     [1, 2, 3],
# # # # # # #     [4, 5, 6],
# # # # # # #     [7, 8, 9]
# # # # # # # ]

# # # # # # # matrix2 = [
# # # # # # #     [11, 12, 13],
# # # # # # #     [14, 15, 16],
# # # # # # #     [17, 18, 19]
# # # # # # # ]

# # # # # # # transpose = []

# # # # # # # fmatrix1 = [
# # # # # # #     [1, 2, 3],
# # # # # # #     [4, 5, 6],
# # # # # # #     [7, 8, 9]
# # # # # # # ]

# # # # # # # matrix2 = [
# # # # # # #     [11, 12, 13],
# # # # # # #     [14, 15, 16],
# # # # # # #     [17, 18, 19]
# # # # # # # ]

# # # # # # # transpose = []

# # # # # # # for j in range(len(matrix1[0])):
# # # # # # #     row = []
# # # # # # #     for i in range(len(matrix1)):
# # # # # # #         row.append(matrix1[i][j])
# # # # # # #     transpose.append(row)



# # # # # # # print(transpose)



# # # # # # # arr = [[1,2,3],
# # # # # # #        [3,4,5],
# # # # # # #        [6,7,8]]

# # # # # # # transpose = []
# # # # # # # for i in range(3):
# # # # # # #     row = []
# # # # # # #     for j in range(3):
# # # # # # #         row.append(arr[j][i])
# # # # # # #     transpose.append(row)
# # # # # # # # print(transpose)
# # # # # # # for a in transpose:
# # # # # # #     print(a)



# # # # # # # l = [1,11,111,1111,11111]
# # # # # # # rev = []
# # # # # # # for i in range(len(l)-1,-1,-1):
# # # # # # #     rev.append(l[i])
# # # # # # # print(rev)

# # # # # # # que 1
# # # # # # # numbers = [45, 12, 78, 3, 56, 23]

# # # # # # # numbers.sort()

# # # # # # # print(numbers)

# # # # # # # que 2
# # # # # # # numbers = [45, 12, 78, 3, 56, 23]

# # # # # # # que 3
# # # # # # # numbers.sort(reverse=True)

# # # # # # # print(numbers)

# # # # # # # numbers = [34, 11, 89, 22, 5, 67]

# # # # # # # sorted_numbers = sorted(numbers)

# # # # # # # print("Original list:", numbers)
# # # # # # # print("Sorted list:", sorted_numbers)

# # # # # # # que 4

# # # # # # # names = ["Rahul", "Aman", "Priya", "Karan", "Neha"]

# # # # # # # sorted_names = sorted(names)

# # # # # # # print(sorted_names)

# # # # # # # Original list
# # # # # # words = ["Python", "AI", "Data", "Analytics", "SQL"]

# # # # # # # Sort by length using sorted() and key
# # # # # # sorted_words = sorted(words, key=lambda x: len(x))

# # # # # # # Convert into 2D list (word, length)
# # # # # # result = [[word, len(word)] for word in sorted_words]

# # # # # # # Output
# # # # # # print("Sorted Words:", sorted_words)
# # # # # # print("2D List:", result)


# # # # # # matrix1 = [
# # # # # #     [1, 2, 3],
# # # # # #     [4, 5, 6],
# # # # # #     [7, 8, 9],
# # # # # #     [7, 8, 9]
# # # # # # ]

# # # # # # matrix2 = [
# # # # # #     [11, 12, 13],
# # # # # #     [14, 15, 16],
# # # # # #     [17, 18, 19],
# # # # # #     [17, 18, 19]
# # # # # # ]

# # # # # # result = []

# # # # # # for i in range(4):   # 4 rows
# # # # # #     row = []
# # # # # #     for j in range(3):   # 3 columns
# # # # # #         row.append(matrix1[i][j] + matrix2[i][j])
# # # # # #     result.append(row)

# # # # # # # Print the result matrix

# # # # # # for r in result:
# # # # # #     print(r)



# # # # # arr_1 = [[1, 2, 3],
# # # # #        [4, 5, 6],
# # # # #        [7, 8, 9]]

# # # # # arr_2 = [[1, 2, 3],
# # # # #        [4, 5, 6],
# # # # #        [7, 8, 9]]

# # # # # result = []

# # # # # for i in range (len(arr_1)):
# # # # #     row = []
# # # # #     for j in range (len(arr_2)):



# # # # # Accept matrix size
# # # # n = int(input("Enter size of square matrix: "))

# # # # # Accept matrix elements
# # # # matrix = []
# # # # print("Enter matrix elements row-wise:")
# # # # for i in range(n):
# # # #     row = list(map(int, input().split()))
# # # #     matrix.append(row)

# # # # # Print matrix
# # # # print("\nMatrix is:")
# # # # for r in matrix:
# # # #     print(r)

# # # # # Print main diagonal
# # # # print("\nMain Diagonal Elements:")
# # # # for i in range(n):
# # # #     print(matrix[i][i])

# # # # # Print secondary diagonal
# # # # print("\nSecondary Diagonal Elements:")
# # # # for i in range(n):
# # # #     print(matrix[i][n - i - 1])




# # # # class person:
# # # #     def __init__ (self, name, age, contact):
# # # #         self.name = name
# # # #         self.age = age
# # # #         self.__contact__ = contact
# # # #     def 








# # # # destructor method

# # # # class person:
# # # #     def __init__ (self, name):
# # # #         self.name = name
# # # #     def __del__ (self):
# # # #         print ("destructor is called")
# # # # p = person("ram")
# # # # del p

# # # # constructor method

# # class Student:   # class name should be Student, not students
# #     def __init__(self, name, marks):   # Constructor
# #         self.__name = name             # private attribute
# #         self.__marks = marks           # private attribute
# #         print("Constructor called! Object created.")

# #     def display(self):                 # Method to show data
# #         print("Name:", self.__name, "Marks:", self.__marks)

# #     def __del__(self):                 # Destructor
# #         print("Destructor called! Object destroyed.")


# # # Object creation
# # s1 = Student("Liza", 90)   # no comma here
# # s1.display()

# # # Object deletion
# # del s1

# # class person:
# #     def __init__ (self, name, age):
# #         self.name = name
# #         # self.age = age



# # class parent1:
# #     def house (self):
# #         print ("parent1 has house")
# # class parent2 (parent1):
# #     def land (self):
# #         print("parent2 has land")
# # class child (parent2):
# #     def car (self):
# #         print ("son has car")

# # c = child()
# # c.car()


# # Parent class (CEO)
# class CEO:
#     def decision(self):
#         print("CEO takes big decisions")

# # Child classes inheriting from CEO
# class Manager(CEO):
#     def manage_team(self):
#         print("Manager manages the team")

# class Accountant(CEO):
#     def handle_accounts(self):
#         print("Accountant handles company accounts")

# class Developer(CEO):
#     def write_code(self):
#         print("Developer writes code")

# # Object creation
# m = Manager()
# a = Accountant()
# d = Developer()

# # Method calls
# m.decision()
# m.manage_team()

# a.decision()
# a.handle_accounts()

# d.decision()
# d.write_code()


