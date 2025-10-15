# ServiceAgreement

An object that contains the language the terms and conditions were present in and the date the customer accepted the terms and conditions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language translation of the terms and conditions as presented to the customer. | 
**accepted_date** | **datetime** | The date the customer accepted the terms and conditions. Must be a valid ISO-8601 date time. | 

## Example

```python
from openapi_client.models.service_agreement import ServiceAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAgreement from a JSON string
service_agreement_instance = ServiceAgreement.from_json(json)
# print the JSON string representation of the object
print(ServiceAgreement.to_json())

# convert the object into a dict
service_agreement_dict = service_agreement_instance.to_dict()
# create an instance of ServiceAgreement from a dict
service_agreement_from_dict = ServiceAgreement.from_dict(service_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


