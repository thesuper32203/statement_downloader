# UnauthorizedReturnRiskResult

The result object containing the unauthoried return risk score

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | A risk score from 0-100 that indicates the likelihood of an unauthorized return risk, where a higher score indicates a higher likelihood of settlement or lower likelihood of return. | 
**indicator** | **str** | &#x60;indicator&#x60; conveys the &#x60;score&#x60;, projecting 3 possible values: \&quot;Low Risk\&quot;, \&quot;Medium Risk\&quot;, or \&quot;High Risk\&quot; | 

## Example

```python
from openapi_client.models.unauthorized_return_risk_result import UnauthorizedReturnRiskResult

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedReturnRiskResult from a JSON string
unauthorized_return_risk_result_instance = UnauthorizedReturnRiskResult.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedReturnRiskResult.to_json())

# convert the object into a dict
unauthorized_return_risk_result_dict = unauthorized_return_risk_result_instance.to_dict()
# create an instance of UnauthorizedReturnRiskResult from a dict
unauthorized_return_risk_result_from_dict = UnauthorizedReturnRiskResult.from_dict(unauthorized_return_risk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


