# InputMerchantInformation

InputMerchantInformation is an object containing merchant details in the request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_descriptor** | **str** | This is a concatenated combination of DE43 merchant name, DE43 merchant city and DE43 merchant state. Spaces should be excluded when concatenating these fields. If merchant state is not provided by the acquirer, use merchant name and city only. If the acquirer provides a country code instead of a state, use a combination of merchant name, city, and country. | [optional] 
**name** | **str** | Name of the merchant. | [optional] 
**line1** | **str** | Line 1 of the transaction address. | [optional] 
**city** | **str** | City of the transaction. | [optional] 
**state** | **str** | State of the transaction. | [optional] 
**postal_code** | **str** | PostalCode of the transaction. | [optional] 
**country** | **str** | Country of the transaction. | [optional] 
**phone_number** | **str** | The phone number of the merchant | [optional] 
**website** | **str** | Website of the involved entity. | [optional] 
**merchant_category_code** | **str** | This code represents the category that a merchant location may be under and is supported by most payment providers. | [optional] 
**merchant_category_name** | **str** | This is the name of the Merchant Category that accompanies the MCC Code which identifies the category a merchant falls under. | [optional] 

## Example

```python
from openapi_client.models.input_merchant_information import InputMerchantInformation

# TODO update the JSON string below
json = "{}"
# create an instance of InputMerchantInformation from a JSON string
input_merchant_information_instance = InputMerchantInformation.from_json(json)
# print the JSON string representation of the object
print(InputMerchantInformation.to_json())

# convert the object into a dict
input_merchant_information_dict = input_merchant_information_instance.to_dict()
# create an instance of InputMerchantInformation from a dict
input_merchant_information_from_dict = InputMerchantInformation.from_dict(input_merchant_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


