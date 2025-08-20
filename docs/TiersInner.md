# TiersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **str** | Tier identifier | [optional] 
**tier_name** | **str** | Tier name | [optional] 

## Example

```python
from tfd_api_client.models.tiers_inner import TiersInner

# TODO update the JSON string below
json = "{}"
# create an instance of TiersInner from a JSON string
tiers_inner_instance = TiersInner.from_json(json)
# print the JSON string representation of the object
print(TiersInner.to_json())

# convert the object into a dict
tiers_inner_dict = tiers_inner_instance.to_dict()
# create an instance of TiersInner from a dict
tiers_inner_from_dict = TiersInner.from_dict(tiers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


