```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: Olap Common
page_number: 013
page_id: Olap Common#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:25Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes methods related to executing MDX queries, retrieving cube schemas, and managing member relationships in OLAP environments.
- Focuses on data retrieval and manipulation within multidimensional cubes.

## Content

### Table 2: Methods

| Method Name         | Description                                                                                                                                                                                                                     | Parameters                                                                                         | Return Type           | Reference Link |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------|----------------|
| ExecuteCellSet     | Four arguments should be given to invoke this method. The arguments are MDX query as string, drill down state of result set as bool, query append info as bool and finally get the OlapReport. This method will generate the CellSet for the given query or OlapReport. | MDx Query as string, drill down state as bool, Property append status as bool and Current OlapReort of OlapDataManager | CellSet               | -              |
| GetCubeSchema      | This method will get the cube name and intersect the cube to get all the information about the cube and return an object of type CubeSchema, which will contain all the information. CubeSchema is a class in Data namespace. | Cube Name as string                                                                                     | CubeSchema            | -              |
| GetChildMembers    | This method will get the member element and the expander state and return the child members of the given member as MemberCollection.                                                                                     | Parent member as Member and drill down state as bool                                                  | MemberCollection      | -              |
| GetLevelMembers    | This method will get the level element as argument and return the member elements of that level as MemberCollection.                                                                                                       | Level                                                                                               | MemberCollection      | -              |
| GetParentMember    | This method is used to find the parent member of a member element. By passing a member element as an argument, this element will return its parent.                                                                            | Member                                                                                                | Member                | -              |

## Code Examples

Here is an example of how the `ExecuteCellSet` method might be used in C#:

```csharp
using Syncfusion.Olap;

// Assuming OlapReport and OlapDataManager are initialized
string mdxQuery = "SELECT ..."; // Your MDX query
bool drillDownState = true;
bool queryAppendInfo = false;
bool propertyAppendStatus = false;
var cellSet = manager.ExecuteCellSet(mdxQuery, drillDownState, queryAppendInfo, propertyAppendStatus, olapReport);
```

## API Reference

### Methods

#### ExecuteCellSet
- **Parameters:**
  - **Mdx Query as string**: The MDX query to execute.
  - **Drill down state of result set as bool**: Whether to drill down the results.
  - **Query append info as bool**: Whether to append query information.
  - **Property append status as bool**: Whether to include property append status.
  - **Current OlapReort of OlapDataManager**: The current Olap report.
- **Return Type**: CellSet
- **Description**: Executes the given MDX query and returns a CellSet for the given query or OlapReport.

#### GetCubeSchema
- **Parameters**: Cube Name as string
- **Return Type**: CubeSchema
- **Description**: Retrieves the schema of the specified cube.

#### GetChildMembers
- **Parameters**:
  - **Parent member as Member**: The parent member to get child members from.
  - **Drill down state as bool**: Whether to drill down to get child members.
- **Return Type**: MemberCollection
- **Description**: Retrieves the child members of the given member.

#### GetLevelMembers
- **Parameters**: Level
- **Return Type**: MemberCollection
- **Description**: Retrieves the member elements of the specified level.

#### GetParentMember
- **Parameters**: Member
- **Return Type**: Member
- **Description**: Finds the parent member of the given member element.

## Cross References

- See also:
  - [CubeSchema Documentation](#cube-schema)
  - [OlapReport Documentation](#olap-report)

<!-- tags: [Olap, MDX, CubeSchema, Member, OlapReport, CellSet] keywords: [ExecuteCellSet, GetCubeSchema, GetChildMembers, GetLevelMembers, GetParentMember] -->
```