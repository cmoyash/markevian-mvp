raw_leads = [
    {"name": "Agency A", "score": 80},
    {"name": "Agency B", "score": 45}
]

main: list = []



for score in raw_leads:
    print(f"{score['name']} has score {score['score']}")

