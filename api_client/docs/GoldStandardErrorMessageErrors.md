# GoldStandardErrorMessageErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**List[GoldStandardErrorMessageErrorsErrorInner]**](GoldStandardErrorMessageErrorsErrorInner.md) | Mastercard standard error message. | 

## Example

```python
from openapi_client.models.gold_standard_error_message_errors import GoldStandardErrorMessageErrors

# TODO update the JSON string below
json = "{}"
# create an instance of GoldStandardErrorMessageErrors from a JSON string
gold_standard_error_message_errors_instance = GoldStandardErrorMessageErrors.from_json(json)
# print the JSON string representation of the object
print(GoldStandardErrorMessageErrors.to_json())

# convert the object into a dict
gold_standard_error_message_errors_dict = gold_standard_error_message_errors_instance.to_dict()
# create an instance of GoldStandardErrorMessageErrors from a dict
gold_standard_error_message_errors_from_dict = GoldStandardErrorMessageErrors.from_dict(gold_standard_error_message_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


