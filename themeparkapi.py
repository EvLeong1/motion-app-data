
import time
import openapi_client
from pprint import pprint
from openapi_client.api import destinations_api
from openapi_client.api import entities_api
from openapi_client.model.destinations_response import DestinationsResponse
# Defining the host is optional and defaults to https://api.themeparks.wiki/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themeparks.wiki/v1"
)


parkList = []
# Get park ids
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destinations_api.DestinationsApi(api_client)
    

    try:
        # Get a list of supported destinations available on the live API
        api_response = api_instance.get_destinations().destinations
        
        for park in api_response:
            parkList.append(park.slug)
            # print(park)
        # print(api_response.destinations[0].name)
    except openapi_client.ApiException as e:
        print("Exception when calling DestinationsApi->get_destinations: %s\n" % e)
        
print(parkList)

#Get Ride Data from a specific park 
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entities_api.EntitiesApi(api_client)
    for park in parkList:
        
        entity_id = park 
        
        try:            
            park = api_instance.get_entity_children(entity_id)
            for ride in park.children:
                print(f'"{ride.name}", "{park.name}", "{park.name}_{ride.name}"')
                print('\n')
            # print(park.name)
            
        except openapi_client.ApiException as e:
            print("Exception when calling EntitiesApi->get_entity_children: %s\n" % e)