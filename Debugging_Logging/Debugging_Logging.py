# def square(x):
#     temp = x**2
#     print(temp)
#     return

# def main():
#     for i in range(1, 11):
#         square(i)

# if __name__ == "__main__":
#     main()
    
    
# | Command           | Meaning                   |
# | ----------------- | ------------------------- |
# | `l`               | List source code          |
# | `n`               | Execute next line         |
# | `s`               | Step into a function      |
# | `c`               | Continue execution        |
# | `p variable`      | Print a variable          |
# | `pp variable`     | Pretty-print a variable   |
# | `b 10`            | Set breakpoint at line 10 |
# | `b function_name` | Break at a function       |
# | `cl`              | Clear breakpoints         |
# | `q`               | Quit debugger             |


import logging

# logging.basicConfig(filename='test.log', level=logging.INFO)

# logging.debug('This is a debug message.')
# logging.info('This is an informational message.')
# logging.error('This is an error message.')


# a = 10
# b = 0

# try:
#     temp = a/b
#     print(temp)
# except ZeroDivisionError as e:
#     logging.exception(e)
    
    
    
from Code import add, is_even

# logging.basicConfig(filename='test.log', level=logging.INFO)
# logging.info('We are calling our add function.')
# temp = add(12, 78)
# print(temp)
# logging.info('add function executed, task completed.')
# logging.info('We are calling our is_even function.')
# temp = is_even(2)
# print(temp)
# logging.info('is_even function executed, task completed.')



logging.basicConfig(filename='test.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logging.info('We are calling our add function.')
temp = add(12, 78)
print(temp)
logging.info('add function executed, task completed.')
logging.info('We are calling our is_even function.')
temp = is_even(2)
print(temp)
logging.info('is_even function executed, task completed.')