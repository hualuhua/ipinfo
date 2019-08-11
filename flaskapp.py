from flask import Flask, jsonify, request
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

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
