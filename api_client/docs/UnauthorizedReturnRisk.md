# UnauthorizedReturnRisk

The result or error occurred during the execution of the unauthorized return risk prediction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**UnauthorizedReturnRiskResult**](UnauthorizedReturnRiskResult.md) |  | [optional] 
**error** | [**ErrorMessage**](ErrorMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.unauthorized_return_risk import UnauthorizedReturnRisk

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedReturnRisk from a JSON string
unauthorized_return_risk_instance = UnauthorizedReturnRisk.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedReturnRisk.to_json())

# convert the object into a dict
unauthorized_return_risk_dict = unauthorized_return_risk_instance.to_dict()
# create an instance of UnauthorizedReturnRisk from a dict
unauthorized_return_risk_from_dict = UnauthorizedReturnRisk.from_dict(unauthorized_return_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


