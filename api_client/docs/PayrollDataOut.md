# PayrollDataOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_data_retrieval_id** | **str** | An ID to identify the data retrieved from the payroll providers for the report. | [optional] 
**payroll_aggregator_response_id** | **str** | An ID to identify the data retrieved from the payroll providers for the report. | [optional] 
**consent_method** | **str** | Client-collected consent payroll report tagging. | [optional] 
**employment_ids** | **List[str]** | An array of employmentIds | [optional] 
**payroll_account_ids** | **List[str]** | An array of payrollAccountIds | [optional] 
**report_id** | **str** | A report ID | [optional] 

## Example

```python
from openapi_client.models.payroll_data_out import PayrollDataOut

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollDataOut from a JSON string
payroll_data_out_instance = PayrollDataOut.from_json(json)
# print the JSON string representation of the object
print(PayrollDataOut.to_json())

# convert the object into a dict
payroll_data_out_dict = payroll_data_out_instance.to_dict()
# create an instance of PayrollDataOut from a dict
payroll_data_out_from_dict = PayrollDataOut.from_dict(payroll_data_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


