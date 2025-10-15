# PaymentInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of payment instruction: 1. ACH: when payment instruction type is ACH (Automated Clearing House) 2. RTP: when payment instruction type is RTP (Real-Time Payments) | 
**account_number** | **str** | The account number from the institution | 
**tan_enabled** | **bool** | This field indicates whether the FI uses a tokenized account number for origination purposes. | [optional] [default to False]
**descriptors** | [**List[Descriptor]**](Descriptor.md) | List of descriptors | [optional] 
**transfer_in_enabled** | **bool** | Indicates whether transfer to this account is enabled or not. Applicable for \&quot;RTP\&quot; type only. | [optional] 
**transfer_out_enabled** | **bool** | Indicates whether transfer from this account is enabled or not. Applicable for \&quot;RTP\&quot; type only. | [optional] 

## Example

```python
from openapi_client.models.payment_instruction import PaymentInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstruction from a JSON string
payment_instruction_instance = PaymentInstruction.from_json(json)
# print the JSON string representation of the object
print(PaymentInstruction.to_json())

# convert the object into a dict
payment_instruction_dict = payment_instruction_instance.to_dict()
# create an instance of PaymentInstruction from a dict
payment_instruction_from_dict = PaymentInstruction.from_dict(payment_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


