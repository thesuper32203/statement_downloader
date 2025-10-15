# VOETransactionsReportIncomeStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Income stream ID | 
**name** | **str** | A human-readable name based on the &#x60;normalizedPayee&#x60; name of the transactions for this income stream | 
**status** | **str** | Possible values: \&quot;ACTIVE\&quot;, \&quot;INACTIVE\&quot; | 
**estimate_inclusion** | **str** | Possible values: \&quot;HIGH\&quot;, \&quot;MODERATE\&quot;, \&quot;LOW\&quot;, \&quot;NO\&quot; | 
**confidence** | **int** | Level of confidence that the deposit stream represents income (example: 85%) | 
**cadence** | [**CadenceDetails**](CadenceDetails.md) |  | 
**days_since_last_transaction** | **int** | The number of days since the last credit transaction for the particular income stream | 
**next_expected_transaction_date** | **int** | The next expected credit transaction date for the particular income stream, based on the cadence | 
**income_stream_months** | **int** | The number of months the income transactions are observed | [optional] 
**transactions** | [**List[ReportTransaction]**](ReportTransaction.md) | A list of transaction records | 

## Example

```python
from openapi_client.models.voe_transactions_report_income_stream import VOETransactionsReportIncomeStream

# TODO update the JSON string below
json = "{}"
# create an instance of VOETransactionsReportIncomeStream from a JSON string
voe_transactions_report_income_stream_instance = VOETransactionsReportIncomeStream.from_json(json)
# print the JSON string representation of the object
print(VOETransactionsReportIncomeStream.to_json())

# convert the object into a dict
voe_transactions_report_income_stream_dict = voe_transactions_report_income_stream_instance.to_dict()
# create an instance of VOETransactionsReportIncomeStream from a dict
voe_transactions_report_income_stream_from_dict = VOETransactionsReportIncomeStream.from_dict(voe_transactions_report_income_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


