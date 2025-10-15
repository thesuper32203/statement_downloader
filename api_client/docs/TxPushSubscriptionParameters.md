# TxPushSubscriptionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | A callback URL where to receive TxPush notifications | 

## Example

```python
from openapi_client.models.tx_push_subscription_parameters import TxPushSubscriptionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TxPushSubscriptionParameters from a JSON string
tx_push_subscription_parameters_instance = TxPushSubscriptionParameters.from_json(json)
# print the JSON string representation of the object
print(TxPushSubscriptionParameters.to_json())

# convert the object into a dict
tx_push_subscription_parameters_dict = tx_push_subscription_parameters_instance.to_dict()
# create an instance of TxPushSubscriptionParameters from a dict
tx_push_subscription_parameters_from_dict = TxPushSubscriptionParameters.from_dict(tx_push_subscription_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


