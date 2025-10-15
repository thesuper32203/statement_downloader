# AvailableEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the event that is available for subscription. | 
**description** | **str** | A brief description of the event. | 
**conditional_subscription** | [**AvailableEventConditionalSubscription**](AvailableEventConditionalSubscription.md) |  | [optional] 

## Example

```python
from openapi_client.models.available_event import AvailableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableEvent from a JSON string
available_event_instance = AvailableEvent.from_json(json)
# print the JSON string representation of the object
print(AvailableEvent.to_json())

# convert the object into a dict
available_event_dict = available_event_instance.to_dict()
# create an instance of AvailableEvent from a dict
available_event_from_dict = AvailableEvent.from_dict(available_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


