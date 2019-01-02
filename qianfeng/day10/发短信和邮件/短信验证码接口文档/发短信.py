






# ！/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib

host = '106.ihuyi.com'
sms_send_uri = '/webservice/sms.php?method=Submit'

#
account = 'C58023834'

password = '32dc4c13668beeb673ba91202d61405d'


def send_sms(text,mobile):
    params = urllib.parse.urlencode({'account':account,'password':password,'content':text,'mobile':mobile,'format':'json'})
    headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
    conn = http.client.HTTPConnection(host,port=80,timeout=30)
    conn.request('POST',sms_send_uri,params,headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = '18260032928'
    text = '12345'

    print(send_sms(text,mobile))
