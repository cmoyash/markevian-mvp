from models.lead_starategy import LeadStarategy


def search_agencies(city_name: str):
    if city_name.lower() == "mumbai":
        return [{"name" : "mumbai agency a " , "url" : "mumbaiageny.com"}]
    elif city_name.lower() == "delhi":
        return [{"name" : "delhi ageny b" , "url" :  "delhiageny.com" }]
    else:
        return "no data found"




test_strategy = LeadStarategy(
    target_industry="Digital Marketing Agencies",
    location="India",
    signals_to_research=["Hiring"],
    qualification_criteria=["Relevant services"]
)


def define_query(starategy: LeadStarategy):
    return f"{starategy.target_industry} in {starategy.location}"


result = define_query(test_strategy)
print(result)