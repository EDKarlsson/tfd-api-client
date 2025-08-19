# WeaponResponseInnerFirearmAtkInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Firearm level | [optional] 
**firearm** | [**List[WeaponResponseInnerFirearmAtkInnerFirearmInner]**](WeaponResponseInnerFirearmAtkInnerFirearmInner.md) | Firearm ATK | [optional] 

## Example

```python
from tfd_api_client.models.weapon_response_inner_firearm_atk_inner import WeaponResponseInnerFirearmAtkInner

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponResponseInnerFirearmAtkInner from a JSON string
weapon_response_inner_firearm_atk_inner_instance = WeaponResponseInnerFirearmAtkInner.from_json(json)
# print the JSON string representation of the object
print(WeaponResponseInnerFirearmAtkInner.to_json())

# convert the object into a dict
weapon_response_inner_firearm_atk_inner_dict = weapon_response_inner_firearm_atk_inner_instance.to_dict()
# create an instance of WeaponResponseInnerFirearmAtkInner from a dict
weapon_response_inner_firearm_atk_inner_from_dict = WeaponResponseInnerFirearmAtkInner.from_dict(weapon_response_inner_firearm_atk_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


