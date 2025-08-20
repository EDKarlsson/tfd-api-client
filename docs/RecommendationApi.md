# tfd_api_client.RecommendationApi

All URIs are relative to *https://open.api.nexon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tfd_v1_recommendation_module_get**](RecommendationApi.md#tfd_v1_recommendation_module_get) | **GET** /tfd/v1/recommendation/module | Module recommendation


# **tfd_v1_recommendation_module_get**
> ModuleRecommendations tfd_v1_recommendation_module_get(x_nxopen_api_key, descendant_id, weapon_id, void_battle_id, period)

Module recommendation

Recommends modules suited to the user.

### Example


```python
import tfd_api_client
from tfd_api_client.models.module_recommendations import ModuleRecommendations
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
    api_instance = tfd_api_client.RecommendationApi(api_client)
    x_nxopen_api_key = 'x_nxopen_api_key_example' # str | API KEY
    descendant_id = 'descendant_id_example' # str | Descendant identifier (Refer to /meta/descendant API)
    weapon_id = 'weapon_id_example' # str | Weapon identifier (Refer to /meta/weapon API)
    void_battle_id = 'void_battle_id_example' # str | Void Intercept Battle identifier (Refer to /meta/void-battle API)
    period = 'period_example' # str | Query period - 0: last 7 days - 1: last 30 days - 2: all time 

    try:
        # Module recommendation
        api_response = api_instance.tfd_v1_recommendation_module_get(x_nxopen_api_key, descendant_id, weapon_id, void_battle_id, period)
        print("The response of RecommendationApi->tfd_v1_recommendation_module_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationApi->tfd_v1_recommendation_module_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nxopen_api_key** | **str**| API KEY | 
 **descendant_id** | **str**| Descendant identifier (Refer to /meta/descendant API) | 
 **weapon_id** | **str**| Weapon identifier (Refer to /meta/weapon API) | 
 **void_battle_id** | **str**| Void Intercept Battle identifier (Refer to /meta/void-battle API) | 
 **period** | **str**| Query period - 0: last 7 days - 1: last 30 days - 2: all time  | 

### Return type

[**ModuleRecommendations**](ModuleRecommendations.md)

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

