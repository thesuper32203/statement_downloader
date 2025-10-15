# PhoneNumberFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The country code digit representing the phone number for specific country | [optional] 
**phone_no** | **str** | A phone number ([E.164](https://en.wikipedia.org/wiki/E.164) format) minLength: 7 | [optional] 

## Example

```python
from openapi_client.models.phone_number_format import PhoneNumberFormat

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberFormat from a JSON string
phone_number_format_instance = PhoneNumberFormat.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberFormat.to_json())

# convert the object into a dict
phone_number_format_dict = phone_number_format_instance.to_dict()
# create an instance of PhoneNumberFormat from a dict
phone_number_format_from_dict = PhoneNumberFormat.from_dict(phone_number_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


