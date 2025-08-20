# FellowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fellow_id** | **str** | Identifier for the fellow | [optional] 
**fellow_name** | **str** | Fellow name | [optional] 
**fellow_tier_id** | **str** | Fellow level (refer to /meta/tier API) | [optional] 
**fellow_detail** | [**List[FellowsInnerFellowDetailInner]**](FellowsInnerFellowDetailInner.md) | Details by fellow level | [optional] 

## Example

```python
from tfd_api_client.models.fellows_inner import FellowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FellowsInner from a JSON string
fellows_inner_instance = FellowsInner.from_json(json)
# print the JSON string representation of the object
print(FellowsInner.to_json())

# convert the object into a dict
fellows_inner_dict = fellows_inner_instance.to_dict()
# create an instance of FellowsInner from a dict
fellows_inner_from_dict = FellowsInner.from_dict(fellows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


