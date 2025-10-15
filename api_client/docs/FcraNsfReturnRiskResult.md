# FcraNsfReturnRiskResult

The successful result of the execution of the nsf return risk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispute_statement** | **str** | A message mentioning if/what type of dispute exists for the customer\&quot; | [optional] 
**available_balance** | **float** | The available balance provided, by the consumer’s financial institution, at the time of the request. | 
**daily_results** | [**List[NsfIndicator]**](NsfIndicator.md) | An Array of 3-10 days, providing the potentialSettlementDate, score, indicator, and reasons. | 

## Example

```python
from openapi_client.models.fcra_nsf_return_risk_result import FcraNsfReturnRiskResult

# TODO update the JSON string below
json = "{}"
# create an instance of FcraNsfReturnRiskResult from a JSON string
fcra_nsf_return_risk_result_instance = FcraNsfReturnRiskResult.from_json(json)
# print the JSON string representation of the object
print(FcraNsfReturnRiskResult.to_json())

# convert the object into a dict
fcra_nsf_return_risk_result_dict = fcra_nsf_return_risk_result_instance.to_dict()
# create an instance of FcraNsfReturnRiskResult from a dict
fcra_nsf_return_risk_result_from_dict = FcraNsfReturnRiskResult.from_dict(fcra_nsf_return_risk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


