# AvailableBalancePEB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | An account ID represented as a number | [optional] 
**real_account_number_last4** | **str** | The last 4 digits of the ACH account number | 
**available_balance** | **float** | The available balance of the account | 
**available_balance_date** | **datetime** | A date-time with time zone | 
**cleared_balance** | **float** | The cleared balance of the account. Also referred as posted balance, current balance, ledger balance | 
**cleared_balance_date** | **datetime** | A date-time with time zone | 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt (see [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/account-aggregation/#aggregation-status-codes)). Won&#39;t be present until you have run your first aggregation for the account. | 
**currency** | **str** | A currency code | 

## Example

```python
from openapi_client.models.available_balance_peb import AvailableBalancePEB

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableBalancePEB from a JSON string
available_balance_peb_instance = AvailableBalancePEB.from_json(json)
# print the JSON string representation of the object
print(AvailableBalancePEB.to_json())

# convert the object into a dict
available_balance_peb_dict = available_balance_peb_instance.to_dict()
# create an instance of AvailableBalancePEB from a dict
available_balance_peb_from_dict = AvailableBalancePEB.from_dict(available_balance_peb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


