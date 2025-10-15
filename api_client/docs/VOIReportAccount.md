# VOIReportAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the account | [optional] 
**number** | **str** | The account number from the institution (all digits except the last four are obfuscated) | [optional] 
**owner_name** | **str** | The name(s) of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then all owners will be listed separated by |. | [optional] 
**owner_address** | **str** | The mailing address of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then the address of the primary owner will be listed. | [optional] 
**owner_as_of_date** | **int** | The ownerAsOfDate field is populated if the account owner information was retrieved from a prior report and will show the created date of that report. Reports always try and aggregate fresh account owner information and only rarely aren&#39;t able to aggregate it. If account owner information is not able to be aggregated, but it was available from a prior report that had that same account, the information from that prior report will be used and this field will be populated. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/errors/error-list/#handling-epoch-dates-and-times). | [optional] 
**name** | **str** | The account name from the institution | [optional] 
**type** | **str** | The list of supported account types. * &#x60;checking&#x60; * &#x60;savings&#x60; * &#x60;moneyMarket&#x60; | [optional] 
**currency** | **str** | A currency code for account | [optional] 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt | [optional] 
**income_streams** | [**List[VOIReportIncomeStream]**](VOIReportIncomeStream.md) | A list of income stream records | [optional] 
**balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | [optional] 
**average_monthly_balance** | **float** | The average monthly balance of this account | [optional] 
**transactions** | [**List[ReportTransaction]**](ReportTransaction.md) | a list of transaction records | [optional] 
**available_balance** | **float** | The available balance for the account | [optional] 
**current_balance** | **float** | Current balance of the account | [optional] 
**beginning_balance** | **float** | Beginning balance of account per the time period in the report | [optional] 
**oldest_transaction_date** | **int** | The oldest transaction date of this account. | [optional] 
**misc_deposits** | [**List[ReportTransaction]**](ReportTransaction.md) | A list of miscellaneous deposits | [optional] 

## Example

```python
from openapi_client.models.voi_report_account import VOIReportAccount

# TODO update the JSON string below
json = "{}"
# create an instance of VOIReportAccount from a JSON string
voi_report_account_instance = VOIReportAccount.from_json(json)
# print the JSON string representation of the object
print(VOIReportAccount.to_json())

# convert the object into a dict
voi_report_account_dict = voi_report_account_instance.to_dict()
# create an instance of VOIReportAccount from a dict
voi_report_account_from_dict = VOIReportAccount.from_dict(voi_report_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


