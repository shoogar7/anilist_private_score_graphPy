import requests
import json

def fetch_data(series_id):
    query = '''
    query ($id: Int) {#Defining which variables will be used in the query (id)
    Media (id: $id, type: ANIME) {#Inserting variables into query arguments (id)
    title{
        romaji
        english
        }
    coverImage{
        large
    }
    }
    }
    '''

    #Define query variables and values used in query request
    variables = {
        'id': series_id
    }

    url = 'https://graphql.anilist.co'

    #HTTP Api request
    #TRY EXCEPT?
    response = requests.post(url, json={'query': query, 'variables': variables})
    return response.json()['data']['Media']

# print(response.text)
# data = response.json()['data']['Media']
# print(data['title'], data['coverImage'])

f = open('list.json', 'r')
list_data = json.loads(f.read())
print("xxxxx")
i = 0
for line in list_data:
    series_id = line['series_id'] 
    print(fetch_data(series_id))
    fetch_data(series_id)
    i += 1
    if i == 20:
        break
f.close()