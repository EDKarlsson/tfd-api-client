# DescendantLevelDetailResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descendant_level** | **float** | Descendant level | [optional] 
**exp_per_level** | **float** | Required EXP for the next level | [optional] 

## Example

```python
from tfd_api_client.models.descendant_level_detail_response_inner import DescendantLevelDetailResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of DescendantLevelDetailResponseInner from a JSON string
descendant_level_detail_response_inner_instance = DescendantLevelDetailResponseInner.from_json(json)
# print the JSON string representation of the object
print(DescendantLevelDetailResponseInner.to_json())

# convert the object into a dict
descendant_level_detail_response_inner_dict = descendant_level_detail_response_inner_instance.to_dict()
# create an instance of DescendantLevelDetailResponseInner from a dict
descendant_level_detail_response_inner_from_dict = DescendantLevelDetailResponseInner.from_dict(descendant_level_detail_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


