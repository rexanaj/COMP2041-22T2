#! /usr/bin/env python3

import sys

print_line_num = False

if len(sys.argv) > 1 and sys.argv[1] == '-n':
    print_line_num = True
    sys.argv.pop(1)

if len(sys.argv) == 1:
    sys.argv.append("-")

line_num = 1
for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line in stream:
            if print_line_num:
                sys.stdout.write(f"{line_num:6}  {line}")
            else:
                sys.stdout.write(line)
            line_num += 1

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
