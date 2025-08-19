# ModuleResponseInnerModuleStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Module enchantment level | [optional] 
**module_capacity** | **float** | Module capacity | [optional] 
**value** | **str** | Module attribute value | [optional] 

## Example

```python
from tfd_api_client.models.module_response_inner_module_stat_inner import ModuleResponseInnerModuleStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleResponseInnerModuleStatInner from a JSON string
module_response_inner_module_stat_inner_instance = ModuleResponseInnerModuleStatInner.from_json(json)
# print the JSON string representation of the object
print(ModuleResponseInnerModuleStatInner.to_json())

# convert the object into a dict
module_response_inner_module_stat_inner_dict = module_response_inner_module_stat_inner_instance.to_dict()
# create an instance of ModuleResponseInnerModuleStatInner from a dict
module_response_inner_module_stat_inner_from_dict = ModuleResponseInnerModuleStatInner.from_dict(module_response_inner_module_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


