# time -v python3 test.py

# Measure-Command { python test.py } # Windows

# python3 -m timeit '"-".join(str(n) for n in range(100))'

# python -m timeit '"-".join(str(n) for n in range(100))' # Windows

import timeit
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

# cProfile


# from profilehooks import profile

# @profile
# def Work():
#     count = 0
#     while count < 100000:
#         count += 1
#     return count

# if __name__ == '__main__':
#     temp = Work()
#     print(temp, 'loops.')

# from profilehooks import timecall

# @timecall
# def Work():
#     count = 0
#     while count < 100000:
#         count += 1
#     return count

# if __name__ == '__main__':
#     temp = Work()
#     print(temp, 'loops.')

# from profilehooks import coverage

# @coverage
# def work():
#     count = 0
#     while count < 100000:
#         count += 1
#     return count

# if __name__ == '__main__':
#     temp = work()
#     print(temp, 'loops.')
    
    
# line_profiler

@profile
def ghoraghuri():
    count = 0
    while count < 100000:
        count += 1
    return count

if __name__ == '__main__':
    temp = ghoraghuri()
    print(temp, 'loops.')