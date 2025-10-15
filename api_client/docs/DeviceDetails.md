# DeviceDetails

More granular details of the device insights.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DeviceID**](DeviceID.md) |  | [optional] 
**device_info** | [**DeviceInfo**](DeviceInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_details import DeviceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDetails from a JSON string
device_details_instance = DeviceDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceDetails.to_json())

# convert the object into a dict
device_details_dict = device_details_instance.to_dict()
# create an instance of DeviceDetails from a dict
device_details_from_dict = DeviceDetails.from_dict(device_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


