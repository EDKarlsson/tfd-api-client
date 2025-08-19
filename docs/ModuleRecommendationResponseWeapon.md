# ModuleRecommendationResponseWeapon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weapon_id** | **str** | Weapon identifier (Refer to /meta/weapon API) | [optional] 
**recommendation** | [**List[ModuleRecommendationResponseDescendantRecommendationInner]**](ModuleRecommendationResponseDescendantRecommendationInner.md) | Weapon Recommendation information | [optional] 

## Example

```python
from tfd_api_client.models.module_recommendation_response_weapon import ModuleRecommendationResponseWeapon

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleRecommendationResponseWeapon from a JSON string
module_recommendation_response_weapon_instance = ModuleRecommendationResponseWeapon.from_json(json)
# print the JSON string representation of the object
print(ModuleRecommendationResponseWeapon.to_json())

# convert the object into a dict
module_recommendation_response_weapon_dict = module_recommendation_response_weapon_instance.to_dict()
# create an instance of ModuleRecommendationResponseWeapon from a dict
module_recommendation_response_weapon_from_dict = ModuleRecommendationResponseWeapon.from_dict(module_recommendation_response_weapon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


