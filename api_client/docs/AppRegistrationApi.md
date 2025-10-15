# openapi_client.AppRegistrationApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_registration_status**](AppRegistrationApi.md#get_app_registration_status) | **GET** /aggregation/v2/partners/applications | Get App Registration Status
[**get_applications**](AppRegistrationApi.md#get_applications) | **GET** /applications | Get App Details
[**get_registered_institutions**](AppRegistrationApi.md#get_registered_institutions) | **GET** /applications/{application_id}/institutions | Get App Registration Status by Institution
[**migrate_institution_login_accounts**](AppRegistrationApi.md#migrate_institution_login_accounts) | **PUT** /aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/migration | Migrate Institution Login Accounts
[**modify_app_registration**](AppRegistrationApi.md#modify_app_registration) | **PUT** /aggregation/v1/partners/applications/{preAppId} | Modify App Registration
[**register_app**](AppRegistrationApi.md#register_app) | **POST** /aggregation/v1/partners/applications | Register App
[**set_customer_app_id**](AppRegistrationApi.md#set_customer_app_id) | **PUT** /aggregation/v1/customers/{customerId}/applications/{applicationId} | Set Customer App ID


# **get_app_registration_status**
> AppStatuses get_app_registration_status(pre_app_id=pre_app_id, application_id=application_id, status=status, app_name=app_name, submitted_date=submitted_date, modified_date=modified_date, page=page, page_size=page_size)

Get App Registration Status

Get the status of your application registration(s).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.app_statuses import AppStatuses
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
    api_instance = openapi_client.AppRegistrationApi(api_client)
    pre_app_id = '2581' # str | The application registration tracking ID (optional)
    application_id = '00278431-b712-4f30-a044-b611f25e533d' # str | The application ID (optional)
    status = 'P' # str | Look up app registration requests by status (optional)
    app_name = 'Awesome Budget App' # str | Look up app registration requests by app name (optional)
    submitted_date = 1607450357 # int | Look up app registration requests by the date they were submitted (optional)
    modified_date = 1607450357 # int | Look up app registration requests by the date the request was updated. This can be used to determine when a request was updated to \"A\" or \"R\". (optional)
    page = 1 # int | Index of the page of results to return (optional) (default to 1)
    page_size = 1 # int | Maximum number of results per page (optional) (default to 1)

    try:
        # Get App Registration Status
        api_response = api_instance.get_app_registration_status(pre_app_id=pre_app_id, application_id=application_id, status=status, app_name=app_name, submitted_date=submitted_date, modified_date=modified_date, page=page, page_size=page_size)
        print("The response of AppRegistrationApi->get_app_registration_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRegistrationApi->get_app_registration_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_app_id** | **str**| The application registration tracking ID | [optional] 
 **application_id** | **str**| The application ID | [optional] 
 **status** | **str**| Look up app registration requests by status | [optional] 
 **app_name** | **str**| Look up app registration requests by app name | [optional] 
 **submitted_date** | **int**| Look up app registration requests by the date they were submitted | [optional] 
 **modified_date** | **int**| Look up app registration requests by the date the request was updated. This can be used to determine when a request was updated to \&quot;A\&quot; or \&quot;R\&quot;. | [optional] 
 **page** | **int**| Index of the page of results to return | [optional] [default to 1]
 **page_size** | **int**| Maximum number of results per page | [optional] [default to 1]

### Return type

[**AppStatuses**](AppStatuses.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app registration statuses were returned |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> ApplicationResponse get_applications(start=start, limit=limit, pre_app_id=pre_app_id, application_id=application_id, name=name, status=status)

Get App Details

This endpoint returns the status of the submitted application and provides additional details.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.application_response import ApplicationResponse
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
    api_instance = openapi_client.AppRegistrationApi(api_client)
    start = 1 # int | Index of the page of results to return (optional) (default to 1)
    limit = 50 # int | Maximum number of results per page (optional) (default to 50)
    pre_app_id = 13 # int | The identifier is provided by Mastercard at the first stage of application registration. (optional)
    application_id = '00278431-b712-4f30-a044-b611f25e533d' # str | The identifier is generated after the pre-app is approved. Pre-app is the first stage of application registration. Partner first submits an application registration request, then a Pre-app Id is generated for it, and if all the details are correct, the sales team will approve it, and then an application will be registered with the Application Id and associated with the Pre-app. This Application Id is utilized throughout the lifespan of an application. (optional)
    name = 'Mvelopes' # str | The application name provided by the partner. (optional)
    status = 'P' # str | The application registration status with Mastercard. ('A'=Approved, 'P'=Pending, 'D'=Deleted, 'R'=Rejected, 'S'=Skipped) (optional)

    try:
        # Get App Details
        api_response = api_instance.get_applications(start=start, limit=limit, pre_app_id=pre_app_id, application_id=application_id, name=name, status=status)
        print("The response of AppRegistrationApi->get_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRegistrationApi->get_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Index of the page of results to return | [optional] [default to 1]
 **limit** | **int**| Maximum number of results per page | [optional] [default to 50]
 **pre_app_id** | **int**| The identifier is provided by Mastercard at the first stage of application registration. | [optional] 
 **application_id** | **str**| The identifier is generated after the pre-app is approved. Pre-app is the first stage of application registration. Partner first submits an application registration request, then a Pre-app Id is generated for it, and if all the details are correct, the sales team will approve it, and then an application will be registered with the Application Id and associated with the Pre-app. This Application Id is utilized throughout the lifespan of an application. | [optional] 
 **name** | **str**| The application name provided by the partner. | [optional] 
 **status** | **str**| The application registration status with Mastercard. (&#39;A&#39;&#x3D;Approved, &#39;P&#39;&#x3D;Pending, &#39;D&#39;&#x3D;Deleted, &#39;R&#39;&#x3D;Rejected, &#39;S&#39;&#x3D;Skipped) | [optional] 

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response containing one or more application details. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_institutions**
> InstitutionResponse get_registered_institutions(application_id, start=start, limit=limit, institution_id=institution_id)

Get App Registration Status by Institution

Query the status of your application registration. If you specify the ID of a financial instituion in your query then the status for that institution is returned. If you do not specify an instituion ID then the status for all financial instituions is returned.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.institution_response import InstitutionResponse
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
    api_instance = openapi_client.AppRegistrationApi(api_client)
    application_id = '234dsfdsf-535fdgdtrtr-546464564' # str | The identifier is generated after the pre-app is approved. Pre-app is the first stage of application registration. Partner first submits an application registration request, then a Pre-app Id is generated for it, and if all the details are correct, the sales team will approve it, and then an application will be registered with the Application Id and associated with the Pre-app. This Application Id is utilized throughout the lifespan of an application.
    start = 1 # int | Index of the page of results to return (optional) (default to 1)
    limit = 25 # int | Maximum number of results per page (optional) (default to 25)
    institution_id = 170716 # int | The financial institution id at Mastercard. (optional)

    try:
        # Get App Registration Status by Institution
        api_response = api_instance.get_registered_institutions(application_id, start=start, limit=limit, institution_id=institution_id)
        print("The response of AppRegistrationApi->get_registered_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRegistrationApi->get_registered_institutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The identifier is generated after the pre-app is approved. Pre-app is the first stage of application registration. Partner first submits an application registration request, then a Pre-app Id is generated for it, and if all the details are correct, the sales team will approve it, and then an application will be registered with the Application Id and associated with the Pre-app. This Application Id is utilized throughout the lifespan of an application. | 
 **start** | **int**| Index of the page of results to return | [optional] [default to 1]
 **limit** | **int**| Maximum number of results per page | [optional] [default to 25]
 **institution_id** | **int**| The financial institution id at Mastercard. | [optional] 

### Return type

[**InstitutionResponse**](InstitutionResponse.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested application registration status against financial institutions. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_institution_login_accounts**
> CustomerAccounts migrate_institution_login_accounts(customer_id, institution_login_id)

Migrate Institution Login Accounts

The `institutionLoginId` parameter uses Finicity's internal FI mapping to move accounts from the current FI legacy connection to the new OAuth FI connection.

This API returns a list of accounts for the given institution login ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.customer_accounts import CustomerAccounts
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
    api_instance = openapi_client.AppRegistrationApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    institution_login_id = '1007302745' # str | The institution login ID

    try:
        # Migrate Institution Login Accounts
        api_response = api_instance.migrate_institution_login_accounts(customer_id, institution_login_id)
        print("The response of AppRegistrationApi->migrate_institution_login_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRegistrationApi->migrate_institution_login_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **institution_login_id** | **str**| The institution login ID | 

### Return type

[**CustomerAccounts**](CustomerAccounts.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The migration succeeded |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_app_registration**
> RegisteredApplication modify_app_registration(pre_app_id, application)

Modify App Registration

Update a registered application.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.application import Application
from openapi_client.models.registered_application import RegisteredApplication
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
    api_instance = openapi_client.AppRegistrationApi(api_client)
    pre_app_id = '2581' # str | The application registration tracking ID
    application = openapi_client.Application() # Application | 

    try:
        # Modify App Registration
        api_response = api_instance.modify_app_registration(pre_app_id, application)
        print("The response of AppRegistrationApi->modify_app_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRegistrationApi->modify_app_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pre_app_id** | **str**| The application registration tracking ID | 
 **application** | [**Application**](Application.md)|  | 

### Return type

[**RegisteredApplication**](RegisteredApplication.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The app registration was updated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_app**
> RegisteredApplication register_app(application)

Register App

Register a new application to access financial institutions using OAuth connections.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.application import Application
from openapi_client.models.registered_application import RegisteredApplication
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
    api_instance = openapi_client.AppRegistrationApi(api_client)
    application = openapi_client.Application() # Application | 

    try:
        # Register App
        api_response = api_instance.register_app(application)
        print("The response of AppRegistrationApi->register_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRegistrationApi->register_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)|  | 

### Return type

[**RegisteredApplication**](RegisteredApplication.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The app registration was successfully created |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_customer_app_id**
> set_customer_app_id(customer_id, application_id)

Set Customer App ID

If you have multiple applications for a single client, and you want to register their applications to access financial institutions using OAuth connections, then use this API to assign applications to an existing customer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

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
    api_instance = openapi_client.AppRegistrationApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    application_id = '00278431-b712-4f30-a044-b611f25e533d' # str | The application ID

    try:
        # Set Customer App ID
        api_instance.set_customer_app_id(customer_id, application_id)
    except Exception as e:
        print("Exception when calling AppRegistrationApi->set_customer_app_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **application_id** | **str**| The application ID | 

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
**200** | The app was successfully assigned |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

