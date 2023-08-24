#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import re
import sys

if __name__ == '__main__':
    try:
        regex = re.compile(r'\d+.\d+.\d+.\d+ - \[\d+-\d+\d+-\d+ \d+:\d+:\d+\.\d+\] \"GET \/projects\/260 HTTP\/1\.1\" (\d+) (\d+)')
        sum_file_size = 0
        code_occurencies = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
        }
        while True:
            for i in range(10):
                line = input()
                code = int(regex.match(line).group(1))
                code_occurencies[code] += 1
                file_size = regex.match(line).group(2)
                sum_file_size += int(file_size)

            print('File size: {}'.format(sum_file_size))

            for code_occurency in code_occurencies:
                if (code_occurencies[code_occurency] != 0):
                    print(
                        f'{code_occurency}: {code_occurencies[code_occurency]}'
                    )

            sys.stdin.flush()
    except KeyboardInterrupt as k:
        for i in range(10):
            code = int(regex.match(line).group(1))
            code_occurencies[code] += 1
            file_size = regex.match(line).group(2)
            sum_file_size += int(file_size)

        print('File size: {}'.format(sum_file_size))

        for code_occurency in code_occurencies:
            if (code_occurencies[code_occurency] != 0):
                print(f'{code_occurency}: {code_occurencies[code_occurency]}')

        sys.stdin.flush()
    except ValueError as v:
        print('Status code or File size is not a number :(')
