import urllib.request
import json

token = (
'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTQ1ODM3NDIs'
'InR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJoaXBwYXN1c29mbWV0YXBvbnR1b'
'UBnbWFpbC5jb20ifQ.n21k9Yl6LeO6Xa1LUgSYqOwdLWNclHb0LecZtO7FJnQ'
'tcvf7cZV95gDfQQ69nlHDtB88E2ZaX9I_9GWSn_8WmA')

header = {'Authorization': 'BEARER {}'.format(token)}

consultas = ['base', 'base_usd', 'reservas', 'base_div_res', 'usd', 'usd_of',
            'usd_of_minorista', 'var_usd_vs_usd_of', 'circulacion_monetaria']

link = 'https://api.estadisticasbcra.com/base'

req = urllib.request.Request(link, headers=header)
html = urllib.request.urlopen(req).read()

json = json.loads(html)
for value in json[:5]:
    print(value)
