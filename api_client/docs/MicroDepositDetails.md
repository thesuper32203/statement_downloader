# MicroDepositDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The following values may be returned in the field of a status:  * \&quot;Pending\&quot; : Micro entries not yet deposited to customer&#39;s account * \&quot;Completed\&quot;: Micro entries deposited to customer&#39;s account * \&quot;Verified\&quot;: Micro entries got successfully verified * \&quot;Rejected\&quot;: Micro entries got rejected due to some reason * \&quot;Returned\&quot;: Micro entries got returned back * \&quot;Failed\&quot;: Micro entries got failed due to some reason * \&quot;Expired\&quot;: Micro entries got expired as they remains unverified for certain defined days | [optional] 
**status_description** | **str** | Micro entries status description | [optional] 
**creation_date** | **str** | A date-time without time zone | [optional] 
**routing_number** | **str** | Routing number of receiving bank | [optional] 
**account_number_last4** | **str** | The last 4 digits of the ACH account number | [optional] 
**auto_verified_account** | **int** | This field stores an ID for the linked bank account to verify the microdeposits. It will have a value populated only when the microdeposits are auto verified successfully via account aggregation, otherwise this field will not be present. | [optional] 
**rail_type** | **str** | The Rail (ACH / RTP) used for initiating bank deposit(s). | [optional] 

## Example

```python
from openapi_client.models.micro_deposit_details import MicroDepositDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MicroDepositDetails from a JSON string
micro_deposit_details_instance = MicroDepositDetails.from_json(json)
# print the JSON string representation of the object
print(MicroDepositDetails.to_json())

# convert the object into a dict
micro_deposit_details_dict = micro_deposit_details_instance.to_dict()
# create an instance of MicroDepositDetails from a dict
micro_deposit_details_from_dict = MicroDepositDetails.from_dict(micro_deposit_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


