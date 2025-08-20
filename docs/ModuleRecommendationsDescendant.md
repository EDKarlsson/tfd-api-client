# ModuleRecommendationsDescendant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant_id** | **str** | Descendant identifier (Refer to /meta/descendant API) | [optional] 
**recommendation** | [**List[ModuleRecommendationsDescendantRecommendationInner]**](ModuleRecommendationsDescendantRecommendationInner.md) | Descendant Recommendation information | [optional] 

## Example

```python
from tfd_api_client.models.module_recommendations_descendant import ModuleRecommendationsDescendant

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleRecommendationsDescendant from a JSON string
module_recommendations_descendant_instance = ModuleRecommendationsDescendant.from_json(json)
# print the JSON string representation of the object
print(ModuleRecommendationsDescendant.to_json())

# convert the object into a dict
module_recommendations_descendant_dict = module_recommendations_descendant_instance.to_dict()
# create an instance of ModuleRecommendationsDescendant from a dict
module_recommendations_descendant_from_dict = ModuleRecommendationsDescendant.from_dict(module_recommendations_descendant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


