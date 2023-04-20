import requests

appname = 'N5XU-FOX'

def get(callsign):
    
    try:
        response = requests.get(f'http://api.hamdb.org/{callsign}/JSON/{appname}')
        response.raise_for_status()

        jsonResponse = response.json()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    if jsonResponse['hamdb']['messages']['status'] == 'OK':
        return jsonResponse
    else:
        return None
    
if __name__ == '__main__':
    print(get('KN4LRA'))
