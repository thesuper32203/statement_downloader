# PayStatementReport

A Pay Statement report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A report ID | [optional] 
**customer_type** | **str** | The type of customer (\&quot;active\&quot; or \&quot;testing\&quot; or \&quot;\&quot; for all types) | [optional] 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | [optional] 
**request_id** | **str** | Finicity indicator to track all activity associated with this report | [optional] 
**requester_name** | **str** | Name of a Finicity partner | [optional] 
**end_user** | [**ConsumerEndUser**](ConsumerEndUser.md) |  | [optional] 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). Note: If the report is retrieved on a day other than the day it was generated, on the header of the PDF version of the report there will be a \&quot;Retrieved Date\&quot; populated. | [optional] 
**title** | **str** | Title of the report | [optional] 
**consumer_id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | [optional] 
**consumer_ssn** | **str** | Last 4 digits of a SSN | [optional] 
**consumer_details** | [**ConsumerDetails**](ConsumerDetails.md) |  | [optional] 
**dispute_statement** | **str** | The dispute text | [optional] 
**type** | **str** | A report type. Possible values:  * &#x60;voi&#x60;  * &#x60;voa&#x60;  * &#x60;voaHistory&#x60;  * &#x60;history&#x60;  * &#x60;voieTxVerify&#x60;  * &#x60;voieWithReport&#x60;  * &#x60;voieWithInterview&#x60;  * &#x60;voieWithStatement&#x60;  * &#x60;paystatement&#x60;  * &#x60;preQualVoa&#x60;  * &#x60;assetSummary&#x60;  * &#x60;voie&#x60;  * &#x60;transactions&#x60;  * &#x60;statement&#x60;  * &#x60;voiePayroll&#x60;  * &#x60;voeTransactions&#x60;  * &#x60;farpbfnoncra&#x60;  * &#x60;voePayroll&#x60;  * &#x60;cfrp&#x60;  * &#x60;cfrb&#x60;  * &#x60;barpcra&#x60;  * &#x60;barpnoncra&#x60;  * &#x60;barbcra&#x60;  * &#x60;barbftc&#x60;  * &#x60;barbnoncra&#x60;  * &#x60;cfrpcra&#x60;  * &#x60;cfrpnoncra&#x60;  * &#x60;cracfrbcra&#x60;  * &#x60;cfrbnoncra&#x60;  * &#x60;cfrbftc&#x60;  * &#x60;phrbcra&#x60;  * &#x60;phrbnoncra&#x60;  * &#x60;phrbftc&#x60;  | [optional] 
**status** | **str** | A report generation status. Possible values:  * &#x60;inProgress&#x60;  * &#x60;success&#x60;  * &#x60;failure&#x60;  | [optional] 
**constraints** | [**BaseReportAckConstraints**](BaseReportAckConstraints.md) |  | [optional] 
**errors** | [**List[ErrorMessage]**](ErrorMessage.md) | In case errors occurred during the report generation | [optional] 
**portfolio_id** | **str** | A unique identifier that will be consistent across all reports created for the same customer | [optional] 
**start_date** | **int** | The &#x60;postedDate&#x60; of the earliest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**end_date** | **int** | The &#x60;postedDate&#x60; of the latest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**report_style** | **str** | A report style. Possible values are directAPIPayroll, credentialedPayroll, paystatement, voieWithInterview, voieWithStatement, voieWithReport | [optional] 
**number_of_billable_assets** | **int** | Total number of billable pay statements included in the report | [optional] 
**asset_ids** | **List[str]** |  | [optional] 
**pay_statements** | [**List[VOIEPayStatement]**](VOIEPayStatement.md) | Extracted pay statement details | [optional] 

## Example

```python
from openapi_client.models.pay_statement_report import PayStatementReport

# TODO update the JSON string below
json = "{}"
# create an instance of PayStatementReport from a JSON string
pay_statement_report_instance = PayStatementReport.from_json(json)
# print the JSON string representation of the object
print(PayStatementReport.to_json())

# convert the object into a dict
pay_statement_report_dict = pay_statement_report_instance.to_dict()
# create an instance of PayStatementReport from a dict
pay_statement_report_from_dict = PayStatementReport.from_dict(pay_statement_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


