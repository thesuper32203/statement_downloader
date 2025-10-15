# CashFlowCashFlowCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_characteristics** | [**List[CashFlowMonthlyCashFlowCharacteristics]**](CashFlowMonthlyCashFlowCharacteristics.md) | List of attributes for each month | 
**average_monthly_net** | **float** | Average (Total Credits - Total Debits) for the account | 
**average_monthly_net_less_transfers** | **float** | Average (Total Credits - Total Debits) without transfers for the account | 
**twelve_month_total_net** | **float** | Sum of all monthly (Total Credits - Total Debits) each month for the account | [optional] 
**twelve_month_total_net_less_transfers** | **float** | Sum of all monthly (Total Credits - Total Debits) without transfers for the account | [optional] 
**six_month_average_total_credits_less_total_debits** | **float** | 6 Month Average (Total Credits - Total Debits) | [optional] 
**six_month_average_total_credits_less_total_debits_less_transfers** | **float** | 6 Month Average (Total Credits - Total Debits) - (Without Transfers) | [optional] 
**two_month_average_total_credits_less_total_debits** | **float** | 2 Month Average (Total Credits - Total Debits) | [optional] 
**two_month_average_total_credits_less_total_debits_less_transfers** | **float** | 2 Month Average (Total Credits - Total Debits) - (Without Transfers) | [optional] 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_characteristic import CashFlowCashFlowCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowCharacteristic from a JSON string
cash_flow_cash_flow_characteristic_instance = CashFlowCashFlowCharacteristic.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowCharacteristic.to_json())

# convert the object into a dict
cash_flow_cash_flow_characteristic_dict = cash_flow_cash_flow_characteristic_instance.to_dict()
# create an instance of CashFlowCashFlowCharacteristic from a dict
cash_flow_cash_flow_characteristic_from_dict = CashFlowCashFlowCharacteristic.from_dict(cash_flow_cash_flow_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


