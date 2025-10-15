# AvailableEventConditionalSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable** | **bool** | Indicates whether conditional subscription is applicable for this event. | 
**fields** | **str** | The fields that are applicable for conditional subscription, such as &#x60;accountId&#x60; or &#x60;customerId&#x60;. | [optional] 
**mandatory** | **bool** | Indicates whether the fields in the conditional subscription are mandatory. | 

## Example

```python
from openapi_client.models.available_event_conditional_subscription import AvailableEventConditionalSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableEventConditionalSubscription from a JSON string
available_event_conditional_subscription_instance = AvailableEventConditionalSubscription.from_json(json)
# print the JSON string representation of the object
print(AvailableEventConditionalSubscription.to_json())

# convert the object into a dict
available_event_conditional_subscription_dict = available_event_conditional_subscription_instance.to_dict()
# create an instance of AvailableEventConditionalSubscription from a dict
available_event_conditional_subscription_from_dict = AvailableEventConditionalSubscription.from_dict(available_event_conditional_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


