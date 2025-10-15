# AccountDetailsTxBased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_margin_balance** | **float** | Only available for investment accounts. Net interest earned after deducting interest paid out. | [optional] 
**available_cash_balance** | **float** | Only available for investment accounts. Amount available for cash withdrawal. | [optional] 
**vested_balance** | **float** | Only available for investment accounts. Vested amount in account. | [optional] 
**current_loan_balance** | **float** | Only available for investment accounts. Current loan balance. | [optional] 
**available_balance_amount** | **float** | The available balance for the account | [optional] 
**margin_balance** | **float** | Net interest earned after deducting interest paid out | [optional] 
**current_balance** | **float** | Current balance | [optional] 

## Example

```python
from openapi_client.models.account_details_tx_based import AccountDetailsTxBased

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDetailsTxBased from a JSON string
account_details_tx_based_instance = AccountDetailsTxBased.from_json(json)
# print the JSON string representation of the object
print(AccountDetailsTxBased.to_json())

# convert the object into a dict
account_details_tx_based_dict = account_details_tx_based_instance.to_dict()
# create an instance of AccountDetailsTxBased from a dict
account_details_tx_based_from_dict = AccountDetailsTxBased.from_dict(account_details_tx_based_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


