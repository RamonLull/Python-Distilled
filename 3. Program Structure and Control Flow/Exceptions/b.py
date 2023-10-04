def find_running_task(tasks, cycle):
    remaining_cycles = cycle
    current_task = -1
    while remaining_cycles > 0:
        min_cycles = float('inf')
        for i, task_cycles in enumerate(tasks):
            if task_cycles > 0 and task_cycles < min_cycles:
                min_cycles = task_cycles
                current_task = i
        if current_task == -1:
            return -1  # No task running
        decrement_cycles = min(min_cycles, remaining_cycles)
        tasks[current_task] -= decrement_cycles
        remaining_cycles -= decrement_cycles
    return current_task

