import numpy as np


def calculate(python_list):
    if len(python_list) < 9:
        raise ValueError('List must contain nine numbers.')

    numpy_list = np.array(python_list).reshape((3, 3))

    mean0 = numpy_list.mean(axis=0)
    mean1 = numpy_list.mean(axis=1)
    mean2 = numpy_list.mean()

    var0 = numpy_list.var(axis=0)
    var1 = numpy_list.var(axis=1)
    var2 = numpy_list.var()

    std0 = numpy_list.std(axis=0)
    std1 = numpy_list.std(axis=1)
    std2 = numpy_list.std()

    max0 = numpy_list.max(axis=0)
    max1 = numpy_list.max(axis=1)
    max2 = numpy_list.max()

    min0 = numpy_list.min(axis=0)
    min1 = numpy_list.min(axis=1)
    min2 = numpy_list.min()

    sum0 = numpy_list.sum(axis=0)
    sum1 = numpy_list.sum(axis=1)
    sum2 = numpy_list.sum()

    calculations = {
        'mean': [mean0.tolist(), mean1.tolist(), mean2],
        'variance': [var0.tolist(), var1.tolist(), var2],
        'standard deviation': [std0.tolist(), std1.tolist(), std2],
        'max': [max0.tolist(), max1.tolist(), max2],
        'min': [min0.tolist(), min1.tolist(), min2],
        'sum': [sum0.tolist(), sum1.tolist(), sum2]
    }

    return calculations


li = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(calculate(li))
