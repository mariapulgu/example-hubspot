# Starting November 30, 2022, API keys will be sunset as an authentication method. Learn more about this change: https://developers.hubspot.com/changelog/upcoming-api-key-sunset and how to migrate an API key integration: https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app to use a private app instead.
import hubspot
from pprint import pprint
from hubspot.crm.contacts import ApiException

client = hubspot.Client.create(access_token="pat-na1-f6c11c89-097c-4983-b482-9991ba3c2696")

try:
    api_response = client.crm.contacts.basic_api.get_page(limit=10, archived=False)
    #pprint(api_response)
    pprint(api_response.results[0].properties)
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)