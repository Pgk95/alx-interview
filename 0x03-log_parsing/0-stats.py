#!/usr/bin/python3
"""Log parsing"""

import sys

expected_status_codes = {'200', '301', '400', '401',
                         '403', '404', '405', '500'}

total_size = 0
status_code_counts = {code: 0 for code in sorted(expected_status_codes)}

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()

        if line.startswith('"GET /projects/260 HTTP/1.1"'):
            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[7]
                if status_code in expected_status_codes:
                    line_count += 1
                    total_size += int(parts[-1])
                    status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in status_code_counts.items():
                if count > 0:
                    print(f"{code}: {count}")
except KeyboardInterrupt:
    pass
