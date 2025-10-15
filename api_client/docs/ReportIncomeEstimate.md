# ReportIncomeEstimate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_annual** | **float** | Sum of all values in &#x60;netMonthlyIncome&#x60; over the previous 12 months | 
**projected_net_annual** | **float** | Projected net income over the next 12 months, across all income streams, based on &#x60;netAnnualIncome&#x60; | 
**estimated_gross_annual** | **float** | Before-tax gross annual income (estimated from &#x60;netAnnual&#x60;) across all income stream in the past 12 months | 
**projected_gross_annual** | **float** | Projected gross income over the next 12 months, across all active income streams, based on &#x60;projectedNetAnnual&#x60; | 

## Example

```python
from openapi_client.models.report_income_estimate import ReportIncomeEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of ReportIncomeEstimate from a JSON string
report_income_estimate_instance = ReportIncomeEstimate.from_json(json)
# print the JSON string representation of the object
print(ReportIncomeEstimate.to_json())

# convert the object into a dict
report_income_estimate_dict = report_income_estimate_instance.to_dict()
# create an instance of ReportIncomeEstimate from a dict
report_income_estimate_from_dict = ReportIncomeEstimate.from_dict(report_income_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


