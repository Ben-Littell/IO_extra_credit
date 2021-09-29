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
    instructions = input(prompts.prompt_1)
    if instructions == '1':
        input_choice_1 = input(prompts.prompt_2)
        return input_choice_1
    elif intructions == '2':
        input_choice_2 = input(prompts.prompt_3)



p_user_choice()


def presidents_info(filename):
    file = open_file(filename, 'readlines')
    print(file)


# presidents_info('presidents.txt')
