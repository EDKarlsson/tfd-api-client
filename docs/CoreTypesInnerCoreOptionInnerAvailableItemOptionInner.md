# CoreTypesInnerCoreOptionInnerAvailableItemOptionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_option** | **str** | Option name | [optional] 
**option_type** | **str** | Option category | [optional] 
**option_grade** | **str** | Option grade&lt;br&gt;- Higher grades provide better effect values. | [optional] 
**option_effect** | [**CoreTypesInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect**](CoreTypesInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect.md) |  | [optional] 
**rate** | **float** | Probability of the option appearing | [optional] 

## Example

```python
from tfd_api_client.models.core_types_inner_core_option_inner_available_item_option_inner import CoreTypesInnerCoreOptionInnerAvailableItemOptionInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoreTypesInnerCoreOptionInnerAvailableItemOptionInner from a JSON string
core_types_inner_core_option_inner_available_item_option_inner_instance = CoreTypesInnerCoreOptionInnerAvailableItemOptionInner.from_json(json)
# print the JSON string representation of the object
print(CoreTypesInnerCoreOptionInnerAvailableItemOptionInner.to_json())

# convert the object into a dict
core_types_inner_core_option_inner_available_item_option_inner_dict = core_types_inner_core_option_inner_available_item_option_inner_instance.to_dict()
# create an instance of CoreTypesInnerCoreOptionInnerAvailableItemOptionInner from a dict
core_types_inner_core_option_inner_available_item_option_inner_from_dict = CoreTypesInnerCoreOptionInnerAvailableItemOptionInner.from_dict(core_types_inner_core_option_inner_available_item_option_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


