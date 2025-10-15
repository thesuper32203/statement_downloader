# openapi_client.ThirdPartyAccessApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_third_party_access_key**](ThirdPartyAccessApi.md#generate_third_party_access_key) | **POST** /aggregation/v1/partners/accessKey | Generate Third Party Access Key
[**revoke_third_party_access_key**](ThirdPartyAccessApi.md#revoke_third_party_access_key) | **DELETE** /aggregation/v1/partners/accessKey/{consentReceiptId} | Revoke Third Party Access
[**update_third_party_access_key**](ThirdPartyAccessApi.md#update_third_party_access_key) | **PUT** /aggregation/v1/partners/accessKey/{consentReceiptId} | Update Third Party Access


# **generate_third_party_access_key**
> ThirdPartyAccessKeyReceiptData generate_third_party_access_key(third_party_access_key_data)

Generate Third Party Access Key

Generate access key for third party partners.
A partner can provide access to third party partners with this access key.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.third_party_access_key_data import ThirdPartyAccessKeyData
from openapi_client.models.third_party_access_key_receipt_data import ThirdPartyAccessKeyReceiptData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ThirdPartyAccessApi(api_client)
    third_party_access_key_data = openapi_client.ThirdPartyAccessKeyData() # ThirdPartyAccessKeyData | 

    try:
        # Generate Third Party Access Key
        api_response = api_instance.generate_third_party_access_key(third_party_access_key_data)
        print("The response of ThirdPartyAccessApi->generate_third_party_access_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyAccessApi->generate_third_party_access_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_access_key_data** | [**ThirdPartyAccessKeyData**](ThirdPartyAccessKeyData.md)|  | 

### Return type

[**ThirdPartyAccessKeyReceiptData**](ThirdPartyAccessKeyReceiptData.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The third party access key was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_third_party_access_key**
> revoke_third_party_access_key(consent_receipt_id)

Revoke Third Party Access

Revoke access of third party partners

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ThirdPartyAccessApi(api_client)
    consent_receipt_id = 'cr_4pfI3r1X8aOHrDDwrwC01NHFxOXlT1' # str | Third party access key receipt ID

    try:
        # Revoke Third Party Access
        api_instance.revoke_third_party_access_key(consent_receipt_id)
    except Exception as e:
        print("Exception when calling ThirdPartyAccessApi->revoke_third_party_access_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_receipt_id** | **str**| Third party access key receipt ID | 

### Return type

void (empty response body)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The third party access key was successfully revoked |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_third_party_access_key**
> ThirdPartyAccessKeyReceiptData update_third_party_access_key(consent_receipt_id, third_party_access_key_data)

Update Third Party Access

Update access for third party partners

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.third_party_access_key_data import ThirdPartyAccessKeyData
from openapi_client.models.third_party_access_key_receipt_data import ThirdPartyAccessKeyReceiptData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ThirdPartyAccessApi(api_client)
    consent_receipt_id = 'cr_4pfI3r1X8aOHrDDwrwC01NHFxOXlT1' # str | Third party access key receipt ID
    third_party_access_key_data = openapi_client.ThirdPartyAccessKeyData() # ThirdPartyAccessKeyData | 

    try:
        # Update Third Party Access
        api_response = api_instance.update_third_party_access_key(consent_receipt_id, third_party_access_key_data)
        print("The response of ThirdPartyAccessApi->update_third_party_access_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyAccessApi->update_third_party_access_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_receipt_id** | **str**| Third party access key receipt ID | 
 **third_party_access_key_data** | [**ThirdPartyAccessKeyData**](ThirdPartyAccessKeyData.md)|  | 

### Return type

[**ThirdPartyAccessKeyReceiptData**](ThirdPartyAccessKeyReceiptData.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The third party access key was successfully updated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

