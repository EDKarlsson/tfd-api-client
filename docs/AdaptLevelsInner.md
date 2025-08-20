# AdaptLevelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Level | [optional] 
**exp_per_level** | **float** | Required EXP for the next level | [optional] 

## Example

```python
from tfd_api_client.models.adapt_levels_inner import AdaptLevelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptLevelsInner from a JSON string
adapt_levels_inner_instance = AdaptLevelsInner.from_json(json)
# print the JSON string representation of the object
print(AdaptLevelsInner.to_json())

# convert the object into a dict
adapt_levels_inner_dict = adapt_levels_inner_instance.to_dict()
# create an instance of AdaptLevelsInner from a dict
adapt_levels_inner_from_dict = AdaptLevelsInner.from_dict(adapt_levels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


