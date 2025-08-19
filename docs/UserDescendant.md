# UserDescendant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ouid** | **str** | OUID | [optional] 
**user_name** | **str** | Nickname | [optional] 
**descendant_id** | **str** | Equipped descendant identifier (Refer to /meta/descendant API) | [optional] 
**descendant_slot_id** | **str** | Descendant slot identifier | [optional] 
**descendant_level** | **float** | Equipped descendant level | [optional] 
**module_max_capacity** | **float** | Max. equippable module capacity | [optional] 
**module_capacity** | **float** | Equipped capacity | [optional] 
**energy_activator_use_count** | **float** | Energy activator usage count | [optional] 
**module** | [**List[UserDescendantModuleInner]**](UserDescendantModuleInner.md) | Module information | [optional] 
**customizing** | [**List[UserDescendantCustomizingInner]**](UserDescendantCustomizingInner.md) | Customization information | [optional] 

## Example

```python
from tfd_api_client.models.user_descendant import UserDescendant

# TODO update the JSON string below
json = "{}"
# create an instance of UserDescendant from a JSON string
user_descendant_instance = UserDescendant.from_json(json)
# print the JSON string representation of the object
print(UserDescendant.to_json())

# convert the object into a dict
user_descendant_dict = user_descendant_instance.to_dict()
# create an instance of UserDescendant from a dict
user_descendant_from_dict = UserDescendant.from_dict(user_descendant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


