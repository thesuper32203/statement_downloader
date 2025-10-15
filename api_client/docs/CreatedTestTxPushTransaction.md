# CreatedTestTxPushTransaction

Response for TxPush test transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A transaction ID | 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 

## Example

```python
from openapi_client.models.created_test_tx_push_transaction import CreatedTestTxPushTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedTestTxPushTransaction from a JSON string
created_test_tx_push_transaction_instance = CreatedTestTxPushTransaction.from_json(json)
# print the JSON string representation of the object
print(CreatedTestTxPushTransaction.to_json())

# convert the object into a dict
created_test_tx_push_transaction_dict = created_test_tx_push_transaction_instance.to_dict()
# create an instance of CreatedTestTxPushTransaction from a dict
created_test_tx_push_transaction_from_dict = CreatedTestTxPushTransaction.from_dict(created_test_tx_push_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


