#!/usr/bin/python3
"""Log parsing"""

import sys


expected_status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
status_code_counts = 0

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in expected_status_codes.keys():
                expected_status_codes[code] += 1
            total_size += size
            status_code_counts += 1

        if status_code_counts == 10:
            print("File size: {}".format(total_size))
            for key, value in sorted(expected_status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            status_code_counts = 0

except KeyboardInterrupt:
    pass

finally:
    print('File size:{}'.format(total_size))
    for key, value in sorted(expected_status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
