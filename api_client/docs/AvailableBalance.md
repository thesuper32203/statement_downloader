# AvailableBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**real_account_number_last4** | **str** | The last 4 digits of the ACH account number | 
**available_balance** | **float** | The available balance of the account | 
**available_balance_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**cleared_balance** | **float** | The cleared balance of the account. Also referred as posted balance, current balance, ledger balance | 
**cleared_balance_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt (see [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/account-aggregation/#aggregation-status-codes)). Won&#39;t be present until you have run your first aggregation for the account. | 
**currency** | **str** | A currency code | 

## Example

```python
from openapi_client.models.available_balance import AvailableBalance

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableBalance from a JSON string
available_balance_instance = AvailableBalance.from_json(json)
# print the JSON string representation of the object
print(AvailableBalance.to_json())

# convert the object into a dict
available_balance_dict = available_balance_instance.to_dict()
# create an instance of AvailableBalance from a dict
available_balance_from_dict = AvailableBalance.from_dict(available_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


