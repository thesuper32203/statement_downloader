# EnrichedTransactions

Request body that contains transactions to be enriched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[EnrichedTransaction]**](EnrichedTransaction.md) | List of input transactions to be enriched. | [optional] 

## Example

```python
from openapi_client.models.enriched_transactions import EnrichedTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedTransactions from a JSON string
enriched_transactions_instance = EnrichedTransactions.from_json(json)
# print the JSON string representation of the object
print(EnrichedTransactions.to_json())

# convert the object into a dict
enriched_transactions_dict = enriched_transactions_instance.to_dict()
# create an instance of EnrichedTransactions from a dict
enriched_transactions_from_dict = EnrichedTransactions.from_dict(enriched_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


