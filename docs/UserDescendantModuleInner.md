# UserDescendantModuleInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_slot_id** | **str** | Module slot identifier | [optional] 
**module_id** | **str** | Module identifier (Refer to /meta/module API) | [optional] 
**module_enchant_level** | **float** | Module enchantment level | [optional] 

## Example

```python
from tfd_api_client.models.user_descendant_module_inner import UserDescendantModuleInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserDescendantModuleInner from a JSON string
user_descendant_module_inner_instance = UserDescendantModuleInner.from_json(json)
# print the JSON string representation of the object
print(UserDescendantModuleInner.to_json())

# convert the object into a dict
user_descendant_module_inner_dict = user_descendant_module_inner_instance.to_dict()
# create an instance of UserDescendantModuleInner from a dict
user_descendant_module_inner_from_dict = UserDescendantModuleInner.from_dict(user_descendant_module_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


