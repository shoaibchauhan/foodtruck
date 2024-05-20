from typing import List
from fastapi import APIRouter, HTTPException, Query
from food_truck_finder.models import FoodCartDetail
from food_truck_finder.schema import DataOut
from geopy.distance import geodesic
from operator import itemgetter

# Create a new FastAPI router instance for handling food truck-related endpoints
food_truck_router = APIRouter()


# Function to find the nearest food carts based on provided latitude and longitude
def nearest_carts(latitude, longitude):
    # Check if the provided latitude and longitude are within valid ranges
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
        # Fetch all food cart details from the database
        all_trucks = FoodCartDetail.objects.filter().values('locationid', 'Latitude', 'Longitude', 'Applicant',
                                                            'Address', 'FoodItems')
        distances = []

        # Calculate the distance from the given location to each food truck
        for truck in all_trucks:
            truck_lat = truck['Latitude']
            truck_long = truck['Longitude']
            # Use geopy to calculate the distance between two geographical points
            dist = geodesic((latitude, longitude), (truck_lat, truck_long)).miles
            distances.append((truck['locationid'], dist))

        # Sort the list of distances in ascending order
        distances.sort(key=itemgetter(1))

        # Retrieve the top 5 nearest food truck location IDs
        nearest_locations = [loc_id for loc_id, _ in distances[:5]]
        # Fetch the detailed information of the nearest food trucks based on their location IDs
        detail_obj = FoodCartDetail.objects.filter(locationid__in=nearest_locations)
        return detail_obj
    else:
        # Raise an HTTP 400 error if the input latitude or longitude is invalid
        raise HTTPException(status_code=400, detail="Invalid Input")


# Define a GET endpoint to get the nearest food trucks based on provided latitude and longitude
@food_truck_router.get('/food', response_model=List[DataOut])
def get_food_truck(latitude: float = Query(...), longitude: float = Query(...)):
    # Call the nearest_carts function to get the nearest food trucks
    near_trucks = nearest_carts(latitude, longitude)
    return near_trucks
