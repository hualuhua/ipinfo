from flask import Flask, jsonify, request, render_template
from ipinfo import *

app = Flask(__name__)

@app.route("/get_whois/<ipaddr>", methods=["GET"])
def get_result(ipaddr):
    rdap_result = get_rdap(ipaddr)
    if rdap_result is not None:
        result = {
            'target' : rdap_result['query'],
            'rdap_network' : rdap_result['network']['cidr'],
            'rdap_country' : rdap_result['network']['country'],
            'rdap_name' : rdap_result['network']['name'],
            'rdap_asn_network' : rdap_result['asn_cidr'],
            'rdap_asn_country' : rdap_result['asn_country_code'],
            'rdap_asn_description' : rdap_result['asn_description'],
        }
    else :
        nir_result = get_nir(ipaddr)
        if nir_result is not None:
            result = {
                'target' : nir_result['query'],
                'nir_asn_network' : nir_result['asn_cidr'],
                'nir_asn_country' : nir_result['asn_country_code'],
                'nir_asn_description' : nir_result['asn_description'],
            }

    abuseipdb_result = get_abuseipdb(ipaddr)
    if abuseipdb_result is not None:
        result['IPDB_domain'] = abuseipdb_result['data']['domain']
        result['IPDB_abuseConfidenceScore']=abuseipdb_result['data']['abuseConfidenceScore']
        result['IPDB_usageType']=abuseipdb_result['data']['usageType']
    return result, 200

@app.route("/ipinfo/<ipaddr>", methods=["GET"])
def get_ipinfo(ipaddr):
    if get_rdap(ipaddr) is not None:
        rdap_result = get_rdap(ipaddr)
        ipaddrinfo = {
            'target' : rdap_result['query'],
            'network' : rdap_result['network']['cidr'],
            'country' : rdap_result['network']['country'],
            'name' : rdap_result['network']['name'],
            'asn_network' : rdap_result['asn_cidr'],
            'asn_country' : rdap_result['asn_country_code'],
            'asn_description' : rdap_result['asn_description'],
        }
    
    elif get_nir(ipaddr) is not None:
        ipaddrinfo = {
            'target' : nir_result['query'],
            'nir_asn_network' : nir_result['asn_cidr'],
            'nir_asn_country' : nir_result['asn_country_code'],
            'nir_asn_description' : nir_result['asn_description'],
        }
    
    else :
        return 0
    
    if get_abuseipdb(ipaddr) is not None :
        abuseipdb_result = get_abuseipdb(ipaddr)
        
        ipaddrinfo['IPDB_domain'] = abuseipdb_result['data']['domain']
        ipaddrinfo['IPDB_abuseConfidenceScore']=abuseipdb_result['data']['abuseConfidenceScore']
        ipaddrinfo['IPDB_usageType']=abuseipdb_result['data']['usageType']
    
    return render_template("ipinfo.tpl.html", ipaddrinfo = ipaddrinfo), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
