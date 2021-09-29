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


def get_pres_bynumb(filename, number):
    file = open_file(filename, 'readlines')
    line = file[number]
    return line


def presidents_info(filename):
    file = open_file(filename, 'readlines')
    choice, instruction = p_user_choice()
    if instruction == 3:
        item = get_pres_bynumb(filename, choice)
        print(item)


presidents_info('presidents.txt')
