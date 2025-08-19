# StatResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stat_id** | **str** | Base stat identifier | [optional] 
**stat_name** | **str** | Base stat name | [optional] 
**stat_order_no** | **float** | Base stat sort order (ascending) | [optional] 

## Example

```python
from tfd_api_client.models.stat_response_inner import StatResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatResponseInner from a JSON string
stat_response_inner_instance = StatResponseInner.from_json(json)
# print the JSON string representation of the object
print(StatResponseInner.to_json())

# convert the object into a dict
stat_response_inner_dict = stat_response_inner_instance.to_dict()
# create an instance of StatResponseInner from a dict
stat_response_inner_from_dict = StatResponseInner.from_dict(stat_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


