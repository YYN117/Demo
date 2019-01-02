# -*- coding:utf-8 -*-
from urllib import request
from urllib import parse
import json

if __name__ == '__main__':
    Request_URL = 'http://fanyi.youdao.com/translate'
    Form_Data = {}

    Form_Data['i'] = 'FUCK'

    Form_Data['type'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1539848136187'
    Form_Data['sign'] = '266c9475529d474616f407ca8d566558'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'
    Form_Data['typoResult'] = 'false'
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    print(html)
    translate_results = json.loads(html)
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print('翻译结果是： %s'% translate_results)
