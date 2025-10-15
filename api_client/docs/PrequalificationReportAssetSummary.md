# PrequalificationReportAssetSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The asset type: \&quot;checking\&quot;, \&quot;savings\&quot;, \&quot;moneyMarket\&quot;, \&quot;cd\&quot;, \&quot;investment\&quot; | [optional] 
**available_balance** | **float** | The available balance for the account | [optional] 
**current_balance** | **float** | The current balance of the account | 
**two_month_average** | **float** | The two month average daily balance of the account | 
**six_month_average** | **float** | The six month average daily balance of the account | [optional] 
**beginning_balance** | **float** | The beginning balance of the account per the time period of the report | 

## Example

```python
from openapi_client.models.prequalification_report_asset_summary import PrequalificationReportAssetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PrequalificationReportAssetSummary from a JSON string
prequalification_report_asset_summary_instance = PrequalificationReportAssetSummary.from_json(json)
# print the JSON string representation of the object
print(PrequalificationReportAssetSummary.to_json())

# convert the object into a dict
prequalification_report_asset_summary_dict = prequalification_report_asset_summary_instance.to_dict()
# create an instance of PrequalificationReportAssetSummary from a dict
prequalification_report_asset_summary_from_dict = PrequalificationReportAssetSummary.from_dict(prequalification_report_asset_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


