# UserArcheTuning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ouid** | **str** | Account identifier | [optional] 
**descendant_group_id** | **str** | Descendant group identifier (Refer to /meta/descendant-group API) | [optional] 
**arche_tuning_board_group_id** | **str** | Arche tuning board group identifier (Refer to /meta/arche-tuning-board-group API) | [optional] 
**arche_tuning** | [**List[UserArcheTuningArcheTuningInner]**](UserArcheTuningArcheTuningInner.md) | Arche tuning list | [optional] 

## Example

```python
from tfd_api_client.models.user_arche_tuning import UserArcheTuning

# TODO update the JSON string below
json = "{}"
# create an instance of UserArcheTuning from a JSON string
user_arche_tuning_instance = UserArcheTuning.from_json(json)
# print the JSON string representation of the object
print(UserArcheTuning.to_json())

# convert the object into a dict
user_arche_tuning_dict = user_arche_tuning_instance.to_dict()
# create an instance of UserArcheTuning from a dict
user_arche_tuning_from_dict = UserArcheTuning.from_dict(user_arche_tuning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


