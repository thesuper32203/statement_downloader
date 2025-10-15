# DeviceScores

Scores that were calculated by analyzing the provided device data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_risk_factor** | **int** | The calculated risk factor is represented numerically using a range from 1 (no/low risk) to 5 (high risk). Each numerical value and it&#39;s associated risk representation is shown below.   * &#x60;1&#x60; - Represents a no or low risk request.   * &#x60;2&#x60; - Represents a low risk request.   * &#x60;3&#x60; - Represents a medium risk request.   * &#x60;4&#x60; - Represents a high risk request.   * &#x60;5&#x60; - Represents a very high risk request.  The calculated risk factor is typically used to identify scenarios where a service provider may want to introduce consumer friction on the authorization process to validate the identity of the consumer. Example usage by a service provider may be to implement controls such as multifactor authentication for calculated risk factors of &#x60;3&#x60; or &#x60;4&#x60; and request blocking for risk factors of &#x60;5&#x60;. | [optional] 
**device_insight_factor** | **int** | The calculated device risk is represented numerically using a range from 1 (no/low risk) to 5 (high risk). Each numerical value and it&#39;s associated risk representation is shown below.   * &#x60;1&#x60; - Represents a no or low risk request.   * &#x60;2&#x60; - Represents a low risk request.   * &#x60;3&#x60; - Represents a medium risk request.   * &#x60;4&#x60; - Represents a high risk request.   * &#x60;5&#x60; - Represents a very high risk request.  The calculated risk score is typically used to identify scenarios where a service provider may want to introduce consumer friction on the authorization process to validate the identity of the consumer. Example usage by a service provider may be to implement controls such as multifactor authentication for calculated risk factors of &#x60;3&#x60; or &#x60;4&#x60; and request blocking for risk factors of &#x60;5&#x60;. | [optional] 
**device_trust_factor** | **int** | An integer between 1-5 (1 being no trust and 5 being high trust). The trust factor value reflects the trustworthiness of the attributes associated with this device. | [optional] 

## Example

```python
from openapi_client.models.device_scores import DeviceScores

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceScores from a JSON string
device_scores_instance = DeviceScores.from_json(json)
# print the JSON string representation of the object
print(DeviceScores.to_json())

# convert the object into a dict
device_scores_dict = device_scores_instance.to_dict()
# create an instance of DeviceScores from a dict
device_scores_from_dict = DeviceScores.from_dict(device_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


