# VOIEReportConstraints

The request details from the report generation that were used to generate the report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voie_with_statement_data** | [**VOIEWithStatementData**](VOIEWithStatementData.md) |  | 
**report_custom_fields** | [**List[ReportCustomField]**](ReportCustomField.md) | The &#x60;reportCustomFields&#x60; parameter is used when experiences are associated with a credit decisioning report.  Designate up to 5 custom fields that you&#39;d like associated with the report when it&#39;s generated. Every custom field consists of three variables: &#x60;label&#x60;, &#x60;value&#x60;, and &#x60;shown&#x60;. The &#x60;shown&#x60; variable is \&quot;true\&quot; or \&quot;false\&quot;. * \&quot;true\&quot;: (default) display the custom field in the PDF report * \&quot;false\&quot;: don&#39;t display the custom field in the PDF report  For an experience that generates multiple reports, the &#x60;reportCustomFields&#x60; parameter gets passed to all reports.  All custom fields display in the Reseller Billing API. | [optional] 

## Example

```python
from openapi_client.models.voie_report_constraints import VOIEReportConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of VOIEReportConstraints from a JSON string
voie_report_constraints_instance = VOIEReportConstraints.from_json(json)
# print the JSON string representation of the object
print(VOIEReportConstraints.to_json())

# convert the object into a dict
voie_report_constraints_dict = voie_report_constraints_instance.to_dict()
# create an instance of VOIEReportConstraints from a dict
voie_report_constraints_from_dict = VOIEReportConstraints.from_dict(voie_report_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


