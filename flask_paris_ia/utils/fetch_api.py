import requests

def get_paris_raw():
    url = "https://1xbet.com/LiveFeed/Get1x2_VZip?sports=85&count=50&lng=fr&gr=70&mode=4&country=96&getEmpty=true"
    response = requests.get(url)
    data = response.json()

    paris = []
    for match in data.get("Value", []):
        nom_match = f"{match['O1']} vs {match['O2']}"
        for e in match.get("E", []):
            paris.append({
                "match": nom_match,
                "type": e["T"],
                "groupe": e["G"],
                "param": e.get("P", 0),
                "cote": e["C"]
            })
        for ae in match.get("AE", []):
            for me in ae.get("ME", []):
                paris.append({
                    "match": nom_match,
                    "type": me["T"],
                    "groupe": me["G"],
                    "param": me.get("P", 0),
                    "cote": me["C"]
                })
    return paris
