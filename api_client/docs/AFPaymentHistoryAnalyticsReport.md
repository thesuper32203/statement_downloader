# AFPaymentHistoryAnalyticsReport

A Cash Flow Analytics Report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A report ID | 
**customer_type** | **str** | The type of customer (\&quot;active\&quot; or \&quot;testing\&quot; or \&quot;\&quot; for all types) | 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**request_id** | **str** | Finicity indicator to track all activity associated with this report | 
**requester_name** | **str** | Name of a Finicity partner | 
**end_user** | [**ConsumerEndUser**](ConsumerEndUser.md) |  | [optional] 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). Note: If the report is retrieved on a day other than the day it was generated, on the header of the PDF version of the report there will be a \&quot;Retrieved Date\&quot; populated. | 
**title** | **str** | Title of the report | 
**consumer_id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | [optional] 
**consumer_ssn** | **str** | Last 4 digits of a SSN | [optional] 
**consumer_details** | [**ConsumerDetails**](ConsumerDetails.md) |  | [optional] 
**dispute_statement** | **str** | The dispute text | [optional] 
**type** | **str** | A report type. Possible values:  * &#x60;voi&#x60;  * &#x60;voa&#x60;  * &#x60;voaHistory&#x60;  * &#x60;history&#x60;  * &#x60;voieTxVerify&#x60;  * &#x60;voieWithReport&#x60;  * &#x60;voieWithInterview&#x60;  * &#x60;voieWithStatement&#x60;  * &#x60;paystatement&#x60;  * &#x60;preQualVoa&#x60;  * &#x60;assetSummary&#x60;  * &#x60;voie&#x60;  * &#x60;transactions&#x60;  * &#x60;statement&#x60;  * &#x60;voiePayroll&#x60;  * &#x60;voeTransactions&#x60;  * &#x60;farpbfnoncra&#x60;  * &#x60;voePayroll&#x60;  * &#x60;cfrp&#x60;  * &#x60;cfrb&#x60;  * &#x60;barpcra&#x60;  * &#x60;barpnoncra&#x60;  * &#x60;barbcra&#x60;  * &#x60;barbftc&#x60;  * &#x60;barbnoncra&#x60;  * &#x60;cfrpcra&#x60;  * &#x60;cfrpnoncra&#x60;  * &#x60;cracfrbcra&#x60;  * &#x60;cfrbnoncra&#x60;  * &#x60;cfrbftc&#x60;  * &#x60;phrbcra&#x60;  * &#x60;phrbnoncra&#x60;  * &#x60;phrbftc&#x60;  | 
**status** | **str** | A report generation status. Possible values:  * &#x60;inProgress&#x60;  * &#x60;success&#x60;  * &#x60;failure&#x60;  | 
**constraints** | [**BaseReportAckConstraints**](BaseReportAckConstraints.md) |  | 
**errors** | [**List[ErrorMessage]**](ErrorMessage.md) | In case errors occurred during the report generation | [optional] 
**business_details** | [**BusinessDetails**](BusinessDetails.md) |  | [optional] 
**report_pin** | **str** | A unique key returned per report for consumer Portal | [optional] 
**start_date** | **int** | The &#x60;postedDate&#x60; of the earliest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**end_date** | **int** | The &#x60;postedDate&#x60; of the latest transaction analyzed for the report. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**days** | **int** | Number of days covered by the report | [optional] 
**seasoned** | **bool** | \&quot;true\&quot; if the report covers more than 365 days | [optional] 
**institutions** | [**List[ReportInstitution]**](ReportInstitution.md) | A list of institution records, including information about the individual accounts used in this report | [optional] 
**customer_analytics** | [**CustomerAnalytics**](CustomerAnalytics.md) |  | [optional] 

## Example

```python
from openapi_client.models.af_payment_history_analytics_report import AFPaymentHistoryAnalyticsReport

# TODO update the JSON string below
json = "{}"
# create an instance of AFPaymentHistoryAnalyticsReport from a JSON string
af_payment_history_analytics_report_instance = AFPaymentHistoryAnalyticsReport.from_json(json)
# print the JSON string representation of the object
print(AFPaymentHistoryAnalyticsReport.to_json())

# convert the object into a dict
af_payment_history_analytics_report_dict = af_payment_history_analytics_report_instance.to_dict()
# create an instance of AFPaymentHistoryAnalyticsReport from a dict
af_payment_history_analytics_report_from_dict = AFPaymentHistoryAnalyticsReport.from_dict(af_payment_history_analytics_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


