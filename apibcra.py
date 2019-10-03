import urllib.request
import json

token = (
        'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTQ1ODM3NDIsInR5c'
        'GUiOiJleHRlcm5hbCIsInVzZXIiOiJoaXBwYXN1c29mbWV0YXBvbnR1bUBnbWFpbC5j'
        'b20ifQ.n21k9Yl6LeO6Xa1LUgSYqOwdLWNclHb0LecZtO7FJnQtcvf7cZV95gDfQQ69n'
        'lHDtB88E2ZaX9I_9GWSn_8WmA')

header = {'Authorization': 'BEARER {}'.format(token)}

link = 'https://api.estadisticasbcra.com/'
consultas = ['base', 'base_usd', 'reservas', 'base_div_res', 'usd', 'usd_of',
            'usd_of_minorista', 'var_usd_vs_usd_of', 'circulacion_monetaria']

for cons in consultas:
    nlink = link + cons
    archivo = cons + '.json'
    print('Obteniendo {}, y generando archivo {}\n'.format(nlink, archivo))
    req = urllib.request.Request(nlink, headers=header)
    html = urllib.request.urlopen(req).read()
    file = open(archivo, 'w')
    data = json.loads(html)
    file.write(json.dumps(data))
