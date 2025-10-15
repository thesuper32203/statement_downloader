# FinancialInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **int** | The financial institution identification at Mastercard. | [optional] 
**institution_name** | **str** | The financial institution name. | [optional] 
**status** | **bool** | Application registration status against the financial institution. | [optional] 
**created_date** | **str** | The application creation date and time at financial institutions are in ISO 8601 format. | [optional] 
**modified_date** | **str** | The application modification date and time at financial institutions in ISO 8601 format. | [optional] 

## Example

```python
from openapi_client.models.financial_institution import FinancialInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialInstitution from a JSON string
financial_institution_instance = FinancialInstitution.from_json(json)
# print the JSON string representation of the object
print(FinancialInstitution.to_json())

# convert the object into a dict
financial_institution_dict = financial_institution_instance.to_dict()
# create an instance of FinancialInstitution from a dict
financial_institution_from_dict = FinancialInstitution.from_dict(financial_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


