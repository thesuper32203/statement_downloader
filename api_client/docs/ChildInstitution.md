# ChildInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rssd** | **int** | The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits. | 
**parent_rssd** | **int** | The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits. | 
**name** | **str** | The name of the institution | 
**institution_id** | **int** | The ID of a financial institution, represented as a number | 

## Example

```python
from openapi_client.models.child_institution import ChildInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of ChildInstitution from a JSON string
child_institution_instance = ChildInstitution.from_json(json)
# print the JSON string representation of the object
print(ChildInstitution.to_json())

# convert the object into a dict
child_institution_dict = child_institution_instance.to_dict()
# create an instance of ChildInstitution from a dict
child_institution_from_dict = ChildInstitution.from_dict(child_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


