


class Lead:

    source = "Linkdein"
    def __init__(self , website , industry , name):
        self.name =  name
        self.website = website
        self.industry = industry

    def display(self):
        print(f"Name: {self.name}\nWebsite: {self.website}\nIndustry: {self.industry}\nSource: {self.source}")


lead1 = Lead(name="Agency A", website="agencA.com", industry="Marketing")
lead2 = Lead(name="Agency B", website="agencB.com", industry="Sales")
lead3 = Lead(name="Agency C", website="agencC.com", industry="Tech")


leads = [lead1, lead2  , lead3]

for lead in leads:
    lead.display()
    print("")

