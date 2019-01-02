from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username='username'
password = 'password'
url = 'http'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)

auth_handler = HTTPBasicAuthHandler(p)

