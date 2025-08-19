# MasteryRankLevelDetailResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mastery_rank_level** | **float** | Mastery Rank | [optional] 
**exp_per_level** | **float** | Required EXP for the next level | [optional] 

## Example

```python
from tfd_api_client.models.mastery_rank_level_detail_response_inner import MasteryRankLevelDetailResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of MasteryRankLevelDetailResponseInner from a JSON string
mastery_rank_level_detail_response_inner_instance = MasteryRankLevelDetailResponseInner.from_json(json)
# print the JSON string representation of the object
print(MasteryRankLevelDetailResponseInner.to_json())

# convert the object into a dict
mastery_rank_level_detail_response_inner_dict = mastery_rank_level_detail_response_inner_instance.to_dict()
# create an instance of MasteryRankLevelDetailResponseInner from a dict
mastery_rank_level_detail_response_inner_from_dict = MasteryRankLevelDetailResponseInner.from_dict(mastery_rank_level_detail_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


