# DeviceID

This field contains device identification information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**u_device_id** | **str** | The generated unique device identifier. | [optional] 

## Example

```python
from openapi_client.models.device_id import DeviceID

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceID from a JSON string
device_id_instance = DeviceID.from_json(json)
# print the JSON string representation of the object
print(DeviceID.to_json())

# convert the object into a dict
device_id_dict = device_id_instance.to_dict()
# create an instance of DeviceID from a dict
device_id_from_dict = DeviceID.from_dict(device_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


