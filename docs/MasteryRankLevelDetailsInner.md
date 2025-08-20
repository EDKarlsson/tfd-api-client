# MasteryRankLevelDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mastery_rank_level** | **float** | Mastery Rank | [optional] 
**exp_per_level** | **float** | Required EXP for the next level | [optional] 

## Example

```python
from tfd_api_client.models.mastery_rank_level_details_inner import MasteryRankLevelDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MasteryRankLevelDetailsInner from a JSON string
mastery_rank_level_details_inner_instance = MasteryRankLevelDetailsInner.from_json(json)
# print the JSON string representation of the object
print(MasteryRankLevelDetailsInner.to_json())

# convert the object into a dict
mastery_rank_level_details_inner_dict = mastery_rank_level_details_inner_instance.to_dict()
# create an instance of MasteryRankLevelDetailsInner from a dict
mastery_rank_level_details_inner_from_dict = MasteryRankLevelDetailsInner.from_dict(mastery_rank_level_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


