# BillingResellerReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BillingReport]**](BillingReport.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.billing_reseller_report import BillingResellerReport

# TODO update the JSON string below
json = "{}"
# create an instance of BillingResellerReport from a JSON string
billing_reseller_report_instance = BillingResellerReport.from_json(json)
# print the JSON string representation of the object
print(BillingResellerReport.to_json())

# convert the object into a dict
billing_reseller_report_dict = billing_reseller_report_instance.to_dict()
# create an instance of BillingResellerReport from a dict
billing_reseller_report_from_dict = BillingResellerReport.from_dict(billing_reseller_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


