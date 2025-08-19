# AdaptLevelResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | Level | [optional] 
**exp_per_level** | **float** | Required EXP for the next level | [optional] 

## Example

```python
from tfd_api_client.models.adapt_level_response_inner import AdaptLevelResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptLevelResponseInner from a JSON string
adapt_level_response_inner_instance = AdaptLevelResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdaptLevelResponseInner.to_json())

# convert the object into a dict
adapt_level_response_inner_dict = adapt_level_response_inner_instance.to_dict()
# create an instance of AdaptLevelResponseInner from a dict
adapt_level_response_inner_from_dict = AdaptLevelResponseInner.from_dict(adapt_level_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


