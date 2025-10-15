# FcraNsfReturnRisk

The result or error occurred during the execution of the nsf return risk prediction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FcraNsfReturnRiskResult**](FcraNsfReturnRiskResult.md) |  | [optional] 
**error** | [**ErrorMessage**](ErrorMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.fcra_nsf_return_risk import FcraNsfReturnRisk

# TODO update the JSON string below
json = "{}"
# create an instance of FcraNsfReturnRisk from a JSON string
fcra_nsf_return_risk_instance = FcraNsfReturnRisk.from_json(json)
# print the JSON string representation of the object
print(FcraNsfReturnRisk.to_json())

# convert the object into a dict
fcra_nsf_return_risk_dict = fcra_nsf_return_risk_instance.to_dict()
# create an instance of FcraNsfReturnRisk from a dict
fcra_nsf_return_risk_from_dict = FcraNsfReturnRisk.from_dict(fcra_nsf_return_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


