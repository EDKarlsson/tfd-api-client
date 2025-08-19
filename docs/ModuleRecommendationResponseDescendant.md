# ModuleRecommendationResponseDescendant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant_id** | **str** | Descendant identifier (Refer to /meta/descendant API) | [optional] 
**recommendation** | [**List[ModuleRecommendationResponseDescendantRecommendationInner]**](ModuleRecommendationResponseDescendantRecommendationInner.md) | Descendant Recommendation information | [optional] 

## Example

```python
from tfd_api_client.models.module_recommendation_response_descendant import ModuleRecommendationResponseDescendant

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleRecommendationResponseDescendant from a JSON string
module_recommendation_response_descendant_instance = ModuleRecommendationResponseDescendant.from_json(json)
# print the JSON string representation of the object
print(ModuleRecommendationResponseDescendant.to_json())

# convert the object into a dict
module_recommendation_response_descendant_dict = module_recommendation_response_descendant_instance.to_dict()
# create an instance of ModuleRecommendationResponseDescendant from a dict
module_recommendation_response_descendant_from_dict = ModuleRecommendationResponseDescendant.from_dict(module_recommendation_response_descendant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


