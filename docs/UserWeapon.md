# UserWeapon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ouid** | **str** | OUID | [optional] 
**user_name** | **str** | Nickname | [optional] 
**weapon** | [**List[UserWeaponWeaponInner]**](UserWeaponWeaponInner.md) | Weapon information | [optional] 

## Example

```python
from tfd_api_client.models.user_weapon import UserWeapon

# TODO update the JSON string below
json = "{}"
# create an instance of UserWeapon from a JSON string
user_weapon_instance = UserWeapon.from_json(json)
# print the JSON string representation of the object
print(UserWeapon.to_json())

# convert the object into a dict
user_weapon_dict = user_weapon_instance.to_dict()
# create an instance of UserWeapon from a dict
user_weapon_from_dict = UserWeapon.from_dict(user_weapon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


