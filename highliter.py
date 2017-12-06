import pdb
# import fileinput


def cycle_through_characters(
        chars='', current_char_index=0, count_dollar=0, location_dollar=0):
    a_found = False

    while current_char_index < len(chars) - 1 and not a_found:
        char = chars[current_char_index]
        print(char)

        # if char == '$' or char == 'A':
            # pdb.set_trace()

        if char == '$':
            count_dollar += 1
            location_dollar = current_char_index

        if count_dollar % 2 == 1 and char == 'A':
            a_found = True
            replace_character(
                location_char=current_char_index,
                location_dollar=location_dollar,
                chars=chars,
                count_dollar=count_dollar
            )
        current_char_index += 1


    # for counter in range(current_char_index, len(chars) - 1):
    #     char = chars[counter]

    #     if char == '$':
    #         count_dollar += 1
    #         location_dollar = counter

    #     if count_dollar % 2 == 1 and char == 'A':
    #         replace_character(
    #             location_char=counter,
    #             location_dollar=location_dollar,
    #             chars=chars)


def replace_character(location_char, location_dollar, chars, count_dollar):
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
    #     replace_character(
    #         location_char=location_char,
    #         location_dollar=location_dollar,
    #         chars=chars)

    if i == 'r':
        print('replacing things\n')
        write_to_file(location_char, location_dollar, chars)
        return
    elif i == 's':
        print('no replacmenet\n')
    elif i == 'b':
        pdb.set_trace()
    else:
        print('didn\'t understand')
        replace_character(location_char, location_dollar, chars)


def write_to_file(location_char, location_dollar, chars):
    string_to_write = '\\textcolor{green}{A}'

    new_chars = chars[:location_char - 1] + \
        string_to_write + chars[location_char + 1:]

    pdb.set_trace()

    new_location_char = location_char + len(string_to_write) - 1
    cycle_through_characters(
        chars=new_chars,
        current_char_index=new_location_char,
        count_dollar=1,
        location_dollar=location_dollar)



if __name__ == '__main__':
    file = open('pset1.tex', 'r+')
    chars = file.read()
    cycle_through_characters(chars=chars)
