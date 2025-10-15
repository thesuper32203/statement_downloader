# Deduction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The normalized category of the deductions in the format [type][number]. The number is the will be the iterating number of the type&#39;s occurrence starting at one. | [optional] 
**description** | **str** | The deduction line&#39;s deduction type description | [optional] 
**amount_current** | **float** | The amount for the deduction line deducted from employee&#39;s pay for the specified pay period | [optional] 
**amount_ytd** | **float** | The amount for the deduction line being deducted from the employee&#39;s pay for the current pay year | [optional] 
**type** | **str** | Categorization based on the deduction line&#39;s description | [optional] 

## Example

```python
from openapi_client.models.deduction import Deduction

# TODO update the JSON string below
json = "{}"
# create an instance of Deduction from a JSON string
deduction_instance = Deduction.from_json(json)
# print the JSON string representation of the object
print(Deduction.to_json())

# convert the object into a dict
deduction_dict = deduction_instance.to_dict()
# create an instance of Deduction from a dict
deduction_from_dict = Deduction.from_dict(deduction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


