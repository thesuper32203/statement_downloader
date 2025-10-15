# EventStatusUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status to set for the event. Can be &#x60;active&#x60;,&#x60;inactive&#x60; , &#x60;pending&#x60; or &#x60;removed&#x60;. | 

## Example

```python
from openapi_client.models.event_status_update import EventStatusUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EventStatusUpdate from a JSON string
event_status_update_instance = EventStatusUpdate.from_json(json)
# print the JSON string representation of the object
print(EventStatusUpdate.to_json())

# convert the object into a dict
event_status_update_dict = event_status_update_instance.to_dict()
# create an instance of EventStatusUpdate from a dict
event_status_update_from_dict = EventStatusUpdate.from_dict(event_status_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


