# Deductions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Deduction types:  * &#x60;Federal tax&#x60;: Federal tax withholdings  * &#x60;State tax&#x60;: State tax withholdings  * &#x60;Local tax&#x60;: Local tax withholdings  * &#x60;Social security tax&#x60;: Social security tax withholdings  * &#x60;Medicare tax&#x60;: Medicare withholdings  * &#x60;SUI SDI VPDI tax&#x60;: SUI SDI VPDI tax  * Retirement deductions: Retirement withholdings  * &#x60;Benefit deductions&#x60;: Medical/Health benefits withholdings (i.e. medical, dental, vision, insurance)  * &#x60;Garnishment deductions&#x60;: Garnishment withholdings, (i.e. bankruptcy, student loan, state garnishments, tax levy garnishments, child support)  * &#x60;Other deductions&#x60;: Other withholdings, includes any other uncommon withholdings, pension plan, stock plans, etc.  | 
**amount** | **float** | Amount associated with deduction | 

## Example

```python
from openapi_client.models.deductions import Deductions

# TODO update the JSON string below
json = "{}"
# create an instance of Deductions from a JSON string
deductions_instance = Deductions.from_json(json)
# print the JSON string representation of the object
print(Deductions.to_json())

# convert the object into a dict
deductions_dict = deductions_instance.to_dict()
# create an instance of Deductions from a dict
deductions_from_dict = Deductions.from_dict(deductions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


