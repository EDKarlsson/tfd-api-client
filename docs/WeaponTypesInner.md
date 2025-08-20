# WeaponTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weapon_type** | **str** | Weapon type | [optional] 
**weapon_type_name** | **str** | Weapon type name | [optional] 

## Example

```python
from tfd_api_client.models.weapon_types_inner import WeaponTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponTypesInner from a JSON string
weapon_types_inner_instance = WeaponTypesInner.from_json(json)
# print the JSON string representation of the object
print(WeaponTypesInner.to_json())

# convert the object into a dict
weapon_types_inner_dict = weapon_types_inner_instance.to_dict()
# create an instance of WeaponTypesInner from a dict
weapon_types_inner_from_dict = WeaponTypesInner.from_dict(weapon_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


