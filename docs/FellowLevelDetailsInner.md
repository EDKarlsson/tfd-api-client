# FellowLevelDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fellow_level** | **float** | Fellow level | [optional] 
**exp_per_level** | **float** | Required EXP for the next level | [optional] 

## Example

```python
from tfd_api_client.models.fellow_level_details_inner import FellowLevelDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FellowLevelDetailsInner from a JSON string
fellow_level_details_inner_instance = FellowLevelDetailsInner.from_json(json)
# print the JSON string representation of the object
print(FellowLevelDetailsInner.to_json())

# convert the object into a dict
fellow_level_details_inner_dict = fellow_level_details_inner_instance.to_dict()
# create an instance of FellowLevelDetailsInner from a dict
fellow_level_details_inner_from_dict = FellowLevelDetailsInner.from_dict(fellow_level_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


