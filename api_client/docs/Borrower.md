# Borrower


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**consumer_id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | 
**type** | **str** | \&quot;primary\&quot; or \&quot;jointBorrower\&quot; | 
**optional_consumer_info** | [**ConsumerInfo**](ConsumerInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.borrower import Borrower

# TODO update the JSON string below
json = "{}"
# create an instance of Borrower from a JSON string
borrower_instance = Borrower.from_json(json)
# print the JSON string representation of the object
print(Borrower.to_json())

# convert the object into a dict
borrower_dict = borrower_instance.to_dict()
# create an instance of Borrower from a dict
borrower_from_dict = Borrower.from_dict(borrower_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


