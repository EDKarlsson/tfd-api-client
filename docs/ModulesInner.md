# ModulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** | Module name | [optional] 
**module_id** | **str** | Module identifier | [optional] 
**image_url** | **str** | Module image path | [optional] 
**module_type** | **str** | Module type | [optional] 
**module_tier_id** | **str** | Module tier (Refer to /meta/tier API) | [optional] 
**module_socket_type** | **str** | Module slot socket type | [optional] 
**module_class** | **str** | Module class | [optional] 
**available_weapon_type** | **List[str]** | List of weapon types that can equip modules (refer to /meta/weapon-type API) | [optional] 
**available_descendant_id** | **List[str]** | List of descendant identifiers that can equip modules (refer to /meta/descendant API) | [optional] 
**available_module_slot_type** | **List[str]** | List of slot types that can equip modules | [optional] 
**module_stat** | [**List[ModulesInnerModuleStatInner]**](ModulesInnerModuleStatInner.md) | Module attribute information | [optional] 

## Example

```python
from tfd_api_client.models.modules_inner import ModulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModulesInner from a JSON string
modules_inner_instance = ModulesInner.from_json(json)
# print the JSON string representation of the object
print(ModulesInner.to_json())

# convert the object into a dict
modules_inner_dict = modules_inner_instance.to_dict()
# create an instance of ModulesInner from a dict
modules_inner_from_dict = ModulesInner.from_dict(modules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


