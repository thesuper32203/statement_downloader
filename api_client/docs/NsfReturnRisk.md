# NsfReturnRisk

The result or error occurred during the execution of the nsf return risk prediction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**NsfReturnRiskResult**](NsfReturnRiskResult.md) |  | [optional] 
**error** | [**ErrorMessage**](ErrorMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.nsf_return_risk import NsfReturnRisk

# TODO update the JSON string below
json = "{}"
# create an instance of NsfReturnRisk from a JSON string
nsf_return_risk_instance = NsfReturnRisk.from_json(json)
# print the JSON string representation of the object
print(NsfReturnRisk.to_json())

# convert the object into a dict
nsf_return_risk_dict = nsf_return_risk_instance.to_dict()
# create an instance of NsfReturnRisk from a dict
nsf_return_risk_from_dict = NsfReturnRisk.from_dict(nsf_return_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


