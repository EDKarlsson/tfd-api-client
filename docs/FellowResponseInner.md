# FellowResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fellow_id** | **str** | Identifier for the fellow | [optional] 
**fellow_name** | **str** | Fellow name | [optional] 
**fellow_tier_id** | **str** | Fellow level (refer to /meta/tier API) | [optional] 
**fellow_detail** | [**List[FellowResponseInnerFellowDetailInner]**](FellowResponseInnerFellowDetailInner.md) | Details by fellow level | [optional] 

## Example

```python
from tfd_api_client.models.fellow_response_inner import FellowResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of FellowResponseInner from a JSON string
fellow_response_inner_instance = FellowResponseInner.from_json(json)
# print the JSON string representation of the object
print(FellowResponseInner.to_json())

# convert the object into a dict
fellow_response_inner_dict = fellow_response_inner_instance.to_dict()
# create an instance of FellowResponseInner from a dict
fellow_response_inner_from_dict = FellowResponseInner.from_dict(fellow_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


