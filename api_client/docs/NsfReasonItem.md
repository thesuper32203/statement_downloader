# NsfReasonItem

A collection of 8 reason codes, with a score ranging from 0-100, that explains the drivers that caused the nsf score.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recent_balance** | **int** | Evaluates the available balance in an account. | 
**balance_history** | **int** | Evaluates balance trends in the account. | 
**nsf_history** | **int** | Evaluates the number of NSF occurrences in the account. | 
**recent_nsf_history** | **int** | Evaluates the recent NSF occurrences in the account. | 
**recurring_nsf** | **int** | Evaluates the frequency of NSF occurrences in the account. | 
**spend_history** | **int** | Evaluates the trends in spend activity in the account. | 
**deposit_history** | **int** | Evaluates the trends of the consumer&#39;s permissioned account deposit over a period of time. | 
**transaction_amount** | **int** | Evaluates the settlementAmount. | 

## Example

```python
from openapi_client.models.nsf_reason_item import NsfReasonItem

# TODO update the JSON string below
json = "{}"
# create an instance of NsfReasonItem from a JSON string
nsf_reason_item_instance = NsfReasonItem.from_json(json)
# print the JSON string representation of the object
print(NsfReasonItem.to_json())

# convert the object into a dict
nsf_reason_item_dict = nsf_reason_item_instance.to_dict()
# create an instance of NsfReasonItem from a dict
nsf_reason_item_from_dict = NsfReasonItem.from_dict(nsf_reason_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


