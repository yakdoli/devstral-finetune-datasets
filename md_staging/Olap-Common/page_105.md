```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: Olap Common
page_number: 105
page_id: Olap Common#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:06Z
fidelity: lossless
-->

## Overview
- Describes the functionality of the "drill-down" button in the context of `OlapDataManager`.
- Explains the sequence of method calls when drill-down is triggered, focusing on recursion, member creation, and query generation.

## Content

### Overview of Drill-Down Functionality

Whenever the drill-down button is clicked, the `ToggleExpandableState()` method in the `OlapDataManager` will be invoked by the control. From there, the `UpdateDrillDowItems` will be called by passing the arguments, and there it checks the unique name and calls the `DrillUpDown()` method, which accepts the hierarchy element as an argument. This method is a recursive method and has an overload method that accepts the member element as an argument. By recursively iterating the drill-down level, all the members in that level will be created and added with its parent for the query creation.

Once the drill-down member is updated, the `NotifyElementModified()` will be invoked to generate the new query.

### Sequential Diagrams

#### Explanation of the Sequential Diagram for Drill-Down Process

The following screenshot explains the sequential diagram for the drill-down process:

![OLAP base sequential diagram](#)
**Figure 12: OLAP base sequential diagram**

The diagram illustrates the following steps in the drill-down process:

1. **User Trigger**: The user initiates a drill-up/down action.
2. **OlapDataManager Handling**: The `OlapDataManager` processes the drill-up/down request.
3. **Update Member**: The `Update DrillDown member` action updates the relevant member.
4. **Data Flow**: The data flows through `DataProvider`, `QuerySpecification`, `QueryBuilder`, `QueryBuilderHelper`, and `PivotEngine`.
5. **Recursive Drill-Down**: The `DrillUpDown` method is called recursively, handling `DrillDownHierarchy` and `DrillDownMember`.
6. **Query Execution**: The `GetQueryEx` method retrieves the query, which is then executed to generate the appropriate `CellSet`.
7. **Result Execution**: The `ExecuteOlapTable` ensures the query results are rendered correctly.

This diagram provides a comprehensive understanding of how the drill-down functionality is implemented and executed within the context of the `OlapDataManager` and related components.

## API Reference

### Methods

#### `ToggleExpandableState()`
- Invoked when the drill-down button is clicked.
- Triggers the `UpdateDrillDowItems` method.

#### `UpdateDrillDowItems`
- Accepts arguments and checks for unique names.
- Calls the `DrillUpDown()` method.

#### `DrillUpDown()`
- A recursive method that accepts a hierarchy element.
- Overloaded to accept a member element.
- Creates and adds members at the drill-down level and their parents for query creation.

#### `NotifyElementModified()`
- Called after updating the drill-down member to generate a new query.

## Code Examples

```csharp
// Example of handling drill-down in C#
public class OlapDataProcessor
{
    public void ToggleExpandableState()
    {
        // Implementation logic for toggling expandable state
        UpdateDrillDowItems();
    }

    public void UpdateDrillDowItems()
    {
        // Logic to update drill-down items
        DrillUpDown();
    }

    private void DrillUpDown()
    {
        // Recursive logic for drill-up/down
    }

    public void NotifyElementModified()
    {
        // Logic to generate new query after member update
    }
}
```

## Cross References

- See also: Other sections or reference materials relevant to the `OlapDataManager` and hierarchical queries.

<!-- tags: [OlapCommon, OlapDataProcessor, drill-down, recursion, query generation, WinForms] keywords: [toggleExpandableState, updateDrillDowItems, drillUpDown, notifyElementModified, sequential diagram, hierarchical queries] -->
```