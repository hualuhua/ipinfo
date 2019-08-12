from ipinfo import * 
import pprint
import sys

args = sys.argv
ipaddr = args[1]

result = get_ipinfo(ipaddr)

print(result.items())
