import requests
import json


endpoint = "https://api.clashofclans.com/v1"
token = ""
clan_search_query = input("Enter search query: ")






response = requests.get(endpoint + "/clans?name=" + clan_search_query, headers={"authorization": "Bearer " + token})

clan_info = response.text

clan_info = json.loads(clan_info)
nice_json = json.dumps(clan_info, indent=4, sort_keys=True)

if "message" in nice_json:
    print(nice_json)
    exit()


f = open('Clans/' + clan_search_query+" Clan Search Results.json", "w")
f.write(nice_json)

f.close()

count = nice_json.lower().split().count('"members":')
print(f"\n{count} Result(s)\n")

print("Done! Wrote results to " +"Clans/ "+clan_search_query+" Clan Search Results.json")
