import requests
import json
import time

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



# print(f"{i}: {fetch_data(series_id)['title']}")
f = open('list.json', 'r')
list_data = json.loads(f.read())
print("xxxxx")
i = 0
file_data = "Title,Score,Image\n"
for line in list_data: 
    if line['series_type'] == 0 and line['status'] == 2:
        try:
            series_id = line['series_id']
            anime_data = fetch_data(series_id)
            title = anime_data['title']['english']
            if title == None: #"None"
                title = anime_data['title']['romaji']
            file_data += f"{title}, {line['score']}, {anime_data['coverImage']['large']} \n"
            print(f"Progress: {i+1} of {len(list_data)} lines done.")
        except Exception as e:
            print("Error occured, retrying in 60 seconds.")
            time.sleep(60)
            try:
                series_id = line['series_id']
                anime_data = fetch_data(series_id)
                title = anime_data['title']['english']
                if title == None: #"None"
                    title = anime_data['title']['romaji']
                file_data += f"{title},{line['score']},{anime_data['coverImage']['large']}\n"
                print(f"Progress: {i+1} of {len(list_data)} lines done.")
            except Exception as e:
                print(f"Another error occured. {e}")
    i += 1
    # if i == 183:
    #     print("Fuck yeah!")
try:
    with open("anime_data_for_graph.csv", "w") as f:
        f.write(file_data)
except Exception as e:
    print(f"Something went wrong. {e}")
f.close()