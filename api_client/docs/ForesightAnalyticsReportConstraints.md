# ForesightAnalyticsReportConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics_report_data** | [**ForesightAnalyticsReportData**](ForesightAnalyticsReportData.md) |  | [optional] 
**account_ids** | **str** | A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set) | [optional] 
**from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 

## Example

```python
from openapi_client.models.foresight_analytics_report_constraints import ForesightAnalyticsReportConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of ForesightAnalyticsReportConstraints from a JSON string
foresight_analytics_report_constraints_instance = ForesightAnalyticsReportConstraints.from_json(json)
# print the JSON string representation of the object
print(ForesightAnalyticsReportConstraints.to_json())

# convert the object into a dict
foresight_analytics_report_constraints_dict = foresight_analytics_report_constraints_instance.to_dict()
# create an instance of ForesightAnalyticsReportConstraints from a dict
foresight_analytics_report_constraints_from_dict = ForesightAnalyticsReportConstraints.from_dict(foresight_analytics_report_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


