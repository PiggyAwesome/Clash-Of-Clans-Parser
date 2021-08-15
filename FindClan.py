import requests
import json


endpoint = "https://api.clashofclans.com/v1"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImU0NzU2OGFhLThlYWItNDNlZS1hYTBiLTIxOTMxMmM2NjMxOCIsImlhdCI6MTYyODk0MzU4MSwic3ViIjoiZGV2ZWxvcGVyLzgxYjcwNTNkLWE1ZGYtN2E3My1mZWFjLTRkZTI3YTgzMWY2NSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMi4xMzAuODAuNyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.prkJFqbVg5nEfD6gjiLmjyL_iqo3wfqrd6bjXXvrKapaRYt_7FZgo7sgpGfKk0MOcfksIQGEAUJJ_IJpb71pSQ"

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
