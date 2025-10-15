# ReportSummaries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[ReportSummary]**](ReportSummary.md) | Data pertaining to each report | 

## Example

```python
from openapi_client.models.report_summaries import ReportSummaries

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSummaries from a JSON string
report_summaries_instance = ReportSummaries.from_json(json)
# print the JSON string representation of the object
print(ReportSummaries.to_json())

# convert the object into a dict
report_summaries_dict = report_summaries_instance.to_dict()
# create an instance of ReportSummaries from a dict
report_summaries_from_dict = ReportSummaries.from_dict(report_summaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


