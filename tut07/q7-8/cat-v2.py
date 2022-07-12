#! /usr/bin/env python3

import sys

print_line_num = False  # `-n` flag
print_all_chars = False  # `-v` flag

if ...:
    sys.exit(1)
    sys.exit(0)

# Check which options are provided
while len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    arg = sys.argv[1][1:]
    sys.argv.pop(1)
    if arg == 'v':
        print_all_chars = True
    elif arg == 'n':
        print_line_num = True

if len(sys.argv) == 1:
    sys.argv.append("-")

line_num = 1
for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        # Alternative way of reading files
        # with open(filename) as f:
        #     for line in f:
        #         print(line)

        for line in stream:
            if print_line_num:
                sys.stdout.write(f"{line_num:6}  ")

            if print_all_chars:
                new_line = ''
                # Translate each invisible character into a visible equivalent
                for char in line:
                    if ord(char) < 32:
                        new_line += "^" + chr(ord('A') + ord(char) - 1)
                    else:
                        new_line += char
                new_line = new_line.replace('^J', '$\n')
                sys.stdout.write(new_line)

            else:
                sys.stdout.write(line)

            line_num += 1

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
