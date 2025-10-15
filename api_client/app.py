import datetime
from functools import wraps

import openapi_client

from openapi_client.api.authentication_api import AuthenticationApi
from openapi_client.api.data_connect_api import DataConnectApi
from openapi_client.models.connect_parameters import ConnectParameters


class ApiClient(object):
    # Credentials
    partner_id = "{{partnerId}}"
    partner_secret = "{{partnerSecret}}"
    app_key = "{{appKey}}"

    # API Client
    api_client = None

    # Token details
    token = None
    expiry = None

    @classmethod
    def __init__(self):
        conf = openapi_client.Configuration()
        conf.verify_ssl = False
        conf.ssl_ca_cert = None
        conf.assert_hostname = False
        conf.cert_file = None

        api_client = openapi_client.ApiClient(conf)
        self.add_authentication(self=self, api_client=api_client)
        self.api_client = api_client

    def add_authentication(self, api_client):
        api_client.rest_client.request = self.authenticate(self, api_client.rest_client.request)

    def authenticate(self, func):
        @wraps(func)
        def call_api_function(*args, **kwargs):
            kwargs['headers']['Finicity-App-Key'] = self.app_key
            if self.expiry is None or self.expiry < datetime.datetime.now():
                self.refresh_token(self)
                kwargs['headers']['Finicity-App-Token'] = self.token

            return func(*args, **kwargs)

        return call_api_function

    def refresh_token(self):
        current_date = datetime.datetime.now()
        expiry_date = current_date + datetime.timedelta(minutes=90)
        self.expiry = expiry_date

        request_body = {
            'partner_id': self.partner_id,
            'partner_secret': self.partner_secret
        }
        auth_response = AuthenticationApi(self.api_client).create_token(partner_credentials=request_body)
        self.token = auth_response.token
client = ApiClient()