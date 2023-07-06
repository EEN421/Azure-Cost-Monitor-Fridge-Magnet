import adafruit_requests as requests
import ssl
import json
import wifi
import socketpool


class azure:
    """
    Class used to represnt Azure
    ...
    Attributes:
    -----------
    app_id : str
        The application id from Azure
    password : str
        Secret generated by Azure for the application
    tenant_id : str
        Tenant id for the application
    subscription_id : str
        Azure subscription id
    ...
    Methods:
    --------
    cost_forecast()
        Returns the Azure cost forecast for the day
    """
    def __init__(self, app_id, password, tenant_id, subscription_id):
        """
        Parameters:
        -----------
        app_id : str
            The application id from Azure
        password : str
            Secret generated by Azure for the application
        Tenant_id : str
            tenant id for the application
        subscription_id : str
            Azure subscription id
        """
        self._app_id = app_id
        self._password = password
        self._tenant_id = tenant_id
        self._subscription_id = subscription_id
        pool = socketpool.SocketPool(wifi.radio)
        self._https = requests.Session(pool, ssl.create_default_context())

    def _error_handler(self, error):
        print(error['error'])

    def _get_token(self):
        data = {'grant_type': 'client_credentials',
                'client_id': self._app_id,
                'client_secret': self._password,
                'resource': 'https://management.azure.com/'
                }
        url = 'https://login.microsoftonline.com/{}/oauth2/token'\
              .format(self._tenant_id)
        response = self._https.post(url, data=data)
        json_resp = response.json()
        try:
            token = json_resp["access_token"]
        except KeyError as error:
            self._error_handler(error)
            quit()

        return token

    def cost_forecast(self):
        """
        Returns Azure cost forecast for the day
        """
        with open('./requestbody.json') as f:
            data = json.load(f)

        token = self._get_token()
        headers = {'Authorization': 'Bearer ' + token}

        url = 'https://management.azure.com/subscriptions/{}/providers/Microsoft.CostManagement/forecast?api-version=2019-10-01'\
              .format(self._subscription_id)

        response = self._https.post(url, json=data, headers=headers)
        json_resp = response.json()
        try:
            cost_forecast = json_resp["properties"]["rows"][0][0]
        except Exception:
            self._error_handler(json_resp)
            quit()

        return cost_forecast
