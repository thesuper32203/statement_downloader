# InsufficientFundsTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of the NSF transaction | 
**description** | **str** | Description of the transaction | [optional] 
**memo** | **str** | Transaction memo | [optional] 
**posted_date** | **str** | Posted date of the NSF transaction | 
**transaction_id** | **int** | Finicity transaction ID | 

## Example

```python
from openapi_client.models.insufficient_funds_transaction import InsufficientFundsTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientFundsTransaction from a JSON string
insufficient_funds_transaction_instance = InsufficientFundsTransaction.from_json(json)
# print the JSON string representation of the object
print(InsufficientFundsTransaction.to_json())

# convert the object into a dict
insufficient_funds_transaction_dict = insufficient_funds_transaction_instance.to_dict()
# create an instance of InsufficientFundsTransaction from a dict
insufficient_funds_transaction_from_dict = InsufficientFundsTransaction.from_dict(insufficient_funds_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


