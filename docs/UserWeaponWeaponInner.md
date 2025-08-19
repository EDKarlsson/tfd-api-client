# UserWeaponWeaponInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_max_capacity** | **float** | Max. equippable module capacity | [optional] 
**module_capacity** | **float** | Equipped capacity | [optional] 
**energy_activator_use_count** | **float** | Energy activator usage count | [optional] 
**weapon_slot_id** | **str** | Weapon slot identifier | [optional] 
**weapon_id** | **str** | Weapon identifier (Refer to /meta/weapon API) | [optional] 
**weapon_level** | **float** | Weapon level | [optional] 
**perk_ability_enchant_level** | **float** | Weapon Unique Ability enchantment level | [optional] 
**weapon_additional_stat** | [**List[UserWeaponWeaponInnerWeaponAdditionalStatInner]**](UserWeaponWeaponInnerWeaponAdditionalStatInner.md) | Weapon random option information | [optional] 
**module** | [**List[UserDescendantModuleInner]**](UserDescendantModuleInner.md) | Module information | [optional] 
**core_unlock_flag** | **str** | Core unlock status (0:Locked | 1:Unlocked) | [optional] 
**core** | [**List[UserWeaponWeaponInnerCoreInner]**](UserWeaponWeaponInnerCoreInner.md) | Core option information | [optional] 

## Example

```python
from tfd_api_client.models.user_weapon_weapon_inner import UserWeaponWeaponInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserWeaponWeaponInner from a JSON string
user_weapon_weapon_inner_instance = UserWeaponWeaponInner.from_json(json)
# print the JSON string representation of the object
print(UserWeaponWeaponInner.to_json())

# convert the object into a dict
user_weapon_weapon_inner_dict = user_weapon_weapon_inner_instance.to_dict()
# create an instance of UserWeaponWeaponInner from a dict
user_weapon_weapon_inner_from_dict = UserWeaponWeaponInner.from_dict(user_weapon_weapon_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


