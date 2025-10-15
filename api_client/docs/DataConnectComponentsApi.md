# openapi_client.DataConnectComponentsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configurations_configuration_id**](DataConnectComponentsApi.md#delete_configurations_configuration_id) | **DELETE** /connect-components/configurations/{configuration_id} | Delete Configuration
[**get_configurations**](DataConnectComponentsApi.md#get_configurations) | **GET** /connect-components/configurations | Get All Configurations for Current Partner
[**get_configurations_configuration_id**](DataConnectComponentsApi.md#get_configurations_configuration_id) | **GET** /connect-components/configurations/{configuration_id} | Get Configuration Details
[**post_configurations**](DataConnectComponentsApi.md#post_configurations) | **POST** /connect-components/configurations | Create Components Configuration
[**post_institutions_institution_id_login_forms**](DataConnectComponentsApi.md#post_institutions_institution_id_login_forms) | **POST** /connect-components/institutions/{institution_id}/login-forms | Create Login Form
[**post_institutions_institution_id_oauth_urls**](DataConnectComponentsApi.md#post_institutions_institution_id_oauth_urls) | **POST** /connect-components/institutions/{institution_id}/oauth-urls | Create OAuth URL
[**post_reconnections**](DataConnectComponentsApi.md#post_reconnections) | **POST** /connect-components/customers/{customer_id}/institution-login-ids/{institution_login_id}/reconnections | Initiate Reconnection


# **delete_configurations_configuration_id**
> delete_configurations_configuration_id(configuration_id)

Delete Configuration

Removes the configuration from the database

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
    api_instance = openapi_client.DataConnectComponentsApi(api_client)
    configuration_id = '9082affa-d965-40be-a3ed-a320bb3467ff' # str | The unique identifier for a configuration object

    try:
        # Delete Configuration
        api_instance.delete_configurations_configuration_id(configuration_id)
    except Exception as e:
        print("Exception when calling DataConnectComponentsApi->delete_configurations_configuration_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_id** | **str**| The unique identifier for a configuration object | 

### Return type

void (empty response body)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty Response Body |  -  |
**401** | The request was rejected |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations**
> List[Configuration] get_configurations()

Get All Configurations for Current Partner

Get all previously saved Data Connect Component configurations.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.configuration import Configuration
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
    api_instance = openapi_client.DataConnectComponentsApi(api_client)

    try:
        # Get All Configurations for Current Partner
        api_response = api_instance.get_configurations()
        print("The response of DataConnectComponentsApi->get_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectComponentsApi->get_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Configuration]**](Configuration.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of available configurations |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations_configuration_id**
> Configuration get_configurations_configuration_id(configuration_id)

Get Configuration Details

Returns the configuration with the specified id if the configuration exists and belongs to the partner calling this endpoint

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.configuration import Configuration
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
    api_instance = openapi_client.DataConnectComponentsApi(api_client)
    configuration_id = '9082affa-d965-40be-a3ed-a320bb3467ff' # str | The unique identifier for a configuration object

    try:
        # Get Configuration Details
        api_response = api_instance.get_configurations_configuration_id(configuration_id)
        print("The response of DataConnectComponentsApi->get_configurations_configuration_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectComponentsApi->get_configurations_configuration_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_id** | **str**| The unique identifier for a configuration object | 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object used to modify the login behavior |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_configurations**
> Configuration post_configurations(post_configurations_request)

Create Components Configuration

Optional endpoint. This endpoint is use to generate a configuration  object, which an then be passed in during the login flow. If used, the ID provided will need to be passed in the Create Login  Form or Create OAuth URL.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.configuration import Configuration
from openapi_client.models.post_configurations_request import PostConfigurationsRequest
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
    api_instance = openapi_client.DataConnectComponentsApi(api_client)
    post_configurations_request = openapi_client.PostConfigurationsRequest() # PostConfigurationsRequest | 

    try:
        # Create Components Configuration
        api_response = api_instance.post_configurations(post_configurations_request)
        print("The response of DataConnectComponentsApi->post_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectComponentsApi->post_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_configurations_request** | [**PostConfigurationsRequest**](PostConfigurationsRequest.md)|  | 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An object used to modify the login behavior |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_institutions_institution_id_login_forms**
> PostInstitutionsInstitutionIdLoginForms201Response post_institutions_institution_id_login_forms(institution_id, post_institutions_institution_id_login_forms_request)

Create Login Form

Generate a new login form for a given institution, customer, and language.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.post_institutions_institution_id_login_forms201_response import PostInstitutionsInstitutionIdLoginForms201Response
from openapi_client.models.post_institutions_institution_id_login_forms_request import PostInstitutionsInstitutionIdLoginFormsRequest
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
    api_instance = openapi_client.DataConnectComponentsApi(api_client)
    institution_id = 170716 # int | The financial institution id at Mastercard.
    post_institutions_institution_id_login_forms_request = openapi_client.PostInstitutionsInstitutionIdLoginFormsRequest() # PostInstitutionsInstitutionIdLoginFormsRequest | An optional configuration object can be applied by including a valid `configurationId` in the request body. <br><br> The preferred language translation for the login form is request with the `language` property in the request body. Supported languages are:   * English: `en`   * English-United States:'en-us`   * Spanish: `es`   * Spanish-United States: `es-us`   * French: `fr`   * French-Canada: `fr-ca`

    try:
        # Create Login Form
        api_response = api_instance.post_institutions_institution_id_login_forms(institution_id, post_institutions_institution_id_login_forms_request)
        print("The response of DataConnectComponentsApi->post_institutions_institution_id_login_forms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectComponentsApi->post_institutions_institution_id_login_forms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **int**| The financial institution id at Mastercard. | 
 **post_institutions_institution_id_login_forms_request** | [**PostInstitutionsInstitutionIdLoginFormsRequest**](PostInstitutionsInstitutionIdLoginFormsRequest.md)| An optional configuration object can be applied by including a valid &#x60;configurationId&#x60; in the request body. &lt;br&gt;&lt;br&gt; The preferred language translation for the login form is request with the &#x60;language&#x60; property in the request body. Supported languages are:   * English: &#x60;en&#x60;   * English-United States:&#39;en-us&#x60;   * Spanish: &#x60;es&#x60;   * Spanish-United States: &#x60;es-us&#x60;   * French: &#x60;fr&#x60;   * French-Canada: &#x60;fr-ca&#x60; | 

### Return type

[**PostInstitutionsInstitutionIdLoginForms201Response**](PostInstitutionsInstitutionIdLoginForms201Response.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Generate a new login form entry |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_institutions_institution_id_oauth_urls**
> PostInstitutionsInstitutionIdOauthUrls201Response post_institutions_institution_id_oauth_urls(institution_id, post_institutions_institution_id_oauth_urls_request)

Create OAuth URL

Generates a new OAuth URL that can be used to connect an end-user into their direct-connection institution. The `redirectURI` will be called when the oauth session has completed. An optional configuration object can be applied by including a valid `configurationId` in the request body.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.post_institutions_institution_id_oauth_urls201_response import PostInstitutionsInstitutionIdOauthUrls201Response
from openapi_client.models.post_institutions_institution_id_oauth_urls_request import PostInstitutionsInstitutionIdOauthUrlsRequest
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
    api_instance = openapi_client.DataConnectComponentsApi(api_client)
    institution_id = 170716 # int | The financial institution id at Mastercard.
    post_institutions_institution_id_oauth_urls_request = openapi_client.PostInstitutionsInstitutionIdOauthUrlsRequest() # PostInstitutionsInstitutionIdOauthUrlsRequest | 

    try:
        # Create OAuth URL
        api_response = api_instance.post_institutions_institution_id_oauth_urls(institution_id, post_institutions_institution_id_oauth_urls_request)
        print("The response of DataConnectComponentsApi->post_institutions_institution_id_oauth_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectComponentsApi->post_institutions_institution_id_oauth_urls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **int**| The financial institution id at Mastercard. | 
 **post_institutions_institution_id_oauth_urls_request** | [**PostInstitutionsInstitutionIdOauthUrlsRequest**](PostInstitutionsInstitutionIdOauthUrlsRequest.md)|  | 

### Return type

[**PostInstitutionsInstitutionIdOauthUrls201Response**](PostInstitutionsInstitutionIdOauthUrls201Response.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The returned oauth url, as well as a reference back to this resource in case modifications are needed |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reconnections**
> PostInstitutionsInstitutionIdLoginForms201Response post_reconnections(customer_id, institution_login_id, body)

Initiate Reconnection

Use the Data Connect Fix API when the following conditions occur:
  * The connection to the user's financial institution is lost.
  * The user's credentials were updated (for any number of reasons).
  * The user's MFA challenge has expired.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.post_institutions_institution_id_login_forms201_response import PostInstitutionsInstitutionIdLoginForms201Response
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
    api_instance = openapi_client.DataConnectComponentsApi(api_client)
    customer_id = '1005061234' # str | Unique identifier of the customer
    institution_login_id = 7008461438 # int | Institution login id of the customer.
    body = None # object | 

    try:
        # Initiate Reconnection
        api_response = api_instance.post_reconnections(customer_id, institution_login_id, body)
        print("The response of DataConnectComponentsApi->post_reconnections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectComponentsApi->post_reconnections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer | 
 **institution_login_id** | **int**| Institution login id of the customer. | 
 **body** | **object**|  | 

### Return type

[**PostInstitutionsInstitutionIdLoginForms201Response**](PostInstitutionsInstitutionIdLoginForms201Response.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Generate a new login form entry |  -  |
**203** | MFA challenges required to log in |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

