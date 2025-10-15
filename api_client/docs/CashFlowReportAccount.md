# CashFlowReportAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Finicity account ID | [optional] 
**owner_name** | **str** | The name(s) of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then all owners will be listed separated by |. | [optional] 
**owner_address** | **str** | The mailing address of the account owner(s). If the owner information is not available, this field will not appear in the report. If the account has multiple owners then the address of the primary owner will be listed. | [optional] 
**owner_as_of_date** | **int** | The ownerAsOfDate field is populated if the account owner information was retrieved from a prior report and will show the created date of that report. Reports always try and aggregate fresh account owner information and only rarely aren&#39;t able to aggregate it. If account owner information is not able to be aggregated, but it was available from a prior report that had that same account, the information from that prior report will be used and this field will be populated. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/errors/error-list/#handling-epoch-dates-and-times). | [optional] 
**name** | **str** | The account name from the institution | [optional] 
**number** | **str** | The account number from the institution (obfuscated) | [optional] 
**type** | **str** | The list of supported account types. * &#x60;checking&#x60; * &#x60;savings&#x60; * &#x60;moneyMarket&#x60; * &#x60;cd&#x60; * &#x60;investment&#x60; * &#x60;investmentTaxDeferred&#x60; * &#x60;employeeStockPurchasePlan&#x60; * &#x60;ira&#x60; * &#x60;401k&#x60; * &#x60;roth&#x60; * &#x60;403b&#x60; * &#x60;529&#x60; * &#x60;rollover&#x60; * &#x60;ugma&#x60; * &#x60;utma&#x60; * &#x60;keogh&#x60; * &#x60;457&#x60; * &#x60;401a&#x60; * &#x60;unknown&#x60; * &#x60;mortgage&#x60; * &#x60;loan&#x60; * &#x60;creditCard&#x60; * &#x60;lineOfCredit&#x60; * &#x60;payroll&#x60; * &#x60;studentLoan&#x60; * &#x60;brokerageAccount&#x60; * &#x60;educationSavings&#x60; * &#x60;healthSavingsAccount&#x60; * &#x60;nonTaxableBrokerageAccount&#x60; * &#x60;pension&#x60; * &#x60;profitSharingPlan&#x60; * &#x60;roth401k&#x60; * &#x60;sepIRA&#x60; * &#x60;simpleIRA&#x60; * &#x60;thriftSavingsPlan&#x60; * &#x60;variableAnnuity&#x60; | [optional] 
**currency** | **str** | A currency code for account | [optional] 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable) | [optional] 
**current_balance** | **float** | The cleared balance of the account as-of &#x60;balanceDate&#x60; | [optional] 
**available_balance** | **float** | Available balance | [optional] 
**balance_date** | **int** | A timestamp showing when the &#x60;balance&#x60; was captured | [optional] 
**transactions** | [**List[ReportTransaction]**](ReportTransaction.md) | a list of transaction records | [optional] 
**cash_flow_balance** | [**CashFlowCashFlowBalance**](CashFlowCashFlowBalance.md) |  | [optional] 
**cash_flow_credit** | [**CashFlowCashFlowCredit**](CashFlowCashFlowCredit.md) |  | [optional] 
**cash_flow_debit** | [**CashFlowCashFlowDebit**](CashFlowCashFlowDebit.md) |  | [optional] 
**cash_flow_characteristic** | [**CashFlowCashFlowCharacteristic**](CashFlowCashFlowCharacteristic.md) |  | [optional] 

## Example

```python
from openapi_client.models.cash_flow_report_account import CashFlowReportAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowReportAccount from a JSON string
cash_flow_report_account_instance = CashFlowReportAccount.from_json(json)
# print the JSON string representation of the object
print(CashFlowReportAccount.to_json())

# convert the object into a dict
cash_flow_report_account_dict = cash_flow_report_account_instance.to_dict()
# create an instance of CashFlowReportAccount from a dict
cash_flow_report_account_from_dict = CashFlowReportAccount.from_dict(cash_flow_report_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


