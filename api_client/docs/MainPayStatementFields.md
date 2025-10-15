# MainPayStatementFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_date** | **int** | Pay date for the pay period | 
**start_date** | **int** | Start date for the pay period | [optional] 
**end_date** | **int** | End date for the pay period | [optional] 
**pay_period_hours** | **float** | Sum of all hours worked each week for the pay period | [optional] 
**pay_frequency** | **str** | The current pay frequency, or how often a regular pay check is distributed:  * &#x60;Daily&#x60;  * &#x60;Weekly&#x60;  * &#x60;Bi-Weekly&#x60;  * &#x60;Semi-Monthly&#x60;  * &#x60;Monthly&#x60;  * &#x60;Quarterly&#x60;  * &#x60;Semi-Annual&#x60;  * &#x60;Annual&#x60;  * &#x60;Every 2.6 wks&#x60;  * &#x60;Every 4 wks&#x60;  * &#x60;Every 5.2 wks&#x60;  * &#x60;Other&#x60;  | [optional] 
**pay_type** | **str** | Current pay type:  * &#x60;Salary&#x60;  * &#x60;Hourly&#x60;  * &#x60;Daily&#x60;  | [optional] 
**gross_pay_amount** | **float** | Gross pay amount for the pay period | 
**gross_pay_amount_ytd** | **float** | Year to date (YTD) gross pay amount at the time of payment | [optional] 
**net_pay_amount** | **float** | Net pay amount for a pay period | [optional] 
**net_pay_amount_ytd** | **float** | Year to date (YTD) net pay amount at the time of payment | [optional] 

## Example

```python
from openapi_client.models.main_pay_statement_fields import MainPayStatementFields

# TODO update the JSON string below
json = "{}"
# create an instance of MainPayStatementFields from a JSON string
main_pay_statement_fields_instance = MainPayStatementFields.from_json(json)
# print the JSON string representation of the object
print(MainPayStatementFields.to_json())

# convert the object into a dict
main_pay_statement_fields_dict = main_pay_statement_fields_instance.to_dict()
# create an instance of MainPayStatementFields from a dict
main_pay_statement_fields_from_dict = MainPayStatementFields.from_dict(main_pay_statement_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


