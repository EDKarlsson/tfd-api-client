# tfd_api_client.MetadataApi

All URIs are relative to *https://open.api.nexon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_meta_acquisition_details**](MetadataApi.md#get_meta_acquisition_details) | **GET** /static/tfd/meta/{language_code}/acquisition-detail.json | Retrieve acquisition source info metadata
[**get_meta_adapt_levels**](MetadataApi.md#get_meta_adapt_levels) | **GET** /static/tfd/meta/adapt-level.json | Retrieve adaptability level metadata
[**get_meta_amorphous_open_condition_descriptions**](MetadataApi.md#get_meta_amorphous_open_condition_descriptions) | **GET** /static/tfd/meta/{language_code}/amorphous-open-condition-description.json | Retrieve Amorphous Material opening location metadata
[**get_meta_amorphous_rewards**](MetadataApi.md#get_meta_amorphous_rewards) | **GET** /static/tfd/meta/amorphous-reward.json | Retrieve Amorphous Material open reward metadata
[**get_meta_arche_tuning_board_groups**](MetadataApi.md#get_meta_arche_tuning_board_groups) | **GET** /static/tfd/meta/arche-tuning-board-group.json | Retrieve Arche tuning board group metadata
[**get_meta_arche_tuning_boards**](MetadataApi.md#get_meta_arche_tuning_boards) | **GET** /static/tfd/meta/arche-tuning-board.json | Retrieve Arche tuning board metadata
[**get_meta_arche_tuning_nodes**](MetadataApi.md#get_meta_arche_tuning_nodes) | **GET** /static/tfd/meta/{language_code}/arche-tuning-node.json | Retrieve Arche tuning node metadata
[**get_meta_consumable_materials**](MetadataApi.md#get_meta_consumable_materials) | **GET** /static/tfd/meta/{language_code}/consumable-material.json | Retrieve consumable items metadata
[**get_meta_core_slots**](MetadataApi.md#get_meta_core_slots) | **GET** /static/tfd/meta/core-slot.json | Retrieve core slot metadata
[**get_meta_core_types**](MetadataApi.md#get_meta_core_types) | **GET** /static/tfd/meta/{language_code}/core-type.json | Retrieve core type metadata
[**get_meta_customizing_items**](MetadataApi.md#get_meta_customizing_items) | **GET** /static/tfd/meta/{language_code}/customizing-item.json | Retrieve customization item metadata
[**get_meta_descendant_groups**](MetadataApi.md#get_meta_descendant_groups) | **GET** /static/tfd/meta/{language_code}/descendant-group.json | Retrieve descendant group metadata
[**get_meta_descendant_level_details**](MetadataApi.md#get_meta_descendant_level_details) | **GET** /static/tfd/meta/descendant-level-detail.json | Retrieve EXP metadata by descendant level
[**get_meta_descendants**](MetadataApi.md#get_meta_descendants) | **GET** /static/tfd/meta/{language_code}/descendant.json | Retrieve descendant metadata
[**get_meta_external_components**](MetadataApi.md#get_meta_external_components) | **GET** /static/tfd/meta/{language_code}/external-component.json | Retrieve external component metadata
[**get_meta_fellow_level_details**](MetadataApi.md#get_meta_fellow_level_details) | **GET** /static/tfd/meta/fellow-level-detail.json | Retrieve EXP metadata by fellow level
[**get_meta_fellows**](MetadataApi.md#get_meta_fellows) | **GET** /static/tfd/meta/{language_code}/fellow.json | Retrieve fellow metadata
[**get_meta_mastery_rank_level_details**](MetadataApi.md#get_meta_mastery_rank_level_details) | **GET** /static/tfd/meta/mastery-rank-level-detail.json | Retrieve EXP metadata by Mastery Rank
[**get_meta_medals**](MetadataApi.md#get_meta_medals) | **GET** /static/tfd/meta/{language_code}/medal.json | Retrieve medal meta data
[**get_meta_modules**](MetadataApi.md#get_meta_modules) | **GET** /static/tfd/meta/{language_code}/module.json | Retrieve module metadata
[**get_meta_reactors**](MetadataApi.md#get_meta_reactors) | **GET** /static/tfd/meta/{language_code}/reactor.json | Retrieve Reactor metadata
[**get_meta_rewards**](MetadataApi.md#get_meta_rewards) | **GET** /static/tfd/meta/{language_code}/reward.json | Retrieve Difficulty Level Rewards metadata
[**get_meta_stats**](MetadataApi.md#get_meta_stats) | **GET** /static/tfd/meta/{language_code}/stat.json | Retrieve base stat metadata
[**get_meta_tiers**](MetadataApi.md#get_meta_tiers) | **GET** /static/tfd/meta/{language_code}/tier.json | Retrieve tier metadata
[**get_meta_titles**](MetadataApi.md#get_meta_titles) | **GET** /static/tfd/meta/{language_code}/title.json | Retrieve Title metadata
[**get_meta_void_battles**](MetadataApi.md#get_meta_void_battles) | **GET** /static/tfd/meta/{language_code}/void-battle.json | Retrieve Void Intercept Battle metadata
[**get_meta_weapon_types**](MetadataApi.md#get_meta_weapon_types) | **GET** /static/tfd/meta/{language_code}/weapon-type.json | Retrieve weapon type metadata
[**get_meta_weapons**](MetadataApi.md#get_meta_weapons) | **GET** /static/tfd/meta/{language_code}/weapon.json | Retrieve weapon metadata
[**static_tfd_meta_language_code_research_json_get**](MetadataApi.md#static_tfd_meta_language_code_research_json_get) | **GET** /static/tfd/meta/{language_code}/research.json | Retrieve research info metadata


# **get_meta_acquisition_details**
> List[AcquisitionDetailsInner] get_meta_acquisition_details(language_code)

Retrieve acquisition source info metadata

Retrieves metadata for acquisition source information.

### Example


```python
import tfd_api_client
from tfd_api_client.models.acquisition_details_inner import AcquisitionDetailsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve acquisition source info metadata
        api_response = api_instance.get_meta_acquisition_details(language_code)
        print("The response of MetadataApi->get_meta_acquisition_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_acquisition_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[AcquisitionDetailsInner]**](AcquisitionDetailsInner.md)

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

# **get_meta_adapt_levels**
> List[AdaptLevelsInner] get_meta_adapt_levels()

Retrieve adaptability level metadata

Retrieves adaptability level metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.adapt_levels_inner import AdaptLevelsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve adaptability level metadata
        api_response = api_instance.get_meta_adapt_levels()
        print("The response of MetadataApi->get_meta_adapt_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_adapt_levels: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AdaptLevelsInner]**](AdaptLevelsInner.md)

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

# **get_meta_amorphous_open_condition_descriptions**
> List[AmorphousOpenConditionDescriptionsInner] get_meta_amorphous_open_condition_descriptions(language_code)

Retrieve Amorphous Material opening location metadata

Retrieves metadata for the locations where Amorphous Materials are opened.

### Example


```python
import tfd_api_client
from tfd_api_client.models.amorphous_open_condition_descriptions_inner import AmorphousOpenConditionDescriptionsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Amorphous Material opening location metadata
        api_response = api_instance.get_meta_amorphous_open_condition_descriptions(language_code)
        print("The response of MetadataApi->get_meta_amorphous_open_condition_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_amorphous_open_condition_descriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[AmorphousOpenConditionDescriptionsInner]**](AmorphousOpenConditionDescriptionsInner.md)

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

# **get_meta_amorphous_rewards**
> List[AmorphousRewardsInner] get_meta_amorphous_rewards()

Retrieve Amorphous Material open reward metadata

Retrieves metadata for rewards received when opening Amorphous Materials in the game.

### Example


```python
import tfd_api_client
from tfd_api_client.models.amorphous_rewards_inner import AmorphousRewardsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve Amorphous Material open reward metadata
        api_response = api_instance.get_meta_amorphous_rewards()
        print("The response of MetadataApi->get_meta_amorphous_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_amorphous_rewards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AmorphousRewardsInner]**](AmorphousRewardsInner.md)

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

# **get_meta_arche_tuning_board_groups**
> List[ArcheTuningBoardGroupsInner] get_meta_arche_tuning_board_groups()

Retrieve Arche tuning board group metadata

Retrieves Arche tuning board group metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.arche_tuning_board_groups_inner import ArcheTuningBoardGroupsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve Arche tuning board group metadata
        api_response = api_instance.get_meta_arche_tuning_board_groups()
        print("The response of MetadataApi->get_meta_arche_tuning_board_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_arche_tuning_board_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ArcheTuningBoardGroupsInner]**](ArcheTuningBoardGroupsInner.md)

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

# **get_meta_arche_tuning_boards**
> List[ArcheTuningBoardsInner] get_meta_arche_tuning_boards()

Retrieve Arche tuning board metadata

Retrieves Arche tuning board metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.arche_tuning_boards_inner import ArcheTuningBoardsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve Arche tuning board metadata
        api_response = api_instance.get_meta_arche_tuning_boards()
        print("The response of MetadataApi->get_meta_arche_tuning_boards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_arche_tuning_boards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ArcheTuningBoardsInner]**](ArcheTuningBoardsInner.md)

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

# **get_meta_arche_tuning_nodes**
> List[ArcheTuningNodesInner] get_meta_arche_tuning_nodes(language_code)

Retrieve Arche tuning node metadata

Retrieves Arche tuning node metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.arche_tuning_nodes_inner import ArcheTuningNodesInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | Language codes

    try:
        # Retrieve Arche tuning node metadata
        api_response = api_instance.get_meta_arche_tuning_nodes(language_code)
        print("The response of MetadataApi->get_meta_arche_tuning_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_arche_tuning_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| Language codes | 

### Return type

[**List[ArcheTuningNodesInner]**](ArcheTuningNodesInner.md)

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

# **get_meta_consumable_materials**
> List[ConsumableMaterialsInner] get_meta_consumable_materials(language_code)

Retrieve consumable items metadata

Retrieves metadata for consumable items.

### Example


```python
import tfd_api_client
from tfd_api_client.models.consumable_materials_inner import ConsumableMaterialsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve consumable items metadata
        api_response = api_instance.get_meta_consumable_materials(language_code)
        print("The response of MetadataApi->get_meta_consumable_materials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_consumable_materials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ConsumableMaterialsInner]**](ConsumableMaterialsInner.md)

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

# **get_meta_core_slots**
> List[CoreSlotsInner] get_meta_core_slots()

Retrieve core slot metadata

Retrieves metadata for core slots.

### Example


```python
import tfd_api_client
from tfd_api_client.models.core_slots_inner import CoreSlotsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve core slot metadata
        api_response = api_instance.get_meta_core_slots()
        print("The response of MetadataApi->get_meta_core_slots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_core_slots: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CoreSlotsInner]**](CoreSlotsInner.md)

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

# **get_meta_core_types**
> List[CoreTypesInner] get_meta_core_types(language_code)

Retrieve core type metadata

Retrieves metadata information for core types.

### Example


```python
import tfd_api_client
from tfd_api_client.models.core_types_inner import CoreTypesInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve core type metadata
        api_response = api_instance.get_meta_core_types(language_code)
        print("The response of MetadataApi->get_meta_core_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_core_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[CoreTypesInner]**](CoreTypesInner.md)

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

# **get_meta_customizing_items**
> List[CustomizingItemsInner] get_meta_customizing_items(language_code)

Retrieve customization item metadata

Retrieves customization item metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.customizing_items_inner import CustomizingItemsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | Language codes

    try:
        # Retrieve customization item metadata
        api_response = api_instance.get_meta_customizing_items(language_code)
        print("The response of MetadataApi->get_meta_customizing_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_customizing_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| Language codes | 

### Return type

[**List[CustomizingItemsInner]**](CustomizingItemsInner.md)

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

# **get_meta_descendant_groups**
> List[DescendantGroupsInner] get_meta_descendant_groups(language_code)

Retrieve descendant group metadata

Retrieves descendant group metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.descendant_groups_inner import DescendantGroupsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | Language codes

    try:
        # Retrieve descendant group metadata
        api_response = api_instance.get_meta_descendant_groups(language_code)
        print("The response of MetadataApi->get_meta_descendant_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_descendant_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| Language codes | 

### Return type

[**List[DescendantGroupsInner]**](DescendantGroupsInner.md)

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

# **get_meta_descendant_level_details**
> List[DescendantLevelDetailsInner] get_meta_descendant_level_details()

Retrieve EXP metadata by descendant level

Retrieves the required EXP information for each Descendant level.

### Example


```python
import tfd_api_client
from tfd_api_client.models.descendant_level_details_inner import DescendantLevelDetailsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve EXP metadata by descendant level
        api_response = api_instance.get_meta_descendant_level_details()
        print("The response of MetadataApi->get_meta_descendant_level_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_descendant_level_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DescendantLevelDetailsInner]**](DescendantLevelDetailsInner.md)

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

# **get_meta_descendants**
> List[DescendantsInner] get_meta_descendants(language_code)

Retrieve descendant metadata

Retrieves descendant metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.descendants_inner import DescendantsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve descendant metadata
        api_response = api_instance.get_meta_descendants(language_code)
        print("The response of MetadataApi->get_meta_descendants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_descendants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[DescendantsInner]**](DescendantsInner.md)

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

# **get_meta_external_components**
> List[ExternalComponentsInner] get_meta_external_components(language_code)

Retrieve external component metadata

Retrieves external component metadata.</br> This API only provides path information. You can check it via a separate client.

### Example


```python
import tfd_api_client
from tfd_api_client.models.external_components_inner import ExternalComponentsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve external component metadata
        api_response = api_instance.get_meta_external_components(language_code)
        print("The response of MetadataApi->get_meta_external_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_external_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ExternalComponentsInner]**](ExternalComponentsInner.md)

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

# **get_meta_fellow_level_details**
> List[FellowLevelDetailsInner] get_meta_fellow_level_details()

Retrieve EXP metadata by fellow level

Retrieves required EXP metadata by fellow level.

### Example


```python
import tfd_api_client
from tfd_api_client.models.fellow_level_details_inner import FellowLevelDetailsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve EXP metadata by fellow level
        api_response = api_instance.get_meta_fellow_level_details()
        print("The response of MetadataApi->get_meta_fellow_level_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_fellow_level_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FellowLevelDetailsInner]**](FellowLevelDetailsInner.md)

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

# **get_meta_fellows**
> List[FellowsInner] get_meta_fellows(language_code)

Retrieve fellow metadata

Retrieves metadata for fellow metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.fellows_inner import FellowsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve fellow metadata
        api_response = api_instance.get_meta_fellows(language_code)
        print("The response of MetadataApi->get_meta_fellows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_fellows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[FellowsInner]**](FellowsInner.md)

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

# **get_meta_mastery_rank_level_details**
> List[MasteryRankLevelDetailsInner] get_meta_mastery_rank_level_details()

Retrieve EXP metadata by Mastery Rank

Retrieves the required EXP information for each Mastery Rank.

### Example


```python
import tfd_api_client
from tfd_api_client.models.mastery_rank_level_details_inner import MasteryRankLevelDetailsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)

    try:
        # Retrieve EXP metadata by Mastery Rank
        api_response = api_instance.get_meta_mastery_rank_level_details()
        print("The response of MetadataApi->get_meta_mastery_rank_level_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_mastery_rank_level_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MasteryRankLevelDetailsInner]**](MasteryRankLevelDetailsInner.md)

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

# **get_meta_medals**
> List[MedalsInner] get_meta_medals(language_code)

Retrieve medal meta data

Retrieves medal meta data.

### Example


```python
import tfd_api_client
from tfd_api_client.models.medals_inner import MedalsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | Language code

    try:
        # Retrieve medal meta data
        api_response = api_instance.get_meta_medals(language_code)
        print("The response of MetadataApi->get_meta_medals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_medals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| Language code | 

### Return type

[**List[MedalsInner]**](MedalsInner.md)

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

# **get_meta_modules**
> List[ModulesInner] get_meta_modules(language_code)

Retrieve module metadata

Retrieves module metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.modules_inner import ModulesInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve module metadata
        api_response = api_instance.get_meta_modules(language_code)
        print("The response of MetadataApi->get_meta_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_modules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ModulesInner]**](ModulesInner.md)

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

# **get_meta_reactors**
> List[ReactorsInner] get_meta_reactors(language_code)

Retrieve Reactor metadata

Retrieves Reactor metadata.<br> This API only provides path information. You can check it via a separate client.

### Example


```python
import tfd_api_client
from tfd_api_client.models.reactors_inner import ReactorsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Reactor metadata
        api_response = api_instance.get_meta_reactors(language_code)
        print("The response of MetadataApi->get_meta_reactors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_reactors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ReactorsInner]**](ReactorsInner.md)

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

# **get_meta_rewards**
> List[RewardsInner] get_meta_rewards(language_code)

Retrieve Difficulty Level Rewards metadata

Retrieves Difficulty Level Rewards metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.rewards_inner import RewardsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Difficulty Level Rewards metadata
        api_response = api_instance.get_meta_rewards(language_code)
        print("The response of MetadataApi->get_meta_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[RewardsInner]**](RewardsInner.md)

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

# **get_meta_stats**
> List[StatsInner] get_meta_stats(language_code)

Retrieve base stat metadata

Retrieves base stat metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.stats_inner import StatsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve base stat metadata
        api_response = api_instance.get_meta_stats(language_code)
        print("The response of MetadataApi->get_meta_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[StatsInner]**](StatsInner.md)

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

# **get_meta_tiers**
> List[TiersInner] get_meta_tiers(language_code)

Retrieve tier metadata

Retrieves tier metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.tiers_inner import TiersInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve tier metadata
        api_response = api_instance.get_meta_tiers(language_code)
        print("The response of MetadataApi->get_meta_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_tiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[TiersInner]**](TiersInner.md)

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

# **get_meta_titles**
> List[TitlesInner] get_meta_titles(language_code)

Retrieve Title metadata

Retrieves Title metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.titles_inner import TitlesInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Title metadata
        api_response = api_instance.get_meta_titles(language_code)
        print("The response of MetadataApi->get_meta_titles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_titles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[TitlesInner]**](TitlesInner.md)

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

# **get_meta_void_battles**
> List[VoidBattlesInner] get_meta_void_battles(language_code)

Retrieve Void Intercept Battle metadata

Retrieves Void Intercept Battle metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.void_battles_inner import VoidBattlesInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve Void Intercept Battle metadata
        api_response = api_instance.get_meta_void_battles(language_code)
        print("The response of MetadataApi->get_meta_void_battles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_void_battles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[VoidBattlesInner]**](VoidBattlesInner.md)

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

# **get_meta_weapon_types**
> List[WeaponTypesInner] get_meta_weapon_types(language_code)

Retrieve weapon type metadata

Retrieves metadata for weapon types.

### Example


```python
import tfd_api_client
from tfd_api_client.models.weapon_types_inner import WeaponTypesInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve weapon type metadata
        api_response = api_instance.get_meta_weapon_types(language_code)
        print("The response of MetadataApi->get_meta_weapon_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_weapon_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[WeaponTypesInner]**](WeaponTypesInner.md)

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

# **get_meta_weapons**
> List[WeaponsInner] get_meta_weapons(language_code)

Retrieve weapon metadata

Retrieves weapon metadata.<br> This API only provides path information. You can check it via a separate client.

### Example


```python
import tfd_api_client
from tfd_api_client.models.weapons_inner import WeaponsInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve weapon metadata
        api_response = api_instance.get_meta_weapons(language_code)
        print("The response of MetadataApi->get_meta_weapons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_meta_weapons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[WeaponsInner]**](WeaponsInner.md)

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

# **static_tfd_meta_language_code_research_json_get**
> List[ResearchInner] static_tfd_meta_language_code_research_json_get(language_code)

Retrieve research info metadata

Retrieves research info metadata.

### Example


```python
import tfd_api_client
from tfd_api_client.models.research_inner import ResearchInner
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
    api_instance = tfd_api_client.MetadataApi(api_client)
    language_code = 'language_code_example' # str | language code

    try:
        # Retrieve research info metadata
        api_response = api_instance.static_tfd_meta_language_code_research_json_get(language_code)
        print("The response of MetadataApi->static_tfd_meta_language_code_research_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->static_tfd_meta_language_code_research_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_code** | **str**| language code | 

### Return type

[**List[ResearchInner]**](ResearchInner.md)

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

