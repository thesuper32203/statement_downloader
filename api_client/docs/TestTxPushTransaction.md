# TestTxPushTransaction

A fake transaction for TxPush testing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the transaction | 
**description** | **str** | The description of the transaction | 
**status** | **str** | \&quot;active\&quot; or \&quot;pending\&quot; (optional) | [optional] [default to 'active']
**posted_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**transaction_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 

## Example

```python
from openapi_client.models.test_tx_push_transaction import TestTxPushTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of TestTxPushTransaction from a JSON string
test_tx_push_transaction_instance = TestTxPushTransaction.from_json(json)
# print the JSON string representation of the object
print(TestTxPushTransaction.to_json())

# convert the object into a dict
test_tx_push_transaction_dict = test_tx_push_transaction_instance.to_dict()
# create an instance of TestTxPushTransaction from a dict
test_tx_push_transaction_from_dict = TestTxPushTransaction.from_dict(test_tx_push_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


