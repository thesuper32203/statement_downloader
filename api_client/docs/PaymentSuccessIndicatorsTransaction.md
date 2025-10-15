# PaymentSuccessIndicatorsTransaction

An object containing the requested transaction info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settle_by_date** | **date** | The expected date that the funds, from the consumer’s account, will be moved to the receiving account.  &#x60;settleByDate&#x60; in ISO 8601 date format (YYYY-MM-DD). &#x60;settleByDate&#x60; dictates the number of days the model responds with. The response can range from 3-10 days, including &#x60;day0&#x60;. Details explained below: 1. If &#x60;settleByDate&#x60; is 9 or more days out from today, the response includes 10 days of data, &#x60;day0&#x60; through &#x60;day9&#x60;. 2. If &#x60;settleByDate&#x60; is between 3 and 8 days out from today, the response includes 4-9 days of data, &#x60;day3-8&#x60;. 3. If &#x60;settleByDate&#x60; is between today and 2 days out from today, the response includes 3 days of data, &#x60;day0&#x60; through &#x60;day2&#x60;. | 
**amount** | **float** | The transaction amount | 

## Example

```python
from openapi_client.models.payment_success_indicators_transaction import PaymentSuccessIndicatorsTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSuccessIndicatorsTransaction from a JSON string
payment_success_indicators_transaction_instance = PaymentSuccessIndicatorsTransaction.from_json(json)
# print the JSON string representation of the object
print(PaymentSuccessIndicatorsTransaction.to_json())

# convert the object into a dict
payment_success_indicators_transaction_dict = payment_success_indicators_transaction_instance.to_dict()
# create an instance of PaymentSuccessIndicatorsTransaction from a dict
payment_success_indicators_transaction_from_dict = PaymentSuccessIndicatorsTransaction.from_dict(payment_success_indicators_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


