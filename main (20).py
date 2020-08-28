import numpy

class Numpy():
    def __init__(self, arr_1, arr_2):
        self.arr_1 = arr_1
        self.arr_2 = arr_2

    def concatenate(self):
        print(numpy.concatenate((arr_1, arr_2), axis = 0))

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    arr_1 = numpy.array([input().split() for _ in range(n)], int)
    arr_2 = numpy.array([input().split() for _ in range(m)], int)
    my_object = Numpy(arr_1, arr_2)
    my_object.concatenate()