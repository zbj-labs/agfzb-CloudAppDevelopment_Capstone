#!/bin/sh
curl -X POST -u "apikey:$NLU_API_KEY" -H "Content-Type: application/json" -d @parameters.json "https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/8d771966-5e4e-446b-a87d-020098e53e3a/v1/analyze?version=2022-04-07"
