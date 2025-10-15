# GoldStandardErrorMessageErrorsErrorInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The applications that generated the error. | [optional] 
**reason_code** | **str** | A unique constant identifying the error case encountered during processing. | [optional] 
**description** | **str** | Short description of the ReasonCode field. | [optional] 
**recoverable** | **bool** | Indicates whether this error will always be returned for this request, or retrying could change the outcome. | [optional] 
**details** | **str** | Where appropriate, indicates detailed information about data received and calculated during request processing, to help the user with diagnosing errors. | [optional] 

## Example

```python
from openapi_client.models.gold_standard_error_message_errors_error_inner import GoldStandardErrorMessageErrorsErrorInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoldStandardErrorMessageErrorsErrorInner from a JSON string
gold_standard_error_message_errors_error_inner_instance = GoldStandardErrorMessageErrorsErrorInner.from_json(json)
# print the JSON string representation of the object
print(GoldStandardErrorMessageErrorsErrorInner.to_json())

# convert the object into a dict
gold_standard_error_message_errors_error_inner_dict = gold_standard_error_message_errors_error_inner_instance.to_dict()
# create an instance of GoldStandardErrorMessageErrorsErrorInner from a dict
gold_standard_error_message_errors_error_inner_from_dict = GoldStandardErrorMessageErrorsErrorInner.from_dict(gold_standard_error_message_errors_error_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


