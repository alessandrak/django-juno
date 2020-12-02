import json
import requests

from django.conf import settings

class JunoProvider:

    def __init__(
            self,
            client_id=settings.JUNO_CLIENT_ID,
            client_key=settings.JUNO_CLIENT_KEY,
            resource_token=settings.JUNO_RESOURCE_TOKEN,
            server=settings.JUNO_SERVER,
            **kwargs
        ):
        self.client_id = client_id
        self.client_key = client_key
        self.resource_token = resource_token
        self.server = server
        self.auth_server = '%s/authorization-server' % server
        self.resource_server = '%s/api-integration' % server
        self.access_token = self.get_access_token()
        self.headers = {
            'Authorization': 'Bearer %s' % self.access_token,
            'X-Api-Version': '2',
            'X-Resource-Token': self.resource_token
        }
        super(JunoProvider, self).__init__(**kwargs)

    def get_access_token(self):
        url = '%s/oauth/token' % self.auth_server
        data = {'grant_type': 'client_credentials'}
        response = requests.post(url, data=data,  auth=(self.client_id, self.client_key))
        content = json.loads(response.content)
        return content.get('access_token')

    def tokenize_credit_card(self, credit_card_hash):
        url = '%s/credit-cards/tokenization' % self.resource_server
        data = {
            'creditCardHash': credit_card_hash
        }
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.content)
        raise Exception(response.text)

    def get_charge(self, charge_id):
        if charge_id:
            url = '%s/charges/%s/' % (self.resource_server, charge_id)
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return json.loads(response.content.decode())
        raise Exception(response.text)

    def create_charge(self, description, amount, name, document, **kwargs):
        url = '%s/charges' % self.resource_server
        data = {
            'charge': {
                'description': description,
                'amount': amount,
                'paymentTypes': ['CREDIT_CARD'],
            },
            'billing': {
                'name': name,
                'document': document,
                'email': kwargs.get('email'),
                'phone': kwargs.get('phone'),
                'birthDate': kwargs.get('birth_date'),
                'notify': False
            }
        }
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code == 200:
            return response.content
        raise Exception(response.text)

    def pay_charge(self, charge_id, credit_card, credit_card_type, street, number, city, state, postCode, **kwargs):
        url = '%s/payments/' % self.resource_server
        if credit_card_type == 'ID':
            credit_card_details = {'creditCardId': credit_card}
        else:
            credit_card_details = {'creditCardHash': credit_card}
        data = {
            'chargeId': charge_id,
            'billing': {
                'email': kwargs.get('email'),
                'address': {
                    'street': street,
                    'number': number,
                    'city': city,
                    'state': state,
                    'postCode': postCode,
                }
            },
            'creditCardDetails': {
                'creditCardId': credit_card_details
            }
        }
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code == 200:
            return response.content
        raise Exception(response.text)

    def list_webhooks(self):
        url = '%s/notifications/webhooks' % self.resource_server
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.content
        raise Exception(response.text)

    def get_webhook(self, wbh_id):
        url = '%s/notifications/webhooks/%s' % (self.resource_server, wbh_id)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.content
        raise Exception(response.text)

    def delete_webhook(self, wbh_id):
        url = '%s/notifications/webhooks/%s' % (self.resource_server, wbh_id)
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 200:
            return response.content
        raise Exception(response.text)

juno_provider = JunoProvider()
