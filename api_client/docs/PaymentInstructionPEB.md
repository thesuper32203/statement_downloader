# PaymentInstructionPEB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Payment instruction type | 
**account_number** | **str** | The account number from the institution | 
**tan_enabled** | **bool** | This field indicates whether the FI uses a tokenized account number for origination purposes. | [optional] 
**descriptors** | [**List[Descriptor]**](Descriptor.md) | List of descriptors | [optional] 

## Example

```python
from openapi_client.models.payment_instruction_peb import PaymentInstructionPEB

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstructionPEB from a JSON string
payment_instruction_peb_instance = PaymentInstructionPEB.from_json(json)
# print the JSON string representation of the object
print(PaymentInstructionPEB.to_json())

# convert the object into a dict
payment_instruction_peb_dict = payment_instruction_peb_instance.to_dict()
# create an instance of PaymentInstructionPEB from a dict
payment_instruction_peb_from_dict = PaymentInstructionPEB.from_dict(payment_instruction_peb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


