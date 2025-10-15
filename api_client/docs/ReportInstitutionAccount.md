# ReportInstitutionAccount

An account record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the account | 
**owner_name** | **str** | The name(s) of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then all owners will be listed separated by |. | [optional] 
**owner_address** | **str** | The mailing address of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then the address of the primary owner will be listed. | [optional] 
**owner_as_of_date** | **int** | The ownerAsOfDate field is populated if the account owner information was retrieved from a prior report and will show the created date of that report. Reports always try and aggregate fresh account owner information and only rarely aren&#39;t able to aggregate it. If account owner information is not able to be aggregated, but it was available from a prior report that had that same account, the information from that prior report will be used and this field will be populated. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/errors/error-list/#handling-epoch-dates-and-times). | [optional] 
**name** | **str** | The account name from the institution | 
**number** | **str** | The account number from the institution (all digits except the last four are obfuscated) | 
**type** | **str** | The list of supported account types. * &#x60;checking&#x60; * &#x60;savings&#x60; * &#x60;moneyMarket&#x60; * &#x60;cd&#x60; * &#x60;investment&#x60; * &#x60;investmentTaxDeferred&#x60; * &#x60;employeeStockPurchasePlan&#x60; * &#x60;ira&#x60; * &#x60;401k&#x60; * &#x60;roth&#x60; * &#x60;403b&#x60; * &#x60;529&#x60; * &#x60;rollover&#x60; * &#x60;ugma&#x60; * &#x60;utma&#x60; * &#x60;keogh&#x60; * &#x60;457&#x60; * &#x60;401a&#x60; * &#x60;unknown&#x60; * &#x60;mortgage&#x60; * &#x60;loan&#x60; * &#x60;creditCard&#x60; * &#x60;lineOfCredit&#x60; * &#x60;payroll&#x60; * &#x60;studentLoan&#x60; * &#x60;brokerageAccount&#x60; * &#x60;educationSavings&#x60; * &#x60;healthSavingsAccount&#x60; * &#x60;nonTaxableBrokerageAccount&#x60; * &#x60;pension&#x60; * &#x60;profitSharingPlan&#x60; * &#x60;roth401k&#x60; * &#x60;sepIRA&#x60; * &#x60;simpleIRA&#x60; * &#x60;thriftSavingsPlan&#x60; * &#x60;variableAnnuity&#x60; | 
**currency** | **str** | A currency code for account | 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt | 
**current_balance** | **float** | Current balance of the account | [optional] 
**available_balance** | **float** | The available balance for the account | [optional] 
**balance_date** | **int** | A timestamp showing when the balance was captured by the FI | [optional] 
**transactions** | [**List[ReportTransactionNewTxBased]**](ReportTransactionNewTxBased.md) | a list of transaction records | 
**details** | [**AccountDetailsTxBased**](AccountDetailsTxBased.md) |  | [optional] 
**analytics** | [**AccountAnalytics**](AccountAnalytics.md) |  | [optional] 
**cash_flow_balance** | [**CashFlowCashFlowBalance**](CashFlowCashFlowBalance.md) |  | [optional] 
**cash_flow_credit** | [**CashFlowCashFlowCredit**](CashFlowCashFlowCredit.md) |  | [optional] 
**cash_flow_debit** | [**CashFlowCashFlowDebit**](CashFlowCashFlowDebit.md) |  | [optional] 
**cash_flow_characteristic** | [**CashFlowCashFlowCharacteristic**](CashFlowCashFlowCharacteristic.md) |  | [optional] 
**balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | [optional] 
**average_monthly_balance** | **float** | The average monthly balance of this account | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_account** | **int** | The count for the total number of insufficient funds transactions, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_over6_months_account** | **int** | The total number of  insufficient funds fees for the account over six months | [optional] 
**tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account** | **int** | The number of days since the most recent insufficient funds transaction, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**asset** | [**PrequalificationReportAssetSummary**](PrequalificationReportAssetSummary.md) |  | [optional] 
**oldest_transaction_date** | **int** | The oldest transaction date of this account. | [optional] 
**transactions_count** | **int** | A number detailing the total number of transactions for a given account. | [optional] 
**tot_number_insufficient_funds_fee_debit_tx_over2_months_account** | **int** | The count for the total number of insufficient funds transactions for the last two months, based on the &#x60;fromDate&#x60; of the report. | [optional] 
**position** | [**ReportAccountPosition**](ReportAccountPosition.md) |  | [optional] 
**income_streams** | [**List[VOIETXVerifyReportIncomeStream]**](VOIETXVerifyReportIncomeStream.md) | A list of income stream records | [optional] 
**beginning_balance** | **float** | Beginning balance of account per the time period in the report | [optional] 
**misc_deposits** | [**List[ReportTransaction]**](ReportTransaction.md) | A list of miscellaneous deposits | [optional] 

## Example

```python
from openapi_client.models.report_institution_account import ReportInstitutionAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ReportInstitutionAccount from a JSON string
report_institution_account_instance = ReportInstitutionAccount.from_json(json)
# print the JSON string representation of the object
print(ReportInstitutionAccount.to_json())

# convert the object into a dict
report_institution_account_dict = report_institution_account_instance.to_dict()
# create an instance of ReportInstitutionAccount from a dict
report_institution_account_from_dict = ReportInstitutionAccount.from_dict(report_institution_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


