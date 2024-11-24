import requests

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("type") == "single":
            return data["joke"]
        elif data.get("type") == "twopart":
            return f"{data['setup']} - {data['delivery']}"
        else:
            return "Une blague n'a pas pu être récupérée."
    except requests.RequestException as e:
        return f"Erreur lors de la récupération de la blague : {e}"

if __name__ == "__main__":
    joke = fetch_joke()
    print(f"Voici une blague pour vous :\n{joke}")





