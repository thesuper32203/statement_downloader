# BaseReportAckConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics_report_data** | [**AnalyticsReportData**](AnalyticsReportData.md) |  | [optional] 
**account_ids** | **List[str]** | An array of account IDs to be included in the report (all accounts will be included if not set) | [optional] 
**report_custom_fields** | [**List[ReportCustomField]**](ReportCustomField.md) | The &#x60;reportCustomFields&#x60; parameter is used when experiences are associated with a credit decisioning report.  Designate up to 5 custom fields that you&#39;d like associated with the report when it&#39;s generated. Every custom field consists of three variables: &#x60;label&#x60;, &#x60;value&#x60;, and &#x60;shown&#x60;. The &#x60;shown&#x60; variable is \&quot;true\&quot; or \&quot;false\&quot;. * \&quot;true\&quot;: (default) display the custom field in the PDF report * \&quot;false\&quot;: don&#39;t display the custom field in the PDF report  For an experience that generates multiple reports, the &#x60;reportCustomFields&#x60; parameter gets passed to all reports.  All custom fields display in the Reseller Billing API. | [optional] 
**from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**show_nsf** | **bool** | Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee | [optional] 
**income_stream_confidence_minimum** | **int** | Include income streams in the report, based on the income stream&#39;s confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher. | [optional] 
**voie_with_interview_data** | [**VOIEWithInterviewData**](VOIEWithInterviewData.md) |  | 
**voie_with_statement_data** | [**VOIEWithStatementData**](VOIEWithStatementData.md) |  | 
**statement_report_data** | [**StatementData**](StatementData.md) |  | 
**to_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**include_pending** | **bool** | If pending transactions must be included | [optional] [default to False]
**find_transaction** | [**List[FindTransactionConstraintsInner]**](FindTransactionConstraintsInner.md) | An array of parameters used to return transactions matching the given criteria. The presence of multiple parameters will be treated as an **AND**  function. | [optional] 
**income_from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).  By default, the income history is set to 24 months, however, a partner can change the transaction history by setting the &#x60;incomeFromDate&#x60; parameter. | [optional] 
**voai_pdf_deposit_view** | **bool** | Provide an alternate PDF view of deposit transactions group by income stream in PDF. | [optional] 
**payroll_data** | [**PayrollDataOut**](PayrollDataOut.md) |  | 
**pay_statements_from_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**report_id** | **str** | A report ID | [optional] 
**paystatement_report** | [**PayStatementData**](PayStatementData.md) |  | 

## Example

```python
from openapi_client.models.base_report_ack_constraints import BaseReportAckConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of BaseReportAckConstraints from a JSON string
base_report_ack_constraints_instance = BaseReportAckConstraints.from_json(json)
# print the JSON string representation of the object
print(BaseReportAckConstraints.to_json())

# convert the object into a dict
base_report_ack_constraints_dict = base_report_ack_constraints_instance.to_dict()
# create an instance of BaseReportAckConstraints from a dict
base_report_ack_constraints_from_dict = BaseReportAckConstraints.from_dict(base_report_ack_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


