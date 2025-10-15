# AccountSimpleDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An account ID | [optional] 
**account_number_display** | **str** | The account number from a financial institution in truncated format:    * Last four digits: \&quot;1234\&quot;    * Last four digits with suffix: \&quot;1234-9\&quot;    * Full value for string accounts: \&quot;john@gmail.com\&quot; example: &#39;1234-9&#39; | 
**name** | **str** | The account name from the institution | 
**type** | **str** | The list of supported account types. * \&quot;checking\&quot;: Standard checking * \&quot;savings\&quot;: Standard savings * \&quot;cd\&quot;: Certificates of deposit * \&quot;moneyMarket\&quot;: Money Market * \&quot;creditCard\&quot;: Standard credit cards * \&quot;lineOfCredit\&quot;: Home equity, line of credit * \&quot;investment\&quot;: Generic investment (no details) * \&quot;investmentTaxDeferred\&quot;: Generic tax-advantaged investment (no details) * \&quot;employeeStockPurchasePlan\&quot;: ESPP, Employee Stock Ownership Plans (ESOP), Stock Purchase Plans * \&quot;ira\&quot;: Individual Retirement Account (not Rollover or Roth) * \&quot;401k\&quot;: 401K Plan * \&quot;roth\&quot;: Roth IRA, Roth 401K * \&quot;403b\&quot;: 403B Plan * \&quot;529plan\&quot;: 529 Plan (True value is 529) * \&quot;rollover\&quot;: Rollover IRA * \&quot;ugma\&quot;: Uniform Gifts to Minors Act * \&quot;utma\&quot;: Uniform Transfers to Minors Act * \&quot;keogh\&quot;: Keogh Plan * \&quot;457plan\&quot;: 457 Plan (True value is 457) * \&quot;401a\&quot;: 401A Plan * \&quot;brokerageAccount\&quot;: Brokerage Account * \&quot;educationSavings\&quot;: Education Savings Account that is not a 529 * \&quot;healthSavingsAccount\&quot;: HSA (Health Savings Accounts) * \&quot;pension\&quot;: Pension * \&quot;profitSharingPlan\&quot;: Profit Sharing Plan * \&quot;roth401k\&quot;: Roth 401K * \&quot;sepIRA\&quot;: Simplified Employee Pension IRA * \&quot;simpleIRA\&quot;: Simple IRA * \&quot;thriftSavingsPlan\&quot;: Thrift Savings Plan * \&quot;variableAnnuity\&quot;: Variable Annuity * \&quot;cryptocurrency\&quot;: Cryptocurrency Wallet, Cryptocurrency Account * \&quot;mortgage\&quot;: Standard Mortgages * \&quot;loan\&quot;: Auto loans, equity loans, other loans * \&quot;studentLoan\&quot;: Student Loan * \&quot;studentLoanGroup\&quot;: Student Loan Group * \&quot;studentLoanAccount\&quot;: Student Loan Account | 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt (see [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/account-aggregation/#aggregation-status-codes)). Won&#39;t be present until you have run your first aggregation for the account. | [optional] 
**status** | **str** | \&quot;pending\&quot; during account discovery, always \&quot;active\&quot; following   successful account activation | 
**aggregation_success_date** | **datetime** | A date-time with time zone | [optional] 
**aggregation_attempt_date** | **datetime** | A date-time with time zone | [optional] 
**created_date** | **datetime** | A date-time with time zone | 
**currency** | **str** | A currency code | 
**display_position** | **int** | Display position of the account at the financial institution, \&quot;1\&quot;     being the top listed account | 
**parent_account** | **str** | An account ID | [optional] 

## Example

```python
from openapi_client.models.account_simple_details import AccountSimpleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSimpleDetails from a JSON string
account_simple_details_instance = AccountSimpleDetails.from_json(json)
# print the JSON string representation of the object
print(AccountSimpleDetails.to_json())

# convert the object into a dict
account_simple_details_dict = account_simple_details_instance.to_dict()
# create an instance of AccountSimpleDetails from a dict
account_simple_details_from_dict = AccountSimpleDetails.from_dict(account_simple_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


