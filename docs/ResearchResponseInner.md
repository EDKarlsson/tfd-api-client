# ResearchResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**research_id** | **str** | Research identifier | [optional] 
**research_name** | **str** | Research name | [optional] 
**repeatable_research** | **bool** | Repeatable | [optional] 
**research_type** | **str** | Research type | [optional] 
**research_time** | **float** | Research time (seconds) | [optional] 
**research_cost** | [**List[ResearchResponseInnerResearchCostInner]**](ResearchResponseInnerResearchCostInner.md) | Research cost | [optional] 
**research_boost_cost** | [**List[ResearchResponseInnerResearchCostInner]**](ResearchResponseInnerResearchCostInner.md) | Boost Research Cost | [optional] 
**research_result** | [**List[ResearchResponseInnerResearchResultInner]**](ResearchResponseInnerResearchResultInner.md) | Research result | [optional] 
**research_material** | [**List[ResearchResponseInnerResearchMaterialInner]**](ResearchResponseInnerResearchMaterialInner.md) | Research materials | [optional] 

## Example

```python
from tfd_api_client.models.research_response_inner import ResearchResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResearchResponseInner from a JSON string
research_response_inner_instance = ResearchResponseInner.from_json(json)
# print the JSON string representation of the object
print(ResearchResponseInner.to_json())

# convert the object into a dict
research_response_inner_dict = research_response_inner_instance.to_dict()
# create an instance of ResearchResponseInner from a dict
research_response_inner_from_dict = ResearchResponseInner.from_dict(research_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


