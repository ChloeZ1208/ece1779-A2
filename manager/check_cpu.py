import math
import random
from manager import admin, worker, auto_scaling


'''
Checking the CPU every 1min
'''
def check_cpu():
    instances = worker.get_all_targets()
    cpu_list = []
    instance_id = []
    for instance in instances:
        id = instance['Target']['Id']
        cpu_stats = worker.get_cpu_stats(id)
        if len(cpu_stats) > 0:
            instance_id.append(id)
            average = (cpu_stats[-1][1] + cpu_stats[-2][1]) / 2  # average cpu in last 2 mins
            cpu_list.append(average)
    num = len(cpu_list)
    cpu_average = sum(cpu_list) / num
    return num, cpu_average, instance_id

def compare_cpu():
    num, cpu_average, instance_id = check_cpu()

    (grow_threshold, shrink_threshold, expand_ratio, shrink_ratio) = auto_scaling.get_policy()

    if cpu_average < grow_threshold:
        num_add = (expand_ratio - 1) * num
        # the maximum size of worker pool is set to 8
        if expand_ratio * num <= 8:
            for n in range(num_add):
                worker.add_worker()
        else:
            num_add = 8 - num
            for n in range(num_add):
                worker.add_worker()

    elif cpu_average > shrink_threshold:
        num_remove = int(math.ceil(num * shrink_ratio))
        # the minimum size of worker pool is set to 1
        if num - num_remove >= 1 :
            for n in range(num_remove):
                random.shuffle(instance_id)
                worker.remove_worker(instance_id[n])
        else:
            num_remove = num - 1
            for n in range(num_remove):
                random.shuffle(instance_id)
                worker.remove_worker(instance_id[n])
