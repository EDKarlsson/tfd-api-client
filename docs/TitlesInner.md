# TitlesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title_id** | **str** | Title identifier | [optional] 
**title_name** | **str** | Title name | [optional] 

## Example

```python
from tfd_api_client.models.titles_inner import TitlesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TitlesInner from a JSON string
titles_inner_instance = TitlesInner.from_json(json)
# print the JSON string representation of the object
print(TitlesInner.to_json())

# convert the object into a dict
titles_inner_dict = titles_inner_instance.to_dict()
# create an instance of TitlesInner from a dict
titles_inner_from_dict = TitlesInner.from_dict(titles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


