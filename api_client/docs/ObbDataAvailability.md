# ObbDataAvailability

Availability of historical data at the time the report was requested

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**historic_availability_begin_date** | **str** | Begin date for data availability | [optional] 
**historic_availability_end_date** | **str** | End date for data availability | [optional] 
**historic_available_days** | **int** | Days for which transaction details are available | 
**historic_data_availability** | **str** | Description of historic data availability | 

## Example

```python
from openapi_client.models.obb_data_availability import ObbDataAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ObbDataAvailability from a JSON string
obb_data_availability_instance = ObbDataAvailability.from_json(json)
# print the JSON string representation of the object
print(ObbDataAvailability.to_json())

# convert the object into a dict
obb_data_availability_dict = obb_data_availability_instance.to_dict()
# create an instance of ObbDataAvailability from a dict
obb_data_availability_from_dict = ObbDataAvailability.from_dict(obb_data_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


