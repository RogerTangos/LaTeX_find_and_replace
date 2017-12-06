import pdb
# import fileinput


def cycle_through_file(start_char=0, count_dollar=0, location_dollar=0):
    file = open('pset1.tex', 'r+')

    chars = file.read()

    for counter in range(start_char, len(chars) - 1):
        char = chars[counter]

        if char == '$':
            count_dollar += 1
            location_dollar = counter

        if count_dollar % 2 == 1 and char == 'A':
            a_found(
                location_a=counter,
                location_dollar=location_dollar,
                chars=chars)


def a_found(location_a, location_dollar, chars):
    offset = location_a - location_dollar + 3

    printer = ' ' * offset + '^'

    print(chars[location_a - offset:location_a + offset])
    print(printer)

    print (
        'char ' +
        str(location_a) +
        ': (r)eplace, (s)kip, (i)ncrement, or (b)reak into debugger')

    i = raw_input('--> ')

    # if i == 'i':
    #     count_dollar += 1
    #     print('number of dollar signs now ') + str(count_dollar)
    #     a_found(
    #         location_a=location_a,
    #         location_dollar=location_dollar,
    #         chars=chars)

    if i == 'r':
        print('replacing things\n')
        write_to_file()
    elif i == 's':
        print('no replacmenet\n')
    elif i == 'b':
        pdb.set_trace()
    else:
        print('didn\'t understand')
        a_found()


def write_to_file(position):
    print('write to file')
    # insert your color string into the file

if __name__ == '__main__':
    cycle_through_file()
