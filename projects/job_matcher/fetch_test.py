import requests

url = "https://remotive.com/api/remote-jobs?category=software-dev&limit=5"

res = requests.get(url)

data = res.json()

for job in data["jobs"][: 5]:
    print((job["title"], job["company_name"]))