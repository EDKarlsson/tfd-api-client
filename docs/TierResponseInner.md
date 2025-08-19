# TierResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **str** | Tier identifier | [optional] 
**tier_name** | **str** | Tier name | [optional] 

## Example

```python
from tfd_api_client.models.tier_response_inner import TierResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of TierResponseInner from a JSON string
tier_response_inner_instance = TierResponseInner.from_json(json)
# print the JSON string representation of the object
print(TierResponseInner.to_json())

# convert the object into a dict
tier_response_inner_dict = tier_response_inner_instance.to_dict()
# create an instance of TierResponseInner from a dict
tier_response_inner_from_dict = TierResponseInner.from_dict(tier_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


