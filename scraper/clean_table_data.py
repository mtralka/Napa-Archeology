import json


def main():
    result = []

    with open("./archeo-data.json") as f:
        data = json.load(f)
        
        for r in data["Items"]:
            id = r["id"]["S"]
            status = int(r["status"]["N"])
            result.append({"id" : id, "status": status})

    with open('clean-archeo-data.json', 'w') as f:
        json.dump(result, f)

if __name__ == "__main__":
    main()
