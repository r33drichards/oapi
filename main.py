from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

configuration = swagger_client.Configuration()

configuration.api_key = "ol_api_rR5xQ5s3Ew1RyDJR5shCqw79dJPo8kgD6X8vbI"


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))


api_response = api_instance.documents_list_post()
pprint(api_response)