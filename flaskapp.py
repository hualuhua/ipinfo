from flask import Flask, jsonify, request, render_template
from ipinfo import *

app = Flask(__name__)

@app.route("/ipinfo/json/<ipaddr>", methods=["GET"])
def output_ipinfo_json(ipaddr):
    result = get_ipinfo(ipaddr)
    return result, 200

@app.route("/ipinfo/<ipaddr>", methods=["GET"])
def output_ipinfo_html(ipaddr):
    result = get_ipinfo(ipaddr)
    return render_template("ipinfo.tpl.html", ipaddrinfo = result), 200

#@app.route("/ipinfo/<ipaddr>", methods=["GET"])
#def get_ipinfo(ipaddr):
#    if get_rdap(ipaddr) is not None:
#        result = get_rdap(ipaddr)
#    elif get_nir(ipaddr) is not None:
#        result = get_rdap(ipaddr)
#    else :
#        return 0
#
#    ipaddrinfo = {
#        'target' : result['query'],
#        'network' : result['network']['cidr'],
#        'country' : result['network']['country'],
#        'name' : result['network']['name'],
#        'asn_network' : result['asn_cidr'],
#        'asn_country' : result['asn_country_code'],
#        'asn_description' : result['asn_description'],
#    }
#    
#    if get_abuseipdb(ipaddr) is not None :
#        abuseipdb_result = get_abuseipdb(ipaddr)
#        
#        ipaddrinfo['IPDB_domain'] = abuseipdb_result['data']['domain']
#        ipaddrinfo['IPDB_abuseConfidenceScore']=abuseipdb_result['data']['abuseConfidenceScore']
#        ipaddrinfo['IPDB_usageType']=abuseipdb_result['data']['usageType']
#    
#    return render_template("ipinfo.tpl.html", ipaddrinfo = ipaddrinfo), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
