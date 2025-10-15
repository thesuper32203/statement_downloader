# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_event_id** | **str** | A unique UUID identifier for the webhook event. | 
**name** | **str** | The name of the event. | 
**url** | **str** | The webhook Url where the event notifications will be sent. The URL must be aligned with RFC 2396. | [optional] 
**status** | **str** | The status of the event (e.g. active, inactive, pending, removed). | 
**condition** | [**Condition**](Condition.md) |  | [optional] 

## Example

```python
from openapi_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


