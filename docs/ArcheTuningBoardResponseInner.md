# ArcheTuningBoardResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arche_tuning_board_id** | **str** | Arche board identifier | [optional] 
**row_size** | **float** | Row size | [optional] 
**column_size** | **float** | Column size | [optional] 
**node** | [**List[ArcheTuningBoardResponseInnerNodeInner]**](ArcheTuningBoardResponseInnerNodeInner.md) |  | [optional] 

## Example

```python
from tfd_api_client.models.arche_tuning_board_response_inner import ArcheTuningBoardResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArcheTuningBoardResponseInner from a JSON string
arche_tuning_board_response_inner_instance = ArcheTuningBoardResponseInner.from_json(json)
# print the JSON string representation of the object
print(ArcheTuningBoardResponseInner.to_json())

# convert the object into a dict
arche_tuning_board_response_inner_dict = arche_tuning_board_response_inner_instance.to_dict()
# create an instance of ArcheTuningBoardResponseInner from a dict
arche_tuning_board_response_inner_from_dict = ArcheTuningBoardResponseInner.from_dict(arche_tuning_board_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


