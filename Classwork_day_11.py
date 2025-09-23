import json
from datetime import datetime
from tripdata import create_trip

trips = [
    create_trip("Paris", "15-05-2023", "Visited Eiffel Tower"),
    create_trip("Rome", "20-06-2023", "Enjoyed Italian food"),
    create_trip("London", "10-07-2023", "Saw the London Bridge")
]

def create_trip(city, date, comment):
    date_obj = datetime.strptime(date, "%d-%m-%Y")
    formatted_date = date_obj.strftime("%d-%m-%Y")
    return {
        "city": city,
        "date": formatted_date,
        "comment": comment
    }


trips_json = json.dumps(trips, indent=4)

print(trips_json)

