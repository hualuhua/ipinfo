from ipwhois import IPWhois
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
    decodedResponse = json.loads(response.text)

    if decodedResponse is None:
        return 0
    else :
        return decodedResponse

