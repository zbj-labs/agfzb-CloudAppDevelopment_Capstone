# INSTRUCTIONS
# 1. Replace the string with your own IAM API key
# 2. Replace the string with your own Couch URL
# 3. Invoke w/ parameters: {"id": "15"}

# docs:
# https://ibm.github.io/cloudant-python-sdk/docs/0.0.32/ibmcloudant.html#module-ibmcloudant.cloudant_v1
# https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-databases&code=python

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    authenticator = IAMAuthenticator("Your IAM API key")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("Your Couch URL")

    dealer_id = dict["dealerId"]
    if dealer_id == "":
        response = service.post_all_docs(
            db='reviews',
            include_docs = True,
            limit = 10
        ).get_result()
    else:
        response = service.post_find(
            db='reviews',
            selector={'dealership': {'$eq': int(dict["dealerId"])}},
        ).get_result()

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
