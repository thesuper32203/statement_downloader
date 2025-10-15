# PEBAccountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An account ID | 
**real_account_number_last4** | **str** | The last 4 digits of the ACH account number | [optional] 
**institution_id** | **str** | The ID of a financial institution | 
**institution_name** | **str** | The name of the institution | 
**institution_login_id** | **int** | An institution login ID (from the account record), represented as a number | 
**account_details** | [**AccountSimpleDetails**](AccountSimpleDetails.md) |  | [optional] 
**balance_details** | [**AvailableBalancePEB**](AvailableBalancePEB.md) |  | [optional] 
**account_identity** | [**AccountOwnerHolders**](AccountOwnerHolders.md) |  | [optional] 
**payment_instruction** | [**PaymentInstructionPEB**](PaymentInstructionPEB.md) |  | [optional] 
**errors** | [**List[FieldError]**](FieldError.md) | Lists of errors while getting the data | [optional] 

## Example

```python
from openapi_client.models.peb_account_details import PEBAccountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PEBAccountDetails from a JSON string
peb_account_details_instance = PEBAccountDetails.from_json(json)
# print the JSON string representation of the object
print(PEBAccountDetails.to_json())

# convert the object into a dict
peb_account_details_dict = peb_account_details_instance.to_dict()
# create an instance of PEBAccountDetails from a dict
peb_account_details_from_dict = PEBAccountDetails.from_dict(peb_account_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


