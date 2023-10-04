import heapq


def find_running_task(tasks, cycle):
    task_heap = [(cycles, index) for index, cycles in enumerate(tasks)]
    heapq.heapify(task_heap)

    while task_heap:
        cycles, index = heapq.heappop(task_heap)

        if cycles == cycle:
            return index
        elif cycles < cycle:
            cycle -= cycles
        else:
            heapq.heappush(task_heap, (cycles - cycle, index))
            break

    return -1


# Example usage
tasks = [2,6,7,1,4]
cpu_cycle = 5
running_task = find_running_task(tasks, cpu_cycle)
print(running_task)  # Output: 0