# INSTRUCTIONS
# 1. Replace the string with your own IAM API key
# 2. Replace the string with your own Couch URL

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator("Your IAM API key")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("Your Couch URL")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
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