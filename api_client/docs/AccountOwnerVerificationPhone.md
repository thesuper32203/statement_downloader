# AccountOwnerVerificationPhone

Consumer phone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The account owner&#39;s phone type:  * \&quot;HOME\&quot;  * \&quot;BUSINESS\&quot;  * \&quot;CELL\&quot;  * \&quot;FAX\&quot; | [optional] 
**country** | **str** | Country calling code of the phone number as defined by ITU-T E.123 and E.164 international standards (max length 3)\&quot;. | [optional] 
**phone** | **str** | A phone number (max length 15). | [optional] 
**phone_scores** | [**PhoneScores**](PhoneScores.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_owner_verification_phone import AccountOwnerVerificationPhone

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerVerificationPhone from a JSON string
account_owner_verification_phone_instance = AccountOwnerVerificationPhone.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerVerificationPhone.to_json())

# convert the object into a dict
account_owner_verification_phone_dict = account_owner_verification_phone_instance.to_dict()
# create an instance of AccountOwnerVerificationPhone from a dict
account_owner_verification_phone_from_dict = AccountOwnerVerificationPhone.from_dict(account_owner_verification_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


