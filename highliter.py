import pdb
# import fileinput

CHAR_TO_FIND = 'A'
REPLACEMENT_STRING = '\\textcolor\{green\}\{A\}'
NEW_FILENAME = 'xkcd.tex'


def cycle_through_characters(
        chars='', current_char_index=0, count_dollar=0, location_dollar=0):
    a_found = False

    while current_char_index < len(chars) - 1 and not a_found:
        char = chars[current_char_index]
        # print(char)

        if char == '$':
            count_dollar += 1
            location_dollar = current_char_index

        if count_dollar % 2 == 1 and char == CHAR_TO_FIND:
            a_found = True
            menu(
                location_char=current_char_index,
                location_dollar=location_dollar,
                chars=chars,
                count_dollar=count_dollar
            )

        current_char_index += 1

    if current_char_index == len(chars) - 1:
        output_to_new_file(chars=chars)


def menu(location_char, location_dollar, chars, count_dollar):
    offset = location_char - location_dollar + 3

    printer = ' ' * offset + '^'

    print(chars[location_char - offset:location_char + offset])
    print(printer)

    print(
        'char ' +
        str(location_char) +
        ': (r)eplace, (s)kip, (i)ncrement, or (b)reak into debugger')

    i = raw_input('--> ')

    # if i == 'i':
    #     count_dollar += 1
    #     print('number of dollar signs now ') + str(count_dollar)
    #     menu(
    #         location_char=location_char,
    #         location_dollar=location_dollar,
    #         chars=chars)

    if i == 'r':
        print('replacing things\n')
        replace_characters(location_char, location_dollar, chars)
        return
    elif i == 's':
        print('no replacmenet\n')
    elif i == 'b':
        pdb.set_trace()
    else:
        print('didn\'t understand')
        menu(location_char, location_dollar, chars, count_dollar)


def replace_characters(location_char, location_dollar, chars):
    new_chars = chars[:location_char - 1] + \
        REPLACEMENT_STRING + chars[location_char + 1:]

    new_location_char = location_char + len(REPLACEMENT_STRING) - 1
    cycle_through_characters(
        chars=new_chars,
        current_char_index=new_location_char,
        count_dollar=1,
        location_dollar=location_dollar)


def output_to_new_file(chars=''):
    f = open(NEW_FILENAME, 'w+')
    pdb.set_trace()
    f.write(chars)
    f.close()


def initial_prompt():
    print('What file are you doing find and replace in?')
    filename = raw_input('--> ')

    print('what do you wnat your new file to be named?')
    globals()['NEW_FILENAME'] = raw_input('--> ')

    print('What character are you searching for (in formulas)?')
    globals()['CHAR_TO_FIND'] = raw_input('--> ')

    print('What do you want to replace it with?')
    globals()['REPLACEMENT_STRING'] = raw_input('--> ')

    print('You have chosen to replace "%s" with "%s" in file "%s". '
          'Output will be written to "%s". '
          'Is this correct? (Y/N)'
          % (CHAR_TO_FIND, REPLACEMENT_STRING, filename, NEW_FILENAME))

    correct = raw_input('--> ').lower()

    if correct == 'y':
        print('\n---running program---')
        file = open(filename, 'r+')

        chars = file.read()
        cycle_through_characters(chars=chars)
    else:
        print('\n---reprompting---')
        initial_prompt()


if __name__ == '__main__':
    initial_prompt()
