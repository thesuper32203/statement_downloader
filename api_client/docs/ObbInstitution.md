# ObbInstitution

Details of the financial institution this account is home to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_icon_url** | **str** | URL of the institution logo icon for reporting | [optional] 
**institution_id** | **int** | ID of the financial institution | 
**institution_name** | **str** | Name of the financial institution | [optional] 
**institution_primary_color** | **str** | Primary branding color of the institution, in hex color format | [optional] 

## Example

```python
from openapi_client.models.obb_institution import ObbInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of ObbInstitution from a JSON string
obb_institution_instance = ObbInstitution.from_json(json)
# print the JSON string representation of the object
print(ObbInstitution.to_json())

# convert the object into a dict
obb_institution_dict = obb_institution_instance.to_dict()
# create an instance of ObbInstitution from a dict
obb_institution_from_dict = ObbInstitution.from_dict(obb_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


