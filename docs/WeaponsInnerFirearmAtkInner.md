# WeaponsInnerFirearmAtkInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Firearm level | [optional] 
**firearm** | [**List[WeaponsInnerFirearmAtkInnerFirearmInner]**](WeaponsInnerFirearmAtkInnerFirearmInner.md) | Firearm ATK | [optional] 

## Example

```python
from tfd_api_client.models.weapons_inner_firearm_atk_inner import WeaponsInnerFirearmAtkInner

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponsInnerFirearmAtkInner from a JSON string
weapons_inner_firearm_atk_inner_instance = WeaponsInnerFirearmAtkInner.from_json(json)
# print the JSON string representation of the object
print(WeaponsInnerFirearmAtkInner.to_json())

# convert the object into a dict
weapons_inner_firearm_atk_inner_dict = weapons_inner_firearm_atk_inner_instance.to_dict()
# create an instance of WeaponsInnerFirearmAtkInner from a dict
weapons_inner_firearm_atk_inner_from_dict = WeaponsInnerFirearmAtkInner.from_dict(weapons_inner_firearm_atk_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


