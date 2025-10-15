# VOAIReportIncomeStream

A report income stream record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Income stream ID | 
**name** | **str** | A human-readable name based on the &#x60;normalizedPayee&#x60; name of the transactions for this income stream | 
**status** | **str** | Possible values: \&quot;ACTIVE\&quot;, \&quot;INACTIVE\&quot; | 
**estimate_inclusion** | **str** | Possible values: \&quot;HIGH\&quot;, \&quot;MODERATE\&quot;, \&quot;LOW\&quot;, \&quot;NO\&quot; | 
**confidence** | **int** | Level of confidence that the deposit stream represents income (example: 85%) | 
**cadence** | [**CadenceDetails**](CadenceDetails.md) |  | 
**net_monthly** | [**List[NetMonthly]**](NetMonthly.md) | A list of net monthly records. One instance for each complete calendar month in the report. | [optional] 
**net_annual** | **float** | Sum of all values in &#x60;netMonthlyIncome&#x60; over the previous 12 months | [optional] 
**projected_net_annual** | **float** | Projected net income over the next 12 months, across all income streams, based on &#x60;netAnnualIncome&#x60; | [optional] 
**estimated_gross_annual** | **float** | Before-tax gross annual income (estimated from &#x60;netAnnual&#x60;) across all income stream in the past 12 months | [optional] 
**projected_gross_annual** | **float** | Projected gross income over the next 12 months, across all active income streams, based on &#x60;projectedNetAnnual&#x60; | [optional] 
**average_monthly_income_net** | **float** | Monthly average amount over the previous 24 months | [optional] 
**income_stream_months** | **int** | The number of months the income transactions are observed | [optional] 
**transactions** | [**List[ReportTransaction]**](ReportTransaction.md) | A list of transaction records | 

## Example

```python
from openapi_client.models.voai_report_income_stream import VOAIReportIncomeStream

# TODO update the JSON string below
json = "{}"
# create an instance of VOAIReportIncomeStream from a JSON string
voai_report_income_stream_instance = VOAIReportIncomeStream.from_json(json)
# print the JSON string representation of the object
print(VOAIReportIncomeStream.to_json())

# convert the object into a dict
voai_report_income_stream_dict = voai_report_income_stream_instance.to_dict()
# create an instance of VOAIReportIncomeStream from a dict
voai_report_income_stream_from_dict = VOAIReportIncomeStream.from_dict(voai_report_income_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


