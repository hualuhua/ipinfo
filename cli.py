from ipinfo import * 
import pprint

result = get_ipinfo('8.8.8.8')

print(result.items())
