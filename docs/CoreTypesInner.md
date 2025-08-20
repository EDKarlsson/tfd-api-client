# CoreTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_type_id** | **str** | Core type identifier | [optional] 
**core_type** | **str** | Core type | [optional] 
**core_option** | [**List[CoreTypesInnerCoreOptionInner]**](CoreTypesInnerCoreOptionInner.md) | core type options | [optional] 

## Example

```python
from tfd_api_client.models.core_types_inner import CoreTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoreTypesInner from a JSON string
core_types_inner_instance = CoreTypesInner.from_json(json)
# print the JSON string representation of the object
print(CoreTypesInner.to_json())

# convert the object into a dict
core_types_inner_dict = core_types_inner_instance.to_dict()
# create an instance of CoreTypesInner from a dict
core_types_inner_from_dict = CoreTypesInner.from_dict(core_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


