# ModuleRecommendations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant** | [**ModuleRecommendationsDescendant**](ModuleRecommendationsDescendant.md) |  | [optional] 
**weapon** | [**ModuleRecommendationsWeapon**](ModuleRecommendationsWeapon.md) |  | [optional] 

## Example

```python
from tfd_api_client.models.module_recommendations import ModuleRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleRecommendations from a JSON string
module_recommendations_instance = ModuleRecommendations.from_json(json)
# print the JSON string representation of the object
print(ModuleRecommendations.to_json())

# convert the object into a dict
module_recommendations_dict = module_recommendations_instance.to_dict()
# create an instance of ModuleRecommendations from a dict
module_recommendations_from_dict = ModuleRecommendations.from_dict(module_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


