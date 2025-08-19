# CoreTypeResponseInnerCoreOptionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_option_id** | **str** | core type option identifier | [optional] 
**detail** | [**List[CoreTypeResponseInnerCoreOptionInnerDetailInner]**](CoreTypeResponseInnerCoreOptionInnerDetailInner.md) | Detailed information on core type options | [optional] 
**available_item_option** | [**List[CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner]**](CoreTypeResponseInnerCoreOptionInnerAvailableItemOptionInner.md) | Item options | [optional] 

## Example

```python
from tfd_api_client.models.core_type_response_inner_core_option_inner import CoreTypeResponseInnerCoreOptionInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoreTypeResponseInnerCoreOptionInner from a JSON string
core_type_response_inner_core_option_inner_instance = CoreTypeResponseInnerCoreOptionInner.from_json(json)
# print the JSON string representation of the object
print(CoreTypeResponseInnerCoreOptionInner.to_json())

# convert the object into a dict
core_type_response_inner_core_option_inner_dict = core_type_response_inner_core_option_inner_instance.to_dict()
# create an instance of CoreTypeResponseInnerCoreOptionInner from a dict
core_type_response_inner_core_option_inner_from_dict = CoreTypeResponseInnerCoreOptionInner.from_dict(core_type_response_inner_core_option_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


