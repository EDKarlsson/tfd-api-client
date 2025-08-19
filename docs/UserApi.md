# tfd_api_client.UserApi

All URIs are relative to *https://open.api.nexon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**thefirstdescendant_get_user_arche_tuning**](UserApi.md#thefirstdescendant_get_user_arche_tuning) | **GET** /tfd/v1/user/arche-tuning | Retrieve Arche tuning information
[**thefirstdescendant_get_user_basic**](UserApi.md#thefirstdescendant_get_user_basic) | **GET** /tfd/v1/user/basic | Retrieve basic information
[**thefirstdescendant_get_user_descendant**](UserApi.md#thefirstdescendant_get_user_descendant) | **GET** /tfd/v1/user/descendant | Retrieve equipped descendant information
[**thefirstdescendant_get_user_external_component**](UserApi.md#thefirstdescendant_get_user_external_component) | **GET** /tfd/v1/user/external-component | Retrieve equipped external component information
[**thefirstdescendant_get_user_id**](UserApi.md#thefirstdescendant_get_user_id) | **GET** /tfd/v1/id | Retrieve account identifier (OUID)
[**thefirstdescendant_get_user_reactor**](UserApi.md#thefirstdescendant_get_user_reactor) | **GET** /tfd/v1/user/reactor | Retrieve equipped Reactor information
[**thefirstdescendant_get_user_weapon**](UserApi.md#thefirstdescendant_get_user_weapon) | **GET** /tfd/v1/user/weapon | Retrieve equipped weapon information


# **thefirstdescendant_get_user_arche_tuning**
> UserArcheTuning thefirstdescendant_get_user_arche_tuning(x_nxopen_api_key, ouid, descendant_group_id)

Retrieve Arche tuning information

Retrieves the Arche tuning information.
- Returns the activated nodes and their coordinates for each descendant group.

### Example


```python
import tfd_api_client
from tfd_api_client.models.user_arche_tuning import UserArcheTuning
from tfd_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tfd_api_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with tfd_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tfd_api_client.UserApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    ouid = 'ouid_example' # str | Account identifier
    descendant_group_id = 'descendant_group_id_example' # str | Descendant group identifier (Refer to /meta/descendant-group API)

    try:
        # Retrieve Arche tuning information
        api_response = api_instance.thefirstdescendant_get_user_arche_tuning(x_nxopen_api_key, ouid, descendant_group_id)
        print("The response of UserApi->thefirstdescendant_get_user_arche_tuning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->thefirstdescendant_get_user_arche_tuning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **ouid** | **str**| Account identifier | 
 **descendant_group_id** | **str**| Descendant group identifier (Refer to /meta/descendant-group API) | 

### Return type

[**UserArcheTuning**](UserArcheTuning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thefirstdescendant_get_user_basic**
> UserBasic thefirstdescendant_get_user_basic(x_nxopen_api_key, ouid)

Retrieve basic information

Retrieves basic information.

### Example


```python
import tfd_api_client
from tfd_api_client.models.user_basic import UserBasic
from tfd_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tfd_api_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with tfd_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tfd_api_client.UserApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    ouid = 'ouid_example' # str | OUID

    try:
        # Retrieve basic information
        api_response = api_instance.thefirstdescendant_get_user_basic(x_nxopen_api_key, ouid)
        print("The response of UserApi->thefirstdescendant_get_user_basic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->thefirstdescendant_get_user_basic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **ouid** | **str**| OUID | 

### Return type

[**UserBasic**](UserBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thefirstdescendant_get_user_descendant**
> UserDescendant thefirstdescendant_get_user_descendant(x_nxopen_api_key, ouid)

Retrieve equipped descendant information

Retrieves information about the equipped descendant.<br>- For equipped module and customization information, it will be updated after you reconnect to the game or complete content with active matchmaking.

### Example


```python
import tfd_api_client
from tfd_api_client.models.user_descendant import UserDescendant
from tfd_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tfd_api_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with tfd_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tfd_api_client.UserApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    ouid = 'ouid_example' # str | OUID

    try:
        # Retrieve equipped descendant information
        api_response = api_instance.thefirstdescendant_get_user_descendant(x_nxopen_api_key, ouid)
        print("The response of UserApi->thefirstdescendant_get_user_descendant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->thefirstdescendant_get_user_descendant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **ouid** | **str**| OUID | 

### Return type

[**UserDescendant**](UserDescendant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thefirstdescendant_get_user_external_component**
> UserExternalComponent thefirstdescendant_get_user_external_component(x_nxopen_api_key, language_code, ouid)

Retrieve equipped external component information

Retrieves information about external components equipped in all slots.

### Example


```python
import tfd_api_client
from tfd_api_client.models.user_external_component import UserExternalComponent
from tfd_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tfd_api_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with tfd_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tfd_api_client.UserApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    language_code = 'language_code_example' # str | language code
    ouid = 'ouid_example' # str | OUID

    try:
        # Retrieve equipped external component information
        api_response = api_instance.thefirstdescendant_get_user_external_component(x_nxopen_api_key, language_code, ouid)
        print("The response of UserApi->thefirstdescendant_get_user_external_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->thefirstdescendant_get_user_external_component: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **language_code** | **str**| language code | 
 **ouid** | **str**| OUID | 

### Return type

[**UserExternalComponent**](UserExternalComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thefirstdescendant_get_user_id**
> User thefirstdescendant_get_user_id(x_nxopen_api_key, user_name)

Retrieve account identifier (OUID)

Retrieves the account identifier (OUID).

### Example


```python
import tfd_api_client
from tfd_api_client.models.user import User
from tfd_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tfd_api_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with tfd_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tfd_api_client.UserApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    user_name = 'Nickname#1234' # str | Nickname

    try:
        # Retrieve account identifier (OUID)
        api_response = api_instance.thefirstdescendant_get_user_id(x_nxopen_api_key, user_name)
        print("The response of UserApi->thefirstdescendant_get_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->thefirstdescendant_get_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **user_name** | **str**| Nickname | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thefirstdescendant_get_user_reactor**
> UserReactor thefirstdescendant_get_user_reactor(x_nxopen_api_key, language_code, ouid)

Retrieve equipped Reactor information

Retrieves information about the equipped Reactor.

### Example


```python
import tfd_api_client
from tfd_api_client.models.user_reactor import UserReactor
from tfd_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tfd_api_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with tfd_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tfd_api_client.UserApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    language_code = 'language_code_example' # str | language code
    ouid = 'ouid_example' # str | OUID

    try:
        # Retrieve equipped Reactor information
        api_response = api_instance.thefirstdescendant_get_user_reactor(x_nxopen_api_key, language_code, ouid)
        print("The response of UserApi->thefirstdescendant_get_user_reactor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->thefirstdescendant_get_user_reactor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **language_code** | **str**| language code | 
 **ouid** | **str**| OUID | 

### Return type

[**UserReactor**](UserReactor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thefirstdescendant_get_user_weapon**
> UserWeapon thefirstdescendant_get_user_weapon(x_nxopen_api_key, language_code, ouid)

Retrieve equipped weapon information

Retrieves information about weapons equipped in all slots.<br>- For equipped module information, it will be updated after you reconnect to the game or complete content with active matchmaking.

### Example


```python
import tfd_api_client
from tfd_api_client.models.user_weapon import UserWeapon
from tfd_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open.api.nexon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = tfd_api_client.Configuration(
    host = "https://open.api.nexon.com"
)


# Enter a context with an instance of the API client
with tfd_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tfd_api_client.UserApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    language_code = 'language_code_example' # str | language code
    ouid = 'ouid_example' # str | OUID

    try:
        # Retrieve equipped weapon information
        api_response = api_instance.thefirstdescendant_get_user_weapon(x_nxopen_api_key, language_code, ouid)
        print("The response of UserApi->thefirstdescendant_get_user_weapon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->thefirstdescendant_get_user_weapon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **language_code** | **str**| language code | 
 **ouid** | **str**| OUID | 

### Return type

[**UserWeapon**](UserWeapon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SUCCESS |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

