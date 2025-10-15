# EntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the entity (entities). | [optional] 
**name** | **str** | Name of the entity (entities). | [optional] 
**group** | **str** | Group of the entity (entities). | [optional] 
**category** | **str** | Category of the entity (entities). | [optional] 
**website** | **str** | Website of the involved entity. | [optional] 
**logo_url** | **str** | Logo of the involved entity. | [optional] 
**entity_standardization_confidence_score** | **float** | A confidence score indicating the entity name returned is correctly standardized to a standard entity name. If no score is returned, the entity has not been standardized. | [optional] 

## Example

```python
from openapi_client.models.entities_inner import EntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EntitiesInner from a JSON string
entities_inner_instance = EntitiesInner.from_json(json)
# print the JSON string representation of the object
print(EntitiesInner.to_json())

# convert the object into a dict
entities_inner_dict = entities_inner_instance.to_dict()
# create an instance of EntitiesInner from a dict
entities_inner_from_dict = EntitiesInner.from_dict(entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


