# ReportIncomeStreamSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_type** | **str** | Possible values: \&quot;HIGH\&quot;, \&quot;MODERATE\&quot;, \&quot;LOW\&quot;, \&quot;NO\&quot; | 
**net_monthly** | [**List[NetMonthly]**](NetMonthly.md) | A list of net monthly records. One instance for each complete calendar month in the report. | 
**income_estimate** | [**ReportIncomeEstimate**](ReportIncomeEstimate.md) |  | 

## Example

```python
from openapi_client.models.report_income_stream_summary import ReportIncomeStreamSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ReportIncomeStreamSummary from a JSON string
report_income_stream_summary_instance = ReportIncomeStreamSummary.from_json(json)
# print the JSON string representation of the object
print(ReportIncomeStreamSummary.to_json())

# convert the object into a dict
report_income_stream_summary_dict = report_income_stream_summary_instance.to_dict()
# create an instance of ReportIncomeStreamSummary from a dict
report_income_stream_summary_from_dict = ReportIncomeStreamSummary.from_dict(report_income_stream_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


