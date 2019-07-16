#!/usr/bin/env python3

import requests

response = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')

# aws_ranges.keys()
#   - syncToken
#   - createDate
#   - prefixes
#   - ipv6_prefixes
#

aws_ranges = response.json()
aws_ipv4 = aws_ranges['prefixes']
aws_ipv6 = aws_ranges['ipv6_prefixes']

print('Ranges:')
print('  createDate: ' + aws_ranges['createDate'])
print('  syncToken:  ' + aws_ranges['syncToken'])
print('  ipv4:       ' + str(len(aws_ipv4)))
print('  ipv6:       ' + str(len(aws_ipv6)))
print()

exit(0)

for item in aws_ipv4:
    msg = '  - prefix: ' + item['ip_prefix']
    msg = msg + ' ' + item['region'] + ' ' + item['service']
    print(msg)


