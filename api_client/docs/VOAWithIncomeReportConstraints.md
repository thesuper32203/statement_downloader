# VOAWithIncomeReportConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **str** | A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set) | [optional] 
**report_custom_fields** | [**List[ReportCustomField]**](ReportCustomField.md) | The &#x60;reportCustomFields&#x60; parameter is used when experiences are associated with a credit decisioning report.  Designate up to 5 custom fields that you&#39;d like associated with the report when it&#39;s generated. Every custom field consists of three variables: &#x60;label&#x60;, &#x60;value&#x60;, and &#x60;shown&#x60;. The &#x60;shown&#x60; variable is \&quot;true\&quot; or \&quot;false\&quot;. * \&quot;true\&quot;: (default) display the custom field in the PDF report * \&quot;false\&quot;: don&#39;t display the custom field in the PDF report  For an experience that generates multiple reports, the &#x60;reportCustomFields&#x60; parameter gets passed to all reports.  All custom fields display in the Reseller Billing API. | [optional] 
**show_nsf** | **bool** | Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee | [optional] 
**from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**income_from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).  By default, the income history is set to 24 months, however, a partner can change the transaction history by setting the &#x60;incomeFromDate&#x60; parameter. | [optional] 
**income_stream_confidence_minimum** | **int** | Include income streams in the report, based on the income stream&#39;s confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher. | [optional] 

## Example

```python
from openapi_client.models.voa_with_income_report_constraints import VOAWithIncomeReportConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of VOAWithIncomeReportConstraints from a JSON string
voa_with_income_report_constraints_instance = VOAWithIncomeReportConstraints.from_json(json)
# print the JSON string representation of the object
print(VOAWithIncomeReportConstraints.to_json())

# convert the object into a dict
voa_with_income_report_constraints_dict = voa_with_income_report_constraints_instance.to_dict()
# create an instance of VOAWithIncomeReportConstraints from a dict
voa_with_income_report_constraints_from_dict = VOAWithIncomeReportConstraints.from_dict(voa_with_income_report_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


