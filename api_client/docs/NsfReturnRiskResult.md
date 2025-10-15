# NsfReturnRiskResult

The successful result of the execution of the nsf return risk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_balance** | **float** | The available balance provided, by the consumer’s financial institution, at the time of the request. | 
**daily_results** | [**List[NsfIndicator]**](NsfIndicator.md) | An Array of 3-10 days, providing the potentialSettlementDate, score, indicator, and reasons. | 

## Example

```python
from openapi_client.models.nsf_return_risk_result import NsfReturnRiskResult

# TODO update the JSON string below
json = "{}"
# create an instance of NsfReturnRiskResult from a JSON string
nsf_return_risk_result_instance = NsfReturnRiskResult.from_json(json)
# print the JSON string representation of the object
print(NsfReturnRiskResult.to_json())

# convert the object into a dict
nsf_return_risk_result_dict = nsf_return_risk_result_instance.to_dict()
# create an instance of NsfReturnRiskResult from a dict
nsf_return_risk_result_from_dict = NsfReturnRiskResult.from_dict(nsf_return_risk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


