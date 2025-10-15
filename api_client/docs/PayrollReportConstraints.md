# PayrollReportConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_data** | [**PayrollData**](PayrollData.md) |  | 
**report_custom_fields** | [**List[ReportCustomField]**](ReportCustomField.md) | The &#x60;reportCustomFields&#x60; parameter is used when experiences are associated with a credit decisioning report.  Designate up to 5 custom fields that you&#39;d like associated with the report when it&#39;s generated. Every custom field consists of three variables: &#x60;label&#x60;, &#x60;value&#x60;, and &#x60;shown&#x60;. The &#x60;shown&#x60; variable is \&quot;true\&quot; or \&quot;false\&quot;. * \&quot;true\&quot;: (default) display the custom field in the PDF report * \&quot;false\&quot;: don&#39;t display the custom field in the PDF report  For an experience that generates multiple reports, the &#x60;reportCustomFields&#x60; parameter gets passed to all reports.  All custom fields display in the Reseller Billing API. | [optional] 
**pay_statements_from_date** | **int** | Limits the pay statement history in the VOIE - Payroll report income record. Pay statements are only included if the payDate of the statement is equal to or greater than the start date requested. Date should be in Unix epoch time (in seconds). See: Handling Epoch Dates and Times. | [optional] 
**market_segment** | **str** | Use case for requesting the consumer&#39;s data. Current supported enumerations are:  &lt;br&gt; * &#x60;Auto&#x60;  &lt;br&gt; * &#x60;Background&#x60;  &lt;br&gt; * &#x60;Credit Card&#x60; &lt;br&gt; * &#x60;Employment&#x60;  &lt;br&gt; * &#x60;Government&#x60;  &lt;br&gt; * &#x60;Identity&#x60;  &lt;br&gt; * &#x60;KYC&#x60; &lt;br&gt; * &#x60;Mortgage&#x60;  &lt;br&gt; * &#x60;Personal&#x60;  &lt;br&gt; * &#x60;Tenant&#x60;  &lt;br&gt; If your usecase doesn&#39;t match one of these please reach out to your technical point of contact. | [optional] 
**exclude_emp_info** | **bool** | Only used on an exception basis for clients that need to exclude EmpInfo data from the VOE-Payroll or VOIE-Payroll report. If true is passed EmpInfo payroll provider&#39;s data will not be searched or returned. | [optional] 
**purpose** | **str** | FCRA required 2-digit Permissible Purpose Code, specifying the reason for retrieving this report. | [optional] 

## Example

```python
from openapi_client.models.payroll_report_constraints import PayrollReportConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollReportConstraints from a JSON string
payroll_report_constraints_instance = PayrollReportConstraints.from_json(json)
# print the JSON string representation of the object
print(PayrollReportConstraints.to_json())

# convert the object into a dict
payroll_report_constraints_dict = payroll_report_constraints_instance.to_dict()
# create an instance of PayrollReportConstraints from a dict
payroll_report_constraints_from_dict = PayrollReportConstraints.from_dict(payroll_report_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


