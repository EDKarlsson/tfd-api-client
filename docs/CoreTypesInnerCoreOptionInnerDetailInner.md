# CoreTypesInnerCoreOptionInnerDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_option_grade** | **float** | Core option grade&lt;br&gt;- Higher grades provide better effect values. | [optional] 
**required_core_item** | [**CoreTypesInnerCoreOptionInnerDetailInnerRequiredCoreItem**](CoreTypesInnerCoreOptionInnerDetailInnerRequiredCoreItem.md) |  | [optional] 

## Example

```python
from tfd_api_client.models.core_types_inner_core_option_inner_detail_inner import CoreTypesInnerCoreOptionInnerDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoreTypesInnerCoreOptionInnerDetailInner from a JSON string
core_types_inner_core_option_inner_detail_inner_instance = CoreTypesInnerCoreOptionInnerDetailInner.from_json(json)
# print the JSON string representation of the object
print(CoreTypesInnerCoreOptionInnerDetailInner.to_json())

# convert the object into a dict
core_types_inner_core_option_inner_detail_inner_dict = core_types_inner_core_option_inner_detail_inner_instance.to_dict()
# create an instance of CoreTypesInnerCoreOptionInnerDetailInner from a dict
core_types_inner_core_option_inner_detail_inner_from_dict = CoreTypesInnerCoreOptionInnerDetailInner.from_dict(core_types_inner_core_option_inner_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


