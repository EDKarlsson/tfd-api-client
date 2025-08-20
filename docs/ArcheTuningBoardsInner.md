# ArcheTuningBoardsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arche_tuning_board_id** | **str** | Arche board identifier | [optional] 
**row_size** | **float** | Row size | [optional] 
**column_size** | **float** | Column size | [optional] 
**node** | [**List[ArcheTuningBoardsInnerNodeInner]**](ArcheTuningBoardsInnerNodeInner.md) |  | [optional] 

## Example

```python
from tfd_api_client.models.arche_tuning_boards_inner import ArcheTuningBoardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArcheTuningBoardsInner from a JSON string
arche_tuning_boards_inner_instance = ArcheTuningBoardsInner.from_json(json)
# print the JSON string representation of the object
print(ArcheTuningBoardsInner.to_json())

# convert the object into a dict
arche_tuning_boards_inner_dict = arche_tuning_boards_inner_instance.to_dict()
# create an instance of ArcheTuningBoardsInner from a dict
arche_tuning_boards_inner_from_dict = ArcheTuningBoardsInner.from_dict(arche_tuning_boards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


