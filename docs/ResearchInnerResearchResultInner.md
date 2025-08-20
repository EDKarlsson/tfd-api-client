# ResearchInnerResearchResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_type** | **str** | Metadata type of the research result item | [optional] 
**meta_id** | **str** | Identifier of the research result item | [optional] 
**result_count** | **float** | Quantity of the research result item | [optional] 

## Example

```python
from tfd_api_client.models.research_inner_research_result_inner import ResearchInnerResearchResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResearchInnerResearchResultInner from a JSON string
research_inner_research_result_inner_instance = ResearchInnerResearchResultInner.from_json(json)
# print the JSON string representation of the object
print(ResearchInnerResearchResultInner.to_json())

# convert the object into a dict
research_inner_research_result_inner_dict = research_inner_research_result_inner_instance.to_dict()
# create an instance of ResearchInnerResearchResultInner from a dict
research_inner_research_result_inner_from_dict = ResearchInnerResearchResultInner.from_dict(research_inner_research_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


