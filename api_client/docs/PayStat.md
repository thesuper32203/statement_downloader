# PayStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The normalized category of the earnings with a number appended. The number is the will be the iterating number of the type&#39;s occurrence starting at one. | [optional] 
**type** | **str** | The categorization based on the earning line&#39;s description. Possible values: * \&quot;bereavement\&quot;  * \&quot;bonus\&quot;  * \&quot;commission\&quot;  * \&quot;holiday\&quot;  * \&quot;jury duty\&quot;  * \&quot;overtime\&quot;  * \&quot;pension\&quot;  * \&quot;pto\&quot;  * \&quot;regular\&quot;  * \&quot;sick\&quot;  * \&quot;tips\&quot;  * \&quot;unknown\&quot;  * \&quot;vacation\&quot;  * \&quot;reimbursement\&quot;  * \&quot;stock\&quot;  * \&quot;benefit\&quot; | [optional] 
**description** | **str** | The earnings line&#39;s pay type description | [optional] 
**rate** | **float** | The rate for the earning line paid out to the employee for the specified pay period. | [optional] 
**units** | **float** | The units for the earning line paid out to the employee for the specified pay period. | [optional] 
**amount_current** | **float** | The amount for the earning line paid out to the employee for the specified pay period. | [optional] 
**amount_ytd** | **float** | The amount for the earning line being paid out to the employee for the current pay year. | [optional] 

## Example

```python
from openapi_client.models.pay_stat import PayStat

# TODO update the JSON string below
json = "{}"
# create an instance of PayStat from a JSON string
pay_stat_instance = PayStat.from_json(json)
# print the JSON string representation of the object
print(PayStat.to_json())

# convert the object into a dict
pay_stat_dict = pay_stat_instance.to_dict()
# create an instance of PayStat from a dict
pay_stat_from_dict = PayStat.from_dict(pay_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


