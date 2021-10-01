# EXTRA CREDIT
import prompts


def open_file(filename, mode='read'):
    with open(filename, 'r') as file:
        if mode == 'read':
            text = file.read()
        elif mode == 'readlines':
            text = file.readlines()
        elif mode == 'readline':
            text = file.readline()
        return text


def p_user_choice():
    run = True
    while run:
        instructions = input(prompts.prompt_1)
        if instructions == '1':
            input_choice_1 = input(prompts.prompt_2)
            run = False
            return input_choice_1, instructions
        elif instructions == '2':
            input_choice_2 = input(prompts.prompt_3)
            run = False
            return input_choice_2, instructions
        elif instructions == '3':
            input_choice_3 = input(prompts.prompt_4)
            run = False
            return input_choice_3, instructions
        else:
            print('Try again')


def get_pres_by_numb(filename, number):
    file = open_file(filename, 'readlines')
    line = file[number]
    return line


def get_office_date(filename, name):
    file = open_file(filename, 'readlines')
    for line in file:
        split_line = line.split(',')
        if name.lower() == split_line[1].lower():
            c_line = split_line
            return c_line[3]

# get_office_date('presidents.txt', 'John Adams')
######


def year_to_pres(filename, year):
    file = open_file(filename, 'readlines')
    name = []
    for line in file:
        split_line = line.split(',')
        for item in split_line[3].split('-'):
            if year == item:
                name.append(split_line[1])
    return name


# test = year_to_pres('presidents.txt', '1797')
# print(test)


def presidents_info(filename):
    choice, instruction = p_user_choice()
    if instruction == '1':
        item = get_office_date(filename, choice)
        return item
    elif instruction == '2':
        item = year_to_pres(filename, choice)
        return item
    elif instruction == '3':
        item = get_pres_by_numb(filename, int(choice))
        item_s = item.split(',')
        return item_s[1]


# test = presidents_info('presidents.txt')
# print(test)
