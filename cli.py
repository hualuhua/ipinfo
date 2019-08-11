from ipinfo import * 
import pprint

rdap_result = get_rdap('8.8.8.8')

result = {
    'target' : rdap_result['query'],
    'rdap_network' : rdap_result['network']['cidr'],
    'rdap_country' : rdap_result['network']['country'],
    'rdap_name' : rdap_result['network']['name'],
    'rdap_asn_network' : rdap_result['asn_cidr'],
    'rdap_asn_country' : rdap_result['asn_country_code'],
    'rdap_asn_description' : rdap_result['asn_description'],
}


print(result.items())
