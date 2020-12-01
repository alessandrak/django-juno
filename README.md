Django Juno
=====

Django Juno é um app para facilitar a integração com a API da Juno no Django.

*Documentação detalhada na pasta "docs".*

Instalação
-----------

Instale usando pip
```
pip install django-juno
```
Adicione as seguintes variáveis no seu arquivo settings.py
```
JUNO_CLIENT_ID = 'client-id'
JUNO_CLIENT_KEY = 'client-key'
JUNO_RESOURCE_TOKEN = 'resource-token'
JUNO_SERVER = 'server'
```


Exemplos
-----------
```
>>> from juno import juno_provider
>>> juno_provider.list_webhooks()
b'{"_embedded":{"webhooks":[{"id":"wbh_XXXXXXXXXXX","url":"xxxx","secret":"xxxxx","status":"ACTIVE","eventTypes":[{"id":"evt_XXXXXXXXX","name":"PAYMENT_NOTIFICATION","label":"Uma notifica\xc3\xa7\xc3\xa3o de pagamento foi gerada","status":"ENABLED"},{"id":"evt_CFCEXXXXXXXX","name":"CHARGE_STATUS_CHANGED","label":"O status de uma cobran\xc3\xa7a foi alterado","status":"ENABLED"}],"_links":{"self":{"href":"https://sandbox.boletobancario.com/api-integration/notifications/webhooks/wbh_7CXXXXXXXXXX"}}}]},"_links":{"self":{"href":"https://sandbox.boletobancario.com/api-integration/notifications/webhooks"}}}'

```