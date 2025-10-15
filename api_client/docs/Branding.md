# Branding

All assets are SVGs so can be slightly resized without any issues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **str** | File path of the institution&#39;s logo. For white backgrounds designed at 375 x 72, has built in spacing around it to normalize brand sizing. | [optional] 
**alternate_logo** | **str** | File path of the institution&#39;s alternate logo. For colored backgrounds designed at 375 x 72 has built in spacing around it to normalize brand sizing. | [optional] 
**icon** | **str** | File path of the institution&#39;s icon. For search results designed at 40 x 40. | [optional] 
**primary_color** | **str** | Hex code for the institution&#39;s primary color | [optional] 
**tile** | **str** | File path of institution name logo. For popular banks designed at 160 x 72. | [optional] 

## Example

```python
from openapi_client.models.branding import Branding

# TODO update the JSON string below
json = "{}"
# create an instance of Branding from a JSON string
branding_instance = Branding.from_json(json)
# print the JSON string representation of the object
print(Branding.to_json())

# convert the object into a dict
branding_dict = branding_instance.to_dict()
# create an instance of Branding from a dict
branding_from_dict = Branding.from_dict(branding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


