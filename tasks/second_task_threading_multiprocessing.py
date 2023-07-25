import time
import threading
import multiprocessing

"""
Розробіть програму для виконання одного і того ж обчислювального завдання двома способами: 
за допомогою багатопоточності та багатопроцесорності. 
Зробіть висновки про продуктивність кожного методу.
"""


def calculate_task(number):
    result = 0
    for i in range(0, number + 1):
        result += i
    return result


def threading_task():
    global number
    number = int(input("Enter the number for second task: "))

    time_start = time.time()

    t1, t2 = threading.Thread(target=calculate_task, args=[number]), threading.Thread(
        target=calculate_task, args=[number * 2]
    )

    print("Starting the process...")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    time_end = time.time()

    return print(
        f"""
    _______________________________________________
                Done second task!
            Thread is alive: {t1.is_alive()}
           Time taken for threading: 
                  {round(time_end - time_start, 8)} s
    _______________________________________________
        """
    )


def multiprocessing_task():
    global number
    print("*" * 100)

    start_time = time.time()

    process1, process2 = multiprocessing.Process(
        target=calculate_task, args=[number]
    ), multiprocessing.Process(target=calculate_task, args=[number * 2])

    print("\nStarting the process...")

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()

    print(
        f"""
    _______________________________________________
                Done second task!
            Process is alive: {process1.is_alive()}
         Time taken for multiprocessing: 
                   {round(end_time - start_time, 8)} s
    _______________________________________________
        """
    )

    print("*" * 100)


if __name__ == "__main__":
    threading_task()
    multiprocessing_task()
