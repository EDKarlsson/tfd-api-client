# MedalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medal_id** | **str** | Medal identifier | [optional] 
**medal_detail** | [**List[MedalsInnerMedalDetailInner]**](MedalsInnerMedalDetailInner.md) | Description by medal grade | [optional] 

## Example

```python
from tfd_api_client.models.medals_inner import MedalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedalsInner from a JSON string
medals_inner_instance = MedalsInner.from_json(json)
# print the JSON string representation of the object
print(MedalsInner.to_json())

# convert the object into a dict
medals_inner_dict = medals_inner_instance.to_dict()
# create an instance of MedalsInner from a dict
medals_inner_from_dict = MedalsInner.from_dict(medals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


