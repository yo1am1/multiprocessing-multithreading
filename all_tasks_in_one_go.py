from tasks import (
    second_task_threading_multiprocessing,
    fourth_task_get_multiprocessing,
    first_task_multiprocessing,
    third_task_get_threading,
    fifth_task_get_concurent_futures,
)


def main():
    print(
        f"""

            ________________________________________________________________
            |                                                              |
            |   This is a program that runs all tasks in one go.           |
            |   You can find all tasks in the same directory as this file. |
            |                                                              |
            |   You can run each task separately by running the file       |
            |   with the name of the task.                                 |
            |                                                              |
            |   For example:                                               |
            |   python first_task_multiprocessing.py                       |
            |                                                              |
            ________________________________________________________________

    """
    )

    first_task_multiprocessing.main()
    second_task_threading_multiprocessing.threading_task()
    second_task_threading_multiprocessing.multiprocessing_task()
    third_task_get_threading.main()
    fourth_task_get_multiprocessing.main()
    fifth_task_get_concurent_futures.main()


if __name__ == "__main__":
    main()
