# WeaponTypeResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weapon_type** | **str** | Weapon type | [optional] 
**weapon_type_name** | **str** | Weapon type name | [optional] 

## Example

```python
from tfd_api_client.models.weapon_type_response_inner import WeaponTypeResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponTypeResponseInner from a JSON string
weapon_type_response_inner_instance = WeaponTypeResponseInner.from_json(json)
# print the JSON string representation of the object
print(WeaponTypeResponseInner.to_json())

# convert the object into a dict
weapon_type_response_inner_dict = weapon_type_response_inner_instance.to_dict()
# create an instance of WeaponTypeResponseInner from a dict
weapon_type_response_inner_from_dict = WeaponTypeResponseInner.from_dict(weapon_type_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


