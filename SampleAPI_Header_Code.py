#sample Header code in python for header authentication
#Authentication

#Authenticating your API requests is done by sending a HTTP Header called: X-API-KEY with the value being your API Key which you got by following the Get your API Key instructions.

#Here are some relevant snippits of sample code showing this to give you the idea.
#Authentication example using Python & the Requests Module

import requests
headers = {
    '_7l3tcaVyqh_dzSUdP2P79g': config.api_key,
}
result = requests.post(api_url, data=json.dumps(post_data), headers=headers)
