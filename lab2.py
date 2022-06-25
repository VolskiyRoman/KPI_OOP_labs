class Matrix:
    def __init__(self):
        self.matrix_c = None
        self.odd_sum = None
        self.even_sum = None
        self.matrix = [[2, 4, 5, 17, 8, 23], [13, 15, 2, 1, 7, 6], [5, 12, 15, 9, 1, 22], [17, 14, 11, 5, 9, 8]]

    def matrix_print(self):
        print("Початкова матриця:")
        for i in self.matrix:
            print(i)
        print("\n")

    def matrix_c_gen(self):
        self.matrix_c = []
        for i in range(len(self.matrix[0])):
            c_row = []
            for j in range(len(self.matrix)):
                c_row.append(self.matrix[j][i])
            self.matrix_c.append(c_row)



    def matrix_c_print(self):
        print("Матриця C")
        for i in self.matrix_c:
            print(i)
        print("\n")

    def odd_sum_gen(self):
        biggest_odd_list = []
        for i in self.matrix_c:
            odd_list = i[0::2]
            biggest_odd_list.append(max(odd_list))
        self.odd_sum = sum(biggest_odd_list)

        print("Найбільші непарні значення кожного рядка: {0}".format(biggest_odd_list))
        print("Сума найбільших непарних значень кожного рядка: {0}".format(self.odd_sum))
        print("\n")

    def even_sum_gen(self):
        least_even_list = []
        for i in self.matrix_c:
            even_list = i[1::2]
            least_even_list.append(min(even_list))
        self.even_sum = sum(least_even_list)

        print("Найменші парні значення кожного рядка: {0}".format(least_even_list))
        print("Сума найменших парних значень кожного рядка: {0}".format(self.even_sum))


obj = Matrix()
obj.matrix_print()
obj.matrix_c_gen()
obj.matrix_c_print()
obj.odd_sum_gen()
obj.even_sum_gen()
