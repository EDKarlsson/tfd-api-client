# WeaponsInnerBaseStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_id** | **str** | Weapon base spec identifier (Refer to /meta/stat API) | [optional] 
**stat_value** | **float** | Weapon base spec value | [optional] 

## Example

```python
from tfd_api_client.models.weapons_inner_base_stat_inner import WeaponsInnerBaseStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponsInnerBaseStatInner from a JSON string
weapons_inner_base_stat_inner_instance = WeaponsInnerBaseStatInner.from_json(json)
# print the JSON string representation of the object
print(WeaponsInnerBaseStatInner.to_json())

# convert the object into a dict
weapons_inner_base_stat_inner_dict = weapons_inner_base_stat_inner_instance.to_dict()
# create an instance of WeaponsInnerBaseStatInner from a dict
weapons_inner_base_stat_inner_from_dict = WeaponsInnerBaseStatInner.from_dict(weapons_inner_base_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


