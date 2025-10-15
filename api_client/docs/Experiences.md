# Experiences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID that distinguishes each experience | [optional] 
**app_name** | **str** | Your registered application name in our system | [optional] 
**product_code** | **List[str]** | A unique code assigned to each open finance product used. | [optional] 

## Example

```python
from openapi_client.models.experiences import Experiences

# TODO update the JSON string below
json = "{}"
# create an instance of Experiences from a JSON string
experiences_instance = Experiences.from_json(json)
# print the JSON string representation of the object
print(Experiences.to_json())

# convert the object into a dict
experiences_dict = experiences_instance.to_dict()
# create an instance of Experiences from a dict
experiences_from_dict = Experiences.from_dict(experiences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


