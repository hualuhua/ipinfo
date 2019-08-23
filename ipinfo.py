from ipwhois import IPWhois
from ipwhois.net import Net
from ipwhois.asn import IPASN
import json
import requests
from config import *


def get_rdap(ipaddr):
    obj = IPWhois(ipaddr)
    RdapInfo = obj.lookup_rdap()

    if RdapInfo is None:
        return 0
    else :
        return RdapInfo

def get_nir(ipaddr):
    obj = IPWhois(ipaddr)
    NirInfo = obj.lookup_whois(inc_nir=True)

    if NirInfo is None:
        return 0
    else :
        return NirInfo

def get_whois(ipaddr):
    obj = IPWhois(ipaddr)
    WhoisInfo = obj.lookup_whois()

    if WhoisInfo is None:
        return 0
    else :
        return WhoisInfo
      
def get_asn(ipaddr):
    net = Net(ipaddr)
    obj = IPASN(net)
    AsnInfo = obj.lookup()

    if AsnInfo is None:
        return 0
    else :
        return AsnInfo

def get_abuseipdb(ipaddr):
    url = abuseipdbcheckurl
    querystring = {
        'ipAddress': ipaddr ,
        'maxAgeInDays': abuseipdbmaxAgeInDays
    }
    headers = {
        'Accept': 'application/json',
        'Key': abuseipdbkey
    }
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    abuseipdb_result = json.loads(response.text)
    if abuseipdb_result is None :
        return 0
    else :
        return abuseipdb_result

def get_ipinfo(ipaddr):
    if get_rdap(ipaddr) is not None:
        result = get_rdap(ipaddr)
        ipaddrinfo = {
            'method' : 'RDAP',
            'target' : result['query'],
            'network' : result['network']['cidr'],
            'country' : result['network']['country'],
            'name' : result['network']['name'],
            'asn_network' : result['asn_cidr'],
            'asn_country' : result['asn_country_code'],
            'asn_description' : result['asn_description'],
        }

    elif get_nir(ipaddr) is not None:
        result = get_rdap(ipaddr)
        ipaddrinfo = {
            'method' : 'NIR',
            'target' : result['query'],
            'network' : result['network']['cidr'],
            'country' : result['network']['country'],
            'name' : result['network']['name'],
            'asn_network' : result['asn_cidr'],
            'asn_country' : result['asn_country_code'],
            'asn_description' : result['asn_description'],
        }

    elif get_whois(ipaddr) is not None:
        result = get_whois(ipaddr)
        ipaddrinfo = {
            'method' : 'WHOIS',
            'target' : result['query'],
            'network' : result['nets'][0]['cidr'],
            'country' : result['nets'][0]['country'],
            'name' : result['nets'][0]['name'],
        }
    else :
        return 0

    ipaddrinfo = {
        'target' : result['query'],
        'network' : result['network']['cidr'],
        'country' : result['network']['country'],
        'name' : result['network']['name'],
    }
    
    if get_asn(ipaddr) is not None:
        asn_result = get_asn(ipaddr)
        
        ipaddrinfo['asn_number'] = asn_result['asn']
        ipaddrinfo['asn_cidr'] = asn_result['asn_cidr']
        ipaddrinfo['asn_country_code'] = asn_result['asn_country_code']
        ipaddrinfo['asn_description'] = asn_result['asn_description']


    if get_abuseipdb(ipaddr) is not None :
        abuseipdb_result = get_abuseipdb(ipaddr)

        ipaddrinfo['IPDB_domain'] = abuseipdb_result['data']['domain']
        ipaddrinfo['IPDB_abuseConfidenceScore']=abuseipdb_result['data']['abuseConfidenceScore']
        ipaddrinfo['IPDB_usageType']=abuseipdb_result['data']['usageType']
        ipaddrinfo['IPDB_isp']=abuseipdb_result['data']['isp']

    return ipaddrinfo

