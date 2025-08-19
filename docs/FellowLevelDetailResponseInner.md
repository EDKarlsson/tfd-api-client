# FellowLevelDetailResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fellow_level** | **float** | Fellow level | [optional] 
**exp_per_level** | **float** | Required EXP for the next level | [optional] 

## Example

```python
from tfd_api_client.models.fellow_level_detail_response_inner import FellowLevelDetailResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of FellowLevelDetailResponseInner from a JSON string
fellow_level_detail_response_inner_instance = FellowLevelDetailResponseInner.from_json(json)
# print the JSON string representation of the object
print(FellowLevelDetailResponseInner.to_json())

# convert the object into a dict
fellow_level_detail_response_inner_dict = fellow_level_detail_response_inner_instance.to_dict()
# create an instance of FellowLevelDetailResponseInner from a dict
fellow_level_detail_response_inner_from_dict = FellowLevelDetailResponseInner.from_dict(fellow_level_detail_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


