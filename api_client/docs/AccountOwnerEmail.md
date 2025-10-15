# AccountOwnerEmail

Account owner email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_primary** | **bool** | The email is primary. | [optional] 
**email** | **str** | An email address | [optional] 
**email_type** | **str** | The account owner&#39;s email type.  * \&quot;Personal\&quot;  * \&quot;Business\&quot; | [optional] 

## Example

```python
from openapi_client.models.account_owner_email import AccountOwnerEmail

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerEmail from a JSON string
account_owner_email_instance = AccountOwnerEmail.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerEmail.to_json())

# convert the object into a dict
account_owner_email_dict = account_owner_email_instance.to_dict()
# create an instance of AccountOwnerEmail from a dict
account_owner_email_from_dict = AccountOwnerEmail.from_dict(account_owner_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


