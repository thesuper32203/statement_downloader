# PrequalificationReportConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **str** | A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set) | [optional] 
**report_custom_fields** | [**List[ReportCustomField]**](ReportCustomField.md) | The &#x60;reportCustomFields&#x60; parameter is used when experiences are associated with a credit decisioning report.  Designate up to 5 custom fields that you&#39;d like associated with the report when it&#39;s generated. Every custom field consists of three variables: &#x60;label&#x60;, &#x60;value&#x60;, and &#x60;shown&#x60;. The &#x60;shown&#x60; variable is \&quot;true\&quot; or \&quot;false\&quot;. * \&quot;true\&quot;: (default) display the custom field in the PDF report * \&quot;false\&quot;: don&#39;t display the custom field in the PDF report  For an experience that generates multiple reports, the &#x60;reportCustomFields&#x60; parameter gets passed to all reports.  All custom fields display in the Reseller Billing API. | [optional] 
**show_nsf** | **bool** | Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee | [optional] 
**from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 

## Example

```python
from openapi_client.models.prequalification_report_constraints import PrequalificationReportConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of PrequalificationReportConstraints from a JSON string
prequalification_report_constraints_instance = PrequalificationReportConstraints.from_json(json)
# print the JSON string representation of the object
print(PrequalificationReportConstraints.to_json())

# convert the object into a dict
prequalification_report_constraints_dict = prequalification_report_constraints_instance.to_dict()
# create an instance of PrequalificationReportConstraints from a dict
prequalification_report_constraints_from_dict = PrequalificationReportConstraints.from_dict(prequalification_report_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


