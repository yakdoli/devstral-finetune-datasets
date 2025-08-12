```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_636.jpeg
document_name: grid
page_number: 636
page_id: grid#page_636
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Implementation of a custom summary class for calculating totals in a grouped grid view.
- Provides functionality to manually calculate and store summary totals for specific fields.
- Includes methods to mark the summary as "dirty" and recalculate totals when data changes.

## Content

### ManualTotalSummary Class
The `ManualTotalSummary` class is designed to manage summary calculations for grouped data in a grid. It is particularly useful for maintaining manual summary totals when direct summation methods are not applicable or desired.

#### Class Definition
The class is defined as follows:

```csharp
public class ManualTotalSummary
{
    double total;
    bool dirty = true;
    Group group;
    int fieldIndex = -1;

    public ManualTotalSummary(Group g, string field)
        : this(g, g.ParentTableDescriptor.Fields[field])
    {
    }

    public ManualTotalSummary(Group g, FieldDescriptor field)
    {
        this.Field = field;
        this.Group = g;
    }

    public double Total
    {
        get
        {
            if (dirty)
            {
                CalculateTotal();
                this.dirty = false;
            }
            return this.total;
        }
        set
        {
            this.total = value;
        }
    }

    void CalculateTotal()
    {
        total = 0;
        if (group.Details is RecordsDetails)
        {
            foreach (Record r in group.Records)
```

### Key Features
- **Fields**:
  - `total`: Holds the current summary total.
  - `dirty`: A flag indicating whether the summary total needs recalculation.
  - `group`: Reference to the group for which the summary is calculated.
  - `fieldIndex`: Index of the field used for summation.

- **Constructors**:
  - `ManualTotalSummary(Group g, string field)`: Initializes the summary using a string field name.
  - `ManualTotalSummary(Group g, FieldDescriptor field)`: Initializes the summary using a `FieldDescriptor`.

- **Properties**:
  - `Total`: Property for accessing or setting the summary total. It recalculates the total if marked as "dirty".

- **Methods**:
  - `CalculateTotal()`: Method to manually calculate the summary total for the group.

### Usage
The class is used to manually manage summary totals for specific fields within grouped data. The `Total` property ensures that the summary is recalculated only when necessary, improving performance by avoiding redundant calculations.

#### Example Usage
```csharp
// Initialize the summary for a specific group and field
var summary = new ManualTotalSummary(group, "Amount");

// Access the total, triggering recalculation if necessary
double total = summary.Total;

// Mark the summary as dirty to force recalculation
summary.MarkAsDirty();
```

### Implementation Details
- **Recalculation Logic**: The `CalculateTotal` method iterates through the records in the group to compute the total for the specified field.
- **Dirty Flag**: The `dirty` flag ensures that recalculations are triggered only when necessary, optimizing performance.

## API Reference

### Class: ManualTotalSummary
#### Properties
- **Total**
  - **Type**: `double`
  - **Description**: Getter and setter for the summary total. The getter recalculates the total if the summary is marked as "dirty".

#### Methods
- **CalculateTotal**
  - **Description**: Calculates the total for the group by iterating through the records and summing the specified field values.

## Code Examples

### Example 1: Creating and Using a Summary
```csharp
using Syncfusion.Windows.Forms.Grid;

// Assuming 'grid' is an instance of GridControl with data and grouping applied
Group group = grid.EmbeddedMaintable.Root.TableGroups.FirstOrDefault();
if (group != null)
{
    // Create a manual summary for the "Amount" field
    var summary = new ManualTotalSummary(group, "Amount");

    // Access the total
    double totalAmount = summary.Total;

    // Optionally, force recalculation
    summary.MarkAsDirty();
    totalAmount = summary.Total;
}
```

### Example 2: Handling Data Changes
```csharp
// Event handler for record changes
private void grid_RecordChanged(object sender, GridTableNotifyEventArgs e)
{
    if (e.Action == GridRecordAction.Insert || e.Action == GridRecordAction.Update)
    {
        // Mark all summaries as dirty to recalculate totals
        foreach (var summary in summaries)
        {
            summary.MarkAsDirty();
        }
    }
}
```

## Cross References
- **Related Concepts**: Grouping, Summaries, Grid Control
- **API Documentation**: GridControl, Group, FieldDescriptor, RecordsDetails, Record

<!-- tags: [Syncfusion Winforms, Grid, Summaries, Grouping, ManualTotalSummary] keywords: [ManualTotalSummary, Grouping, Summaries, GridControl, RecordsDetails, Records, Total, CalculateTotal, dirty flag, C#] -->
```