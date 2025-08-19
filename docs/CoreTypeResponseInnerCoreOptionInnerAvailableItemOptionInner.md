# CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_option** | **str** | Option name | [optional] 
**option_type** | **str** | Option category | [optional] 
**option_grade** | **str** | Option grade&lt;br&gt;- Higher grades provide better effect values. | [optional] 
**option_effect** | [**CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect**](CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInnerOptionEffect.md) |  | [optional] 
**rate** | **float** | Probability of the option appearing | [optional] 

## Example

```python
from tfd_api_client.models.core_type_response_inner_core_option_inner_available_item_option_inner import CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner from a JSON string
core_type_response_inner_core_option_inner_available_item_option_inner_instance = CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner.from_json(json)
# print the JSON string representation of the object
print(CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner.to_json())

# convert the object into a dict
core_type_response_inner_core_option_inner_available_item_option_inner_dict = core_type_response_inner_core_option_inner_available_item_option_inner_instance.to_dict()
# create an instance of CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner from a dict
core_type_response_inner_core_option_inner_available_item_option_inner_from_dict = CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner.from_dict(core_type_response_inner_core_option_inner_available_item_option_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


