# ModuleRecommendationsWeapon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weapon_id** | **str** | Weapon identifier (Refer to /meta/weapon API) | [optional] 
**recommendation** | [**List[ModuleRecommendationsDescendantRecommendationInner]**](ModuleRecommendationsDescendantRecommendationInner.md) | Weapon Recommendation information | [optional] 

## Example

```python
from tfd_api_client.models.module_recommendations_weapon import ModuleRecommendationsWeapon

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleRecommendationsWeapon from a JSON string
module_recommendations_weapon_instance = ModuleRecommendationsWeapon.from_json(json)
# print the JSON string representation of the object
print(ModuleRecommendationsWeapon.to_json())

# convert the object into a dict
module_recommendations_weapon_dict = module_recommendations_weapon_instance.to_dict()
# create an instance of ModuleRecommendationsWeapon from a dict
module_recommendations_weapon_from_dict = ModuleRecommendationsWeapon.from_dict(module_recommendations_weapon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


