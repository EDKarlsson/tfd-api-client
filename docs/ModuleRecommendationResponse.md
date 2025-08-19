# ModuleRecommendationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant** | [**ModuleRecommendationResponseDescendant**](ModuleRecommendationResponseDescendant.md) |  | [optional] 
**weapon** | [**ModuleRecommendationResponseWeapon**](ModuleRecommendationResponseWeapon.md) |  | [optional] 

## Example

```python
from tfd_api_client.models.module_recommendation_response import ModuleRecommendationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleRecommendationResponse from a JSON string
module_recommendation_response_instance = ModuleRecommendationResponse.from_json(json)
# print the JSON string representation of the object
print(ModuleRecommendationResponse.to_json())

# convert the object into a dict
module_recommendation_response_dict = module_recommendation_response_instance.to_dict()
# create an instance of ModuleRecommendationResponse from a dict
module_recommendation_response_from_dict = ModuleRecommendationResponse.from_dict(module_recommendation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


