# GeoLocationItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The name of the Geolocation details. Possible values are POSTAL_CODE | [optional] 
**value** | **str** | The value of the Geolocation field | [optional] 

## Example

```python
from openapi_client.models.geo_location_items import GeoLocationItems

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLocationItems from a JSON string
geo_location_items_instance = GeoLocationItems.from_json(json)
# print the JSON string representation of the object
print(GeoLocationItems.to_json())

# convert the object into a dict
geo_location_items_dict = geo_location_items_instance.to_dict()
# create an instance of GeoLocationItems from a dict
geo_location_items_from_dict = GeoLocationItems.from_dict(geo_location_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


