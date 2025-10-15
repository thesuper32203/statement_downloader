# ObbAccountDetails

Details of the account and financial institution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number_display** | **str** | The account number from a financial institution in truncated format | [optional] 
**account_owner** | [**ObbAccountOwner**](ObbAccountOwner.md) |  | 
**aggregation_attempt_date** | **str** | A timestamp showing the last aggregation attempt. This will not be present until you have run your first aggregation for the account. | [optional] 
**aggregation_status_code** | **int** | The status of the most recent aggregation attempt. This will not be present until you have run your first aggregation for the account | [optional] 
**aggregation_success_date** | **str** | A timestamp showing the last successful aggregation of the account. This will not be present until you have run your first aggregation for the account. | [optional] 
**currency** | **str** | The currency of the account | [optional] 
**current_balance** | **float** | Current reported balance of the account | [optional] 
**id** | **int** | An account ID represented as a number | 
**institution** | [**ObbInstitution**](ObbInstitution.md) |  | 
**institution_login_id** | **int** | An institution login ID (from the account record), represented as a number | [optional] 
**name** | **str** | The account name from the institution | [optional] 
**real_account_number_last4** | **int** | The last 4 digits of the ACH account number | [optional] 
**status** | **str** | pending during account discovery, always active following successful account activation | [optional] 
**type** | **str** | Account type, e.g. checking/saving | [optional] 

## Example

```python
from openapi_client.models.obb_account_details import ObbAccountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ObbAccountDetails from a JSON string
obb_account_details_instance = ObbAccountDetails.from_json(json)
# print the JSON string representation of the object
print(ObbAccountDetails.to_json())

# convert the object into a dict
obb_account_details_dict = obb_account_details_instance.to_dict()
# create an instance of ObbAccountDetails from a dict
obb_account_details_from_dict = ObbAccountDetails.from_dict(obb_account_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


