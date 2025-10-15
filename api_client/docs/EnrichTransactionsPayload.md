# EnrichTransactionsPayload

Request body that contains transactions to be enriched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionPayload]**](TransactionPayload.md) | A list of transactions requested to be enriched. | 

## Example

```python
from openapi_client.models.enrich_transactions_payload import EnrichTransactionsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichTransactionsPayload from a JSON string
enrich_transactions_payload_instance = EnrichTransactionsPayload.from_json(json)
# print the JSON string representation of the object
print(EnrichTransactionsPayload.to_json())

# convert the object into a dict
enrich_transactions_payload_dict = enrich_transactions_payload_instance.to_dict()
# create an instance of EnrichTransactionsPayload from a dict
enrich_transactions_payload_from_dict = EnrichTransactionsPayload.from_dict(enrich_transactions_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


