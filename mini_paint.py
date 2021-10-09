from sys import argv

if len(argv) != 2:
    print('Error: argument')
    exit()


def get_operations():
    try:
        with open(argv[1], 'r') as f:
            canvas_operation = f.readline().split()

            canvas_width = int(canvas_operation[0])
            canvas_height = int(canvas_operation[1])
            canvas_char = canvas_operation[2]

            if not 0 < canvas_width <= 300 or not 0 < canvas_height <= 300 or len(canvas_char) != 1:
                print('Error: Incorrect operation file')
                exit()

            canvas_arguments = (canvas_width, canvas_height, canvas_char)
            operations = []

            for i in f.readlines():
                i = i.replace('\n', '')
                operations_arguments = i.split()

                if not operations_arguments[0] in ('r', 'R') or int(operations_arguments[3]) > canvas_arguments[0] or int(operations_arguments[4]) > canvas_arguments[1] or len(operations_arguments[5]) != 1:
                    print('Error: Incorrect operation file')
                    exit()

                operations.append(i)

            return canvas_operation, operations

    except FileNotFoundError:
        print('Error: Error: Operation file corrupted')
        exit()


print(get_operations())

