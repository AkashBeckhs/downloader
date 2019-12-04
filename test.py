import requests
cert_file_path = "C:\\Users\\aakash\\Documents\\Project Documents\\FacialRecongnition\\AWS\\POC\\client_certificate_api_gateway\\ca.pem"
key_file_path = "C:\\Users\\aakash\\Documents\\Project Documents\\FacialRecongnition\\AWS\\POC\\client_certificate_api_gateway\\pubkey.pem"

proxies= { "http"  : "http://10.135.0.26:8080/ ", 
           "https" : "http://10.135.0.26:8080/ " 
        }
url = "https://soprasteriamobility.com/fetch/587422"
cert = (cert_file_path)
r = requests.get(url, cert=cert, verify=False,proxies=proxies)
