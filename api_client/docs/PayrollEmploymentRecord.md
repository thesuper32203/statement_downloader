# PayrollEmploymentRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employer_name** | **str** | Name of the employer as stated by the employer in the payroll system | 
**legal_entity_id** | **str** | Employer identification number (EIN) | [optional] 
**original_hire_date** | **int** | The original hired date of an employee at the company | [optional] 
**latest_hire_date** | **int** | If an employee leaves the company and returns later, then the employer states the latest hire date at the company | [optional] 
**latest_pay_period_end_date** | **int** | The most recent pay period’s end date. | [optional] 
**latest_pay_date** | **int** | The most recent pay date from an employer | [optional] 
**days_since_last_pay** | **int** | The number of days since an employee was last paid | [optional] 
**number_pay_cadence_without_pay** | **int** | The number of pay cadences an employee has not been paid; determined by the pay frequency | [optional] 
**employment_end_date** | **int** | The date an employee ended their employment at the company | [optional] 
**employment_duration** | **str** | The length of time an employee has been employed with that employer in ISO 8601 format (e.g. P1Y6M0D) | [optional] 
**employer_address** | [**List[PayrollEmployerAddress]**](PayrollEmployerAddress.md) | Array of addresses | [optional] 
**employment_status_code** | **str** | &#39;Status codes: &#x60;A&#x60; - Active, &#x60;NLE&#x60; - No Longer Employed, &#x60;L&#x60; - Leave, &#x60;O&#x60; - Other&#39;, &#x60;I&#x60; - Inactive, &#x60;U&#x60; - Unknown&#39; | 
**employment_status_name** | **str** | &#39;Status name: &#x60;Active&#x60;, &#x60;No Longer Employed&#x60;, &#x60;Leave&#x60; or &#x60;Other&#x60;, &#x60;Inactive&#x60;, or &#x60;Unknown&#x60;&#39; | 
**derived_employment_status** | **bool** | Describes the employment status - it will be true if it is not directly stated by the employer, and false otherwise | [optional] 
**work_level_code** | **str** | The abbreviate code for the employment level names (workLevelName) that we receive from the employer | [optional] 
**work_level_name** | **str** | The employment level name is whatever we receive from the employer, such as full time, part time, temp, contractor, and more | [optional] 
**work_level_status** | **str** | The categorized work level status. Enumerations are:  * &#x60;Temporary&#x60;  * &#x60;Seasonal&#x60;  * &#x60;Retired&#x60;  * &#x60;Student&#x60;  * &#x60;Full Time&#x60;  * &#x60;Part Time&#x60;  * &#x60;Unspecified&#x60;  This is a new field, currently enabled only for testing reports. It will be added for all reports in August 2021.  | 
**position_title** | **str** | Employee job title | [optional] 
**position_duration** | **str** | The length of time an employee has been employed at their current or latest position for this employment in ISO 8601 format (eg P1Y6M0D) | [optional] 

## Example

```python
from openapi_client.models.payroll_employment_record import PayrollEmploymentRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollEmploymentRecord from a JSON string
payroll_employment_record_instance = PayrollEmploymentRecord.from_json(json)
# print the JSON string representation of the object
print(PayrollEmploymentRecord.to_json())

# convert the object into a dict
payroll_employment_record_dict = payroll_employment_record_instance.to_dict()
# create an instance of PayrollEmploymentRecord from a dict
payroll_employment_record_from_dict = PayrollEmploymentRecord.from_dict(payroll_employment_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


