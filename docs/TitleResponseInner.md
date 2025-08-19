# TitleResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title_id** | **str** | Title identifier | [optional] 
**title_name** | **str** | Title name | [optional] 

## Example

```python
from tfd_api_client.models.title_response_inner import TitleResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of TitleResponseInner from a JSON string
title_response_inner_instance = TitleResponseInner.from_json(json)
# print the JSON string representation of the object
print(TitleResponseInner.to_json())

# convert the object into a dict
title_response_inner_dict = title_response_inner_instance.to_dict()
# create an instance of TitleResponseInner from a dict
title_response_inner_from_dict = TitleResponseInner.from_dict(title_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


