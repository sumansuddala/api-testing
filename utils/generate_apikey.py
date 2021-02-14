import requests
import json

# To generate apikey
def gen_apikey(organization, emailid):
    url = 'https://www.alphavantage.co/create_post/'
    # Adding request parameters to payload
    payload = {
        "first_text": "deprecated",
        "last_text": "deprecated",
        "occupation_text": "Investor",
        "organization_text": "deshaw",
        "email_text": "ssuman.testengineer@gmail.com"
        }
    # Adding header as parameters are being sent in payload
    headers = {
        ':authority': 'www.alphavantage.co',
        ':method': 'POST',
        ':path': '/create_post/',
        ':scheme': 'https',
        'accept': '*/*'
    }
    try:
        #r = requests.post(url, data=json.dumps(payload), headers=json.dumps(headers))
        #resp = r.content
        # Mocking the result, since we are not triggering the service.
        resp = '{"result": "Create post successful!", "text": "Welcome to Alpha Vantage! Here is your API key: EALJNHPOH59FX98P. Please record this API key at a safe place for future data access."}'
        resp = resp.split('API key: ')
        resp = resp[1].split('.')
        apikey = resp[0]
        return apikey

    except:
        print("Oops!", sys.exc_info()[0], "occurred.")






