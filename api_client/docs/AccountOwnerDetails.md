# AccountOwnerDetails

Owner of a customer account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationship** | **str** | The type of relationship to the account: * \&quot;AUTHORIZED_USER\&quot;  * \&quot;BUSINESS\&quot;  * \&quot;FOR_BENEFIT_OF_PRIMARY\&quot;  * \&quot;FOR_BENEFIT_OF_PRIMARY_JOINT_RESTRICTED\&quot;  * \&quot;FOR_BENEFIT_OF_SECONDARY\&quot;  * \&quot;FOR_BENEFIT_OF_SECONDARY_JOINT_RESTRICTED\&quot;  * \&quot;FOR_BENEFIT_OF_SOLE_OWNER_RESTRICTED\&quot;  * \&quot;POWER_OF_ATTORNEY\&quot;  * \&quot;PRIMARY_JOINT_TENANTS\&quot;  * \&quot;PRIMARY\&quot;  * \&quot;PRIMARY_BORROWER\&quot;  * \&quot;PRIMARY_JOINT\&quot;  * \&quot;SECONDARY\&quot;  * \&quot;SECONDARY_JOINT_TENANTS\&quot;  * \&quot;SECONDARY_BORROWER\&quot;  * \&quot;SECONDARY_JOINT\&quot;  * \&quot;SOLE_OWNER\&quot;  * \&quot;TRUSTEE\&quot;  * \&quot;UNIFORM_TRANSFER_TO_MINOR\&quot; | [optional] 
**owner_name** | **str** | The full name of the account owner. Multiple account owners are returned in one string per the source data from the institution. | 
**first_name** | **str** | The first name of the account holder | [optional] 
**middle_name** | **str** | The middle name of the account holder | [optional] 
**last_name** | **str** | The last name of the account holder | [optional] 
**suffix** | **str** | A generational or academic suffix | [optional] 
**name_classification** | **str** | The classification of the account holder: * \&quot;person / personal / home\&quot; * \&quot;business\&quot; * \&quot;other\&quot; | 
**name_classificationconfidencescore** | **float** | The confidence score 0 – 1.0 of the name classification. | [optional] 
**addresses** | [**List[AccountOwnerAddress]**](AccountOwnerAddress.md) | List of addresses | [optional] 
**emails** | [**List[AccountOwnerEmail]**](AccountOwnerEmail.md) | List of emails | [optional] 
**phones** | [**List[AccountOwnerPhone]**](AccountOwnerPhone.md) | List of phones | [optional] 
**documentations** | [**List[AccountOwnerDocumentation]**](AccountOwnerDocumentation.md) | List of account owner documentation | [optional] 
**identity_insights** | [**AccountOwnerIdentityInsights**](AccountOwnerIdentityInsights.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_owner_details import AccountOwnerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerDetails from a JSON string
account_owner_details_instance = AccountOwnerDetails.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerDetails.to_json())

# convert the object into a dict
account_owner_details_dict = account_owner_details_instance.to_dict()
# create an instance of AccountOwnerDetails from a dict
account_owner_details_from_dict = AccountOwnerDetails.from_dict(account_owner_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


