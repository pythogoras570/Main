employee_happiness, improvement_factor = \
    [int(number) for number in input().split()], int(input()); zephyr = \
    [happiness * improvement_factor for happiness in employee_happiness if happiness >= sum(employee_happiness) /
     len(employee_happiness)]; print(f"Score: {len(zephyr)}/{len(employee_happiness)}. "
                                     f"Employees are "
                                     f"{'happy' if len(zephyr) >= len(employee_happiness) / 2 else 'not happy'}!")
