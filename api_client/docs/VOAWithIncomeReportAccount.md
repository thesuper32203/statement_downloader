# VOAWithIncomeReportAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the account | [optional] 
**number** | **str** | The account number from the institution (all digits except the last four are obfuscated) | [optional] 
**owner_name** | **str** | The name(s) of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then all owners will be listed separated by |. | [optional] 
**owner_address** | **str** | The mailing address of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then the address of the primary owner will be listed. | [optional] 
**owner_as_of_date** | **int** | The ownerAsOfDate field is populated if the account owner information was retrieved from a prior report and will show the created date of that report. Reports always try and aggregate fresh account owner information and only rarely aren&#39;t able to aggregate it. If account owner information is not able to be aggregated, but it was available from a prior report that had that same account, the information from that prior report will be used and this field will be populated. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/errors/error-list/#handling-epoch-dates-and-times). | [optional] 
**name** | **str** | The account name from the institution | [optional] 
**type** | **str** | The list of supported account types. * &#x60;checking&#x60; * &#x60;savings&#x60; * &#x60;moneyMarket&#x60; * &#x60;cd&#x60; * &#x60;investment&#x60; * &#x60;investmentTaxDeferred&#x60; * &#x60;employeeStockPurchasePlan&#x60; * &#x60;ira&#x60; * &#x60;401k&#x60; * &#x60;roth&#x60; * &#x60;403b&#x60; * &#x60;529&#x60; * &#x60;rollover&#x60; * &#x60;ugma&#x60; * &#x60;utma&#x60; * &#x60;keogh&#x60; * &#x60;457&#x60; * &#x60;401a&#x60; * &#x60;brokerageAccount&#x60; * &#x60;educationSavings&#x60; * &#x60;healthSavingsAccount&#x60; * &#x60;nonTaxableBrokerageAccount&#x60; * &#x60;pension&#x60; * &#x60;profitSharingPlan&#x60; * &#x60;roth401k&#x60; * &#x60;sepIRA&#x60; * &#x60;simpleIRA&#x60; * &#x60;thriftSavingsPlan&#x60; * &#x60;variableAnnuity&#x60; | [optional] 
**currency** | **str** | A currency code for account | [optional] 
**available_balance** | **float** | The available balance for the account | [optional] 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt | [optional] 
**balance** | **float** | The cleared balance of the account as-of balanceDate | [optional] 
**balance_date** | **int** | A timestamp showing when the balance was captured by the FI | [optional] 
**average_monthly_balance** | **float** | The average monthly balance of this account | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_account** | **int** | The count for the total number of insufficient funds transactions, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_over2_months_account** | **int** | The count for the total number of insufficient funds transactions for the last two months, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account** | **int** | The number of days since the most recent insufficient funds transaction, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**oldest_transaction_date** | **int** | The oldest transaction date of this account. | [optional] 
**transactions** | [**List[ReportTransactionNewTxBased]**](ReportTransactionNewTxBased.md) | a list of transaction records | [optional] 
**details** | [**AccountDetailsTxBased**](AccountDetailsTxBased.md) |  | [optional] 
**position** | [**ReportAccountPosition**](ReportAccountPosition.md) |  | [optional] 
**asset** | [**PrequalificationReportAssetSummary**](PrequalificationReportAssetSummary.md) |  | [optional] 
**income_streams** | [**List[VOAIReportIncomeStream]**](VOAIReportIncomeStream.md) | A list of income stream records | [optional] 

## Example

```python
from openapi_client.models.voa_with_income_report_account import VOAWithIncomeReportAccount

# TODO update the JSON string below
json = "{}"
# create an instance of VOAWithIncomeReportAccount from a JSON string
voa_with_income_report_account_instance = VOAWithIncomeReportAccount.from_json(json)
# print the JSON string representation of the object
print(VOAWithIncomeReportAccount.to_json())

# convert the object into a dict
voa_with_income_report_account_dict = voa_with_income_report_account_instance.to_dict()
# create an instance of VOAWithIncomeReportAccount from a dict
voa_with_income_report_account_from_dict = VOAWithIncomeReportAccount.from_dict(voa_with_income_report_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


