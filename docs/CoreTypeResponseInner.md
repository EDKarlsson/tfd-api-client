# CoreTypeResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_type_id** | **str** | Core type identifier | [optional] 
**core_type** | **str** | Core type | [optional] 
**core_option** | [**List[CoreTypeResponseInnerCoreOptionInner]**](CoreTypeResponseInnerCoreOptionInner.md) | core type options | [optional] 

## Example

```python
from tfd_api_client.models.core_type_response_inner import CoreTypeResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoreTypeResponseInner from a JSON string
core_type_response_inner_instance = CoreTypeResponseInner.from_json(json)
# print the JSON string representation of the object
print(CoreTypeResponseInner.to_json())

# convert the object into a dict
core_type_response_inner_dict = core_type_response_inner_instance.to_dict()
# create an instance of CoreTypeResponseInner from a dict
core_type_response_inner_from_dict = CoreTypeResponseInner.from_dict(core_type_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


