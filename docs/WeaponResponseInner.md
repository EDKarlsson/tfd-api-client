# WeaponResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weapon_name** | **str** | Weapon name | [optional] 
**weapon_id** | **str** | Weapon identifier | [optional] 
**image_url** | **str** | Weapon image path | [optional] 
**weapon_type** | **str** | Weapon type | [optional] 
**weapon_tier_id** | **str** | Weapon tier (Refer to /meta/tier API) | [optional] 
**weapon_rounds_type** | **str** | Weapon rounds type | [optional] 
**available_core_slot** | **List[str]** | List of unlockable core slots (Refer to the /meta/core-slot API) | [optional] 
**base_stat** | [**List[WeaponResponseInnerBaseStatInner]**](WeaponResponseInnerBaseStatInner.md) | Weapon base spec information | [optional] 
**firearm_atk** | [**List[WeaponResponseInnerFirearmAtkInner]**](WeaponResponseInnerFirearmAtkInner.md) | Firearm attack power by level information | [optional] 
**weapon_perk_ability_name** | **str** | Unique Ability name | [optional] 
**weapon_perk_ability_description** | **str** | Unique Ability description | [optional] 
**weapon_perk_ability_image_url** | **str** | Unique Ability image path | [optional] 

## Example

```python
from tfd_api_client.models.weapon_response_inner import WeaponResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponResponseInner from a JSON string
weapon_response_inner_instance = WeaponResponseInner.from_json(json)
# print the JSON string representation of the object
print(WeaponResponseInner.to_json())

# convert the object into a dict
weapon_response_inner_dict = weapon_response_inner_instance.to_dict()
# create an instance of WeaponResponseInner from a dict
weapon_response_inner_from_dict = WeaponResponseInner.from_dict(weapon_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


