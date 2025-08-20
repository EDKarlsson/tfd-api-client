# ResearchInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**research_id** | **str** | Research identifier | [optional] 
**research_name** | **str** | Research name | [optional] 
**repeatable_research** | **bool** | Repeatable | [optional] 
**research_type** | **str** | Research type | [optional] 
**research_time** | **float** | Research time (seconds) | [optional] 
**research_cost** | [**List[ResearchInnerResearchCostInner]**](ResearchInnerResearchCostInner.md) | Research cost | [optional] 
**research_boost_cost** | [**List[ResearchInnerResearchCostInner]**](ResearchInnerResearchCostInner.md) | Boost Research Cost | [optional] 
**research_result** | [**List[ResearchInnerResearchResultInner]**](ResearchInnerResearchResultInner.md) | Research result | [optional] 
**research_material** | [**List[ResearchInnerResearchMaterialInner]**](ResearchInnerResearchMaterialInner.md) | Research materials | [optional] 

## Example

```python
from tfd_api_client.models.research_inner import ResearchInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResearchInner from a JSON string
research_inner_instance = ResearchInner.from_json(json)
# print the JSON string representation of the object
print(ResearchInner.to_json())

# convert the object into a dict
research_inner_dict = research_inner_instance.to_dict()
# create an instance of ResearchInner from a dict
research_inner_from_dict = ResearchInner.from_dict(research_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


