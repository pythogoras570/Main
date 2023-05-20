
low_grades = int(input())

low_grades_count = 0
grade = 0
grade_total = 0
tasks_count = 0
last_task = ''
has_failed = True

while low_grades_count < low_grades:
    task_name = input()
    if task_name == 'Enough':
        has_failed = False
        break
    grade = int(input())

    grade_total += grade
    tasks_count += 1
    last_task = task_name

    if grade <= 4:
        low_grades_count += 1

if not has_failed:
    print(f'Average score: {grade_total / tasks_count:.2f}')
    print(f'Number of problems: {tasks_count}')
    print(f'Last problem: {last_task}')
else:
    print(f'You need a break, {low_grades_count} poor grades.')