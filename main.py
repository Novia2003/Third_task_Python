def read_advertisements(input_file):
    advertisements = []

    with open(input_file, 'r') as file:
        for line in file:
            is_district = True
            advertisement = []

            for parameter in line.split(" "):
                if is_district:
                    advertisement.append(parameter)
                    is_district = False
                else:
                    advertisement.append(int(parameter))

            advertisements.append(advertisement)

    return advertisements


def is_parameter_in_range(maximum, minimum, parameter):
    return (maximum is None or maximum >= parameter) and (minimum is None or minimum <= parameter)


def filter_advertisements(advertisements):
    maximum_quantity_rooms = 8
    minimum_quantity_rooms = 2

    maximum_total_area = 300
    minimum_total_area = None

    maximum_kitchen_area = None
    minimum_kitchen_area = 20

    maximum_cost = None
    minimum_cost = None

    maximums = [maximum_quantity_rooms, maximum_total_area, maximum_kitchen_area, maximum_cost]
    minimums = [minimum_quantity_rooms, minimum_total_area, minimum_kitchen_area, minimum_cost]

    advertisement_index = 0

    while advertisement_index != len(advertisements):
        advertisement = advertisements[advertisement_index]

        for index in range(4):
            if not is_parameter_in_range(maximums[index], minimums[index], advertisement[index + 1]):
                advertisements.pop(advertisement_index)
                advertisement_index -= 1
                break

        advertisement_index += 1


def get_str_from_line(advertisement):
    result_str = ""

    for parameter in advertisement:
        result_str += str(parameter) + " "

    result_str += "\n"

    return result_str


def print_result_to_file(advertisements):
    with open('output.txt', 'w') as file:
        for advertisement in advertisements:
            file.write(get_str_from_line(advertisement))


def main():
    advertisements = read_advertisements('input.txt')
    filter_advertisements(advertisements)
    print_result_to_file(advertisements)


def run_test():
    cases = ('test_files/cases/input01.txt',
             'test_files/cases/input02.txt',
             'test_files/cases/input03.txt',
             'test_files/cases/input04.txt',
             'test_files/cases/input05.txt')

    expected_results = ('test_files/expected_results/output01.txt',
                        'test_files/expected_results/output02.txt',
                        'test_files/expected_results/output03.txt',
                        'test_files/expected_results/output04.txt',
                        'test_files/expected_results/output05.txt')

    for index in range(len(cases)):
        advertisements = read_advertisements(cases[index])
        filter_advertisements(advertisements)
        if not advertisements == read_advertisements(expected_results[index]):
            print("An error occurred in the test №" + str(index))
            return

    main()


run_test()
