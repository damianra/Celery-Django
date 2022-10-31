import random
from celery import shared_task

@shared_task
def add(x, y):
    # Celery recognizes this as the `movies.tasks.add` task
    # the name is purposefully omitted here.
    print('ADD')
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    print('MUL')
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    print('XSUM')
    # Celery recognizes this as the `sum_list_numbers` task
    return sum(numbers)
