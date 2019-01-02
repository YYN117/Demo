from yynSql import yyn

s = yyn('localhost','root','1234','kaige')

res = s.get_all('select*from bandcard where money>400')
for row in res:
    print('{}--{}'.format(row[0],row[1]))