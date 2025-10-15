# PayrollReportConstraintsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_data** | [**PayrollDataOut**](PayrollDataOut.md) |  | 
**report_custom_fields** | [**List[ReportCustomField]**](ReportCustomField.md) | The &#x60;reportCustomFields&#x60; parameter is used when experiences are associated with a credit decisioning report.  Designate up to 5 custom fields that you&#39;d like associated with the report when it&#39;s generated. Every custom field consists of three variables: &#x60;label&#x60;, &#x60;value&#x60;, and &#x60;shown&#x60;. The &#x60;shown&#x60; variable is \&quot;true\&quot; or \&quot;false\&quot;. * \&quot;true\&quot;: (default) display the custom field in the PDF report * \&quot;false\&quot;: don&#39;t display the custom field in the PDF report  For an experience that generates multiple reports, the &#x60;reportCustomFields&#x60; parameter gets passed to all reports.  All custom fields display in the Reseller Billing API. | [optional] 
**pay_statements_from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 

## Example

```python
from openapi_client.models.payroll_report_constraints_out import PayrollReportConstraintsOut

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollReportConstraintsOut from a JSON string
payroll_report_constraints_out_instance = PayrollReportConstraintsOut.from_json(json)
# print the JSON string representation of the object
print(PayrollReportConstraintsOut.to_json())

# convert the object into a dict
payroll_report_constraints_out_dict = payroll_report_constraints_out_instance.to_dict()
# create an instance of PayrollReportConstraintsOut from a dict
payroll_report_constraints_out_from_dict = PayrollReportConstraintsOut.from_dict(payroll_report_constraints_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


