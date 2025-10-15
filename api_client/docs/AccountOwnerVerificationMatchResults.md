# AccountOwnerVerificationMatchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holders** | [**List[AccountOwnerVerificationMatchingDetails]**](AccountOwnerVerificationMatchingDetails.md) |  | [optional] 
**encrypted_value** | **str** | Encrypted response. | [optional] 

## Example

```python
from openapi_client.models.account_owner_verification_match_results import AccountOwnerVerificationMatchResults

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerVerificationMatchResults from a JSON string
account_owner_verification_match_results_instance = AccountOwnerVerificationMatchResults.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerVerificationMatchResults.to_json())

# convert the object into a dict
account_owner_verification_match_results_dict = account_owner_verification_match_results_instance.to_dict()
# create an instance of AccountOwnerVerificationMatchResults from a dict
account_owner_verification_match_results_from_dict = AccountOwnerVerificationMatchResults.from_dict(account_owner_verification_match_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


