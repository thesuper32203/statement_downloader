# SubscriptionRecord

TxPush subscription details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of a TxPush subscription | 
**account_id** | **int** | An account ID represented as a number | 
**type** | **str** | A TxPush subscription type (\&quot;account\&quot; or \&quot;transaction\&quot;) | 
**callback_url** | **str** | A callback URL where to receive TxPush notifications | 
**signing_key** | **str** | Signing key for events | 

## Example

```python
from openapi_client.models.subscription_record import SubscriptionRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRecord from a JSON string
subscription_record_instance = SubscriptionRecord.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRecord.to_json())

# convert the object into a dict
subscription_record_dict = subscription_record_instance.to_dict()
# create an instance of SubscriptionRecord from a dict
subscription_record_from_dict = SubscriptionRecord.from_dict(subscription_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


