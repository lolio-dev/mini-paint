from pprint import pprint
from sys import argv

if len(argv) != 2:
    print('Error: argument')
    exit()


# get data from .txt files
try:
    with open(argv[1], 'r') as f:
        canvas_operation = f.readline().split()

        canvas_width = int(canvas_operation[0])
        canvas_height = int(canvas_operation[1])

        canvas_char = canvas_operation[2]

        if not 0 < canvas_width <= 300 or not 0 < canvas_height <= 300 or len(canvas_char) != 1:
            print('Error: Incorrect operation file')
            exit()

        operations = []
        for i in f.readlines():
            i = i.replace('\n', '')
            operations_arguments = i.split()

            if not operations_arguments[0] in ('r', 'R') or int(operations_arguments[3]) > canvas_width \
                    or int(operations_arguments[4]) > canvas_height or len(operations_arguments[5]) != 1:
                print('Error: Error: Operation file corrupted')
                exit()

            operations.append(i)

except FileNotFoundError:
    print('Error: Error: Operation file corrupted')
    exit()

# Define canvas
canvas = [list(canvas_char * canvas_width) for _ in range(canvas_height)]

# Draw shapes
for operation in operations:
    operation = operation.split()

    begin_X = int(operation[1])
    begin_Y = int(operation[2])

    shape_type = operation[0]
    width = int(operation[3])
    height = int(operation[4])
    character = operation[5]

    try:
        if shape_type == 'R':
            for j in range(begin_Y - 1, begin_Y + height, 1):
                canvas[j][begin_X] = operation[5]

                for i in range(begin_X - 1, begin_X + width, 1):
                    canvas[j][i] = operation[5]
        elif shape_type == 'r':
            for i in range(begin_X, begin_X + width, 1):
                canvas[begin_Y][i] = character
                canvas[begin_Y + height - 1][i] = character

            for i in range(begin_Y, begin_Y + height, 1):
                canvas[i][begin_X] = character
                canvas[i][begin_X + width] = character
    except IndexError:
        print('Error: Error: Operation file corrupted')
        exit()

# Display Canvas
for i in canvas:
    print(''.join(i))
