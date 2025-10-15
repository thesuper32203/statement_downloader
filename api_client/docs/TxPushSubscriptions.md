# TxPushSubscriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[SubscriptionRecord]**](SubscriptionRecord.md) |  | 

## Example

```python
from openapi_client.models.tx_push_subscriptions import TxPushSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of TxPushSubscriptions from a JSON string
tx_push_subscriptions_instance = TxPushSubscriptions.from_json(json)
# print the JSON string representation of the object
print(TxPushSubscriptions.to_json())

# convert the object into a dict
tx_push_subscriptions_dict = tx_push_subscriptions_instance.to_dict()
# create an instance of TxPushSubscriptions from a dict
tx_push_subscriptions_from_dict = TxPushSubscriptions.from_dict(tx_push_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


