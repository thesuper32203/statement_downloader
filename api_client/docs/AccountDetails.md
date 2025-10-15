# AccountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_margin_balance** | **float** | Only available for investment accounts. Net interest earned after deducting interest paid out. | [optional] 
**available_cash_balance** | **float** | Only available for investment accounts. Amount available for cash withdrawal. | [optional] 
**vested_balance** | **float** | Only available for investment accounts. Vested amount in account. | [optional] 
**current_loan_balance** | **float** | Only available for investment accounts. Current loan balance. | [optional] 
**available_balance_amount** | **float** | The available balance for the account | [optional] 

## Example

```python
from openapi_client.models.account_details import AccountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDetails from a JSON string
account_details_instance = AccountDetails.from_json(json)
# print the JSON string representation of the object
print(AccountDetails.to_json())

# convert the object into a dict
account_details_dict = account_details_instance.to_dict()
# create an instance of AccountDetails from a dict
account_details_from_dict = AccountDetails.from_dict(account_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


