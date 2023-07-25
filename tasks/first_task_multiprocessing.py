import multiprocessing
import time

"""
Напишіть програму з двома потоками: 
один потік виводить парні числа,
інший - непарні числа від 1 до 20.
"""


def print_even_numbers():
    for i in range(2, 21, 2):
        print("Even:", i)
        time.sleep(0.01)


def print_odd_numbers():
    for i in range(1, 20, 2):
        print("Odd:", i)
        time.sleep(0.01)


def main():
    print("*" * 100)

    process1 = multiprocessing.Process(target=print_odd_numbers)
    process2 = multiprocessing.Process(target=print_even_numbers)

    time_start = time.time()

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    time_end = time.time()

    print(
        f"""
    _______________________________________
                Done first task!
        Time taken: {time_end - time_start}
    _______________________________________
        """
    )
    print("*" * 100)


if __name__ == "__main__":
    main()
