
import requests 
import json, math
from datetime import datetime
api_key = 'key auth v3'
username = 'username'
password = 'password'

start_execution = datetime.now()
minutos = 0
movies = 0
sessions = 0
episodes = 0
string_file = ''
file= open("Resultado.txt","w+")

def horas(total_minutes, format = 'horas'):
    if format == 'horas':
        return("%02d:%02d" % (divmod(total_minutes, 60)))

    days = math.floor(total_minutes / (24*60))
    leftover_minutes = total_minutes % (24*60)
    
    hours = math.floor(leftover_minutes / 60)
    mins = total_minutes - (days*1440) - (hours*60)

    out = '{} Dias {} Hrs {} Min'.format(days, hours, mins)
    return out

def request(tipo, url, headers, payload):
    if tipo == 'GET':
        response = requests.get(url)
        return response.json()

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def allpages(type = 'tv', page = '1', s = ''):
    if type == 'movie':
        type = 'movies'

    url = 'https://api.themoviedb.org/3/account/{account_id}/rated/'+type+'?api_key='+api_key+'&language=pt-BR&session_id='+s+'&sort_by=created_at.desc&page='+str(page)
    response = request('GET',url,'','')
    return response
    
request_token = request('GET','https://api.themoviedb.org/3/authentication/token/new?api_key=' +  api_key,'','')['request_token']
payload = json.dumps({
  "username": username,
  "password": password,
  "request_token": ''+request_token+''
})
headers = {
  'Content-Type': 'application/json'
}
request('POST','https://api.themoviedb.org/3/authentication/token/validate_with_login?api_key=' +  api_key,headers,payload)

payload = json.dumps({
  "request_token": request_token
})
headers = {
  'Content-Type': 'application/json'
}

session_id = request('POST','https://api.themoviedb.org/3/authentication/session/new?api_key=' +  api_key,headers,payload)['session_id']

print(f"TIPO: \tTEMPO \tVOTO|MEDIA \tTITULO TEMPORADA EPISODIOS")

all_types = ['movie','tv']
for schema in all_types:
    total_pages = allpages(schema,'1', session_id)['total_pages']
    for i in range(1,(total_pages+1)):
        all = allpages(schema,str(i), session_id)
        for tvs in all['results']:
            tv = request('GET','https://api.themoviedb.org/3/'+schema+'/'+str(tvs['id'])+'?api_key='+api_key+'&language=pt-BR','','')
            episode =''
            if schema =='tv':
                episodes = episodes + tv['number_of_episodes']
                sessions = sessions +1
                try:
                    tempo = (tv['episode_run_time'][0] * tv['number_of_episodes'])
                    title = tv['name']
                    episode = f"| Sessions: {tv['number_of_seasons']} Episodes: {tv['number_of_episodes']}"
                except:
                    print(f"Error {str(tv['id'])}")
                    tempo = 0
                    title = tv['name']
            if schema == 'movie':
                movies = movies+1
                try:
                    tempo = tv['runtime']
                    title = tv['title']
                except:
                    tempo = 0
                    title = tv['title']

            minutos = minutos + tempo
            total = horas(minutos, 'dias')

            print(f"{schema}: \t{horas(tempo)} \t{tvs['rating']:04}|{tvs['vote_average']:04} \t{title} {episode}")
            string_file = string_file + (f"{schema}: \t{horas(tempo)} \t{tvs['rating']:04}|{tvs['vote_average']:04} \t{title} {episode}\n")


end_execution = datetime.now()
duration = end_execution-start_execution
file.write(f"RELATORIO FINAL")
file.write(f"\n- Excecução: \t\t\t{duration}")
file.write(f"\n- Tempo Assistido: \t\t{total}")
file.write(f"\n- Total de Filmes: \t\t{movies}")
file.write(f"\n- Total de Series: \t\t{sessions} ")
file.write(f"\n- Total de Episodios: \t{episodes} ")
file.write(f"\n\nLISTA GERAL")
file.write(f"\nTIPO: \tTEMPO \tVOTO|MEDIA \tTITULO TEMPORADA EPISODIOS")
file.write(f"\n{string_file}")
file.close()
