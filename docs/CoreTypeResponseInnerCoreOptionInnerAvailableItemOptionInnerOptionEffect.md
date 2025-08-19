# CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_id** | **str** | Option effect stat identifier (refer to /meta/stat API) | [optional] 
**operator_type** | **str** | Stat operation type (Add:addition, Multiply:multiplication) | [optional] 
**min_stat_value** | **float** | Minimum stat value | [optional] 
**max_stat_value** | **float** | Maximum stat value | [optional] 

## Example

```python
from tfd_api_client.models.core_type_response_inner_core_option_inner_available_item_option_inner_option_effect import CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect

# TODO update the JSON string below
json = "{}"
# create an instance of CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect from a JSON string
core_type_response_inner_core_option_inner_available_item_option_inner_option_effect_instance = CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect.from_json(json)
# print the JSON string representation of the object
print(CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect.to_json())

# convert the object into a dict
core_type_response_inner_core_option_inner_available_item_option_inner_option_effect_dict = core_type_response_inner_core_option_inner_available_item_option_inner_option_effect_instance.to_dict()
# create an instance of CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect from a dict
core_type_response_inner_core_option_inner_available_item_option_inner_option_effect_from_dict = CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect.from_dict(core_type_response_inner_core_option_inner_available_item_option_inner_option_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


