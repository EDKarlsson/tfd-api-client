# ModulesInnerModuleStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Module enchantment level | [optional] 
**module_capacity** | **float** | Module capacity | [optional] 
**value** | **str** | Module attribute value | [optional] 

## Example

```python
from tfd_api_client.models.modules_inner_module_stat_inner import ModulesInnerModuleStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModulesInnerModuleStatInner from a JSON string
modules_inner_module_stat_inner_instance = ModulesInnerModuleStatInner.from_json(json)
# print the JSON string representation of the object
print(ModulesInnerModuleStatInner.to_json())

# convert the object into a dict
modules_inner_module_stat_inner_dict = modules_inner_module_stat_inner_instance.to_dict()
# create an instance of ModulesInnerModuleStatInner from a dict
modules_inner_module_stat_inner_from_dict = ModulesInnerModuleStatInner.from_dict(modules_inner_module_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


