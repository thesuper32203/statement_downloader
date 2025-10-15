# MicroDepositVerificationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The following values may be returned in the field of a status:  * \&quot;Pending\&quot; : Micro entries not yet deposited to customer&#39;s account * \&quot;Completed\&quot;: Micro entries deposited to customer&#39;s account * \&quot;Verified\&quot;: Micro entries got successfully verified * \&quot;Rejected\&quot;: Micro entries got rejected due to some reason * \&quot;Returned\&quot;: Micro entries got returned back * \&quot;Failed\&quot;: Micro entries got failed due to some reason * \&quot;Expired\&quot;: Micro entries got expired as they remains unverified for certain defined days | [optional] 
**status_description** | **str** | Micro entries status description | [optional] 

## Example

```python
from openapi_client.models.micro_deposit_verification_error import MicroDepositVerificationError

# TODO update the JSON string below
json = "{}"
# create an instance of MicroDepositVerificationError from a JSON string
micro_deposit_verification_error_instance = MicroDepositVerificationError.from_json(json)
# print the JSON string representation of the object
print(MicroDepositVerificationError.to_json())

# convert the object into a dict
micro_deposit_verification_error_dict = micro_deposit_verification_error_instance.to_dict()
# create an instance of MicroDepositVerificationError from a dict
micro_deposit_verification_error_from_dict = MicroDepositVerificationError.from_dict(micro_deposit_verification_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


