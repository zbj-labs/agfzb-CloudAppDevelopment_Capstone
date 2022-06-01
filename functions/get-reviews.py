# INSTRUCTIONS
# 1. Replace the string with your own IAM API key
# 2. Replace the string with your own Couch URL
# 3. Invoke w/ parameters: {"id": "15"}

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    authenticator = IAMAuthenticator("Your IAM API key")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("Your Couch URL")
    response = service.post_find(
    db='reviews',
    selector={'dealership': {'$eq': int(dict["id"])}},
    ).get_result()
    try:
        # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }
