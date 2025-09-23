from datetime import datetime
from tracker import travel_record
import json

records = [
    travel_record ("Munnar", "January 28,2003" ,"Visited Tea Factory"),
    travel_record ("Kochi", "february 28,2025" ,"Visited Fort Kochi"),
    travel_record ("Varkala", "November 16,2010" ,"Visited Beach")    
]
def travel_record(city, date, comment):
    date_obj = datetime.strptime(date, "%b %d,%Y")
    formatted_date = date_obj.strftime("%b %d,%Y")
    return {
        "city": city,
        "date": formatted_date,
        "comment": comment
    } 
json_data = json.dumps(records, indent=4)
print(json_data)

parsed_records = json.loads(json_data)

print("\nParsed Records:")
for record in parsed_records:
    print(f"City: {record['city']}, Date: {record['date']}, Comment: {record['comment']}")
