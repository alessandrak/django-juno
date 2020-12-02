# Django Juno


Django Juno é um app para facilitar a integração com a API da Juno no Django.


## Instalação


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

## Métodos

### Tokenizar cartão de crédito

#### `juno_provider.tokenize_credit_card(credit_card_hash)`
Recebe uma hash de cartão criada a partir da biblioteca de criptografia da Juno e retorna o ID do cartão.

**Parâmetros**:
* **credit_card_hash**: Hash do cartão.



### Consultar cobrança

#### `juno_provider.get_charge(charge_id)`
Recebe o ID de uma cobrança e retorna os dados dela se existir.

**Parâmetros**:
* **charge_id**: ID da cobrança.


### Criar cobrança

#### `juno_provider.create_charge(description, amount, name, document, **kwargs)`
Cria uma cobrança a partir dos dados recebidos.

**Parâmetros**:
* **description**: Descrição da cobrança.
* **amount**: Valor da cobrança.
* **name**: Nome do comprador.
* **document**: CPF ou CNPJ do comprador, sem ponto ou traço.
* **email** *(opcional)*: E-mail do comprador.
* **phone** *(opcional)*: Telefone do comprador.
* **birth_date** *(opcional)*: Data de nascimento do comprador.


### Pagar cobrança

#### `juno_provider.create_charge(charge_id, credit_card, credit_card_type, street, number, city, state, post_code, **kwargs)`
Paga uma cobrança existente.

**Parâmetros**:
* **charge_id**: ID da cobrança.
* **credit_card**: Hash ou ID do cartão de crédito do pagador.
* **credit_card_type**: Tipo do dado enviado no parâmetro *credit_card*. Pode ter os seguintes valores: *'HASH'* ou *'ID'*.
* **street**: Rua do pagador.
* **city**: Cidade do pagador.
* **state**: Estado do pagador.
* **post_code**: CEP do pagador.
* **email** *(opcional)*: E-mail do pagador.


### Listar webhooks

#### `juno_provider.list_webhooks()`
Lista webhooks.


### Consultar webhook

#### `juno_provider.list_webhooks(wbh_id)`
Recebe o ID de um webhook e retorna os dados dele se existir.

**Parâmetros**:
* **wbh_id**: ID do webhook.


### Excluir webhook

#### `juno_provider.delete_webhook(wbh_id)`
Recebe o ID de um webhook e o exclui.

**Parâmetros**:
* **wbh_id**: ID do webhook.



## Exemplos

```
>>> from juno import juno_provider
>>> juno_provider.list_webhooks()
b'{"_embedded":{"webhooks":[{"id":"wbh_XXXXXXXXXXX","url":"xxxx","secret":"xxxxx","status":"ACTIVE","eventTypes":[{"id":"evt_XXXXXXXXX","name":"PAYMENT_NOTIFICATION","label":"Uma notifica\xc3\xa7\xc3\xa3o de pagamento foi gerada","status":"ENABLED"},{"id":"evt_CFCEXXXXXXXX","name":"CHARGE_STATUS_CHANGED","label":"O status de uma cobran\xc3\xa7a foi alterado","status":"ENABLED"}],"_links":{"self":{"href":"https://sandbox.boletobancario.com/api-integration/notifications/webhooks/wbh_7CXXXXXXXXXX"}}}]},"_links":{"self":{"href":"https://sandbox.boletobancario.com/api-integration/notifications/webhooks"}}}'

```