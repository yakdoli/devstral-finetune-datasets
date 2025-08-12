```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_640.jpeg
document_name: grid
page_number: 640
page_id: grid#page_640
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### ManualTotalSummaryTable Class

The `ManualTotalSummaryTable` class is a subclass of `GridTable` designed for manual total summary operations. Below is an example of its implementation in C#:

```csharp
public class ManualTotalSummaryTable : GridTable
{
    public ManualTotalSummaryTable(TableDescriptor tableDescriptor, Table parentRelationTable)
        : base((GridTableDescriptor)tableDescriptor, (GridTable)parentRelationTable)
    {
    }

    ArrayList totalSummaries = new ArrayList();
    public ArrayList TotalSummaries
    {
        get
        {
            return this.totalSummaries;
        }
        set
        {
            this.totalSummaries = value;
        }
    }

    protected override void OnRecordChanged(Element r, bool isObsoleteRecord, bool isAddedRecord)
    {
        TableDescriptor td = TableDescriptor;
        Group g = r.ParentGroup;
        while (g is IManualTotalSummaryArraySource)
        {
            OnGroupSummaryInvalidated(new GroupEventArgs(g));

            IManualTotalSummaryArraySource tsa = g as IManualTotalSummaryArraySource;
            foreach (ChangedFieldInfo ci in this.ChangedFieldsArray)
            {
                ManualTotalSummary mt =
                    tsa.GetManualTotalSummaryArray()[ci.FieldIndex];
                if (mt != null)
                    mt.ApplyDelta(r, isObsoleteRecord, isAddedRecord, ci);
            }
            g = g.ParentGroup;
        }
    }
}
```

## API Reference

### Class Definition

- **Namespace:** Not explicitly mentioned in the snippet, but it is likely `Syncfusion.Windows.Forms.Grid`.
- **Class:** `ManualTotalSummaryTable`
- **Inheritance:** Inherits from `GridTable`.

### Properties

- **TotalSummaries**
    - **Type:** `ArrayList`
    - **Description:** Maintains a list of summary calculations for the table.
    - **Access:** Public get/set.

### Methods

- **OnRecordChanged**
    - **Parameters:** 
        - `Element r` – The record element that has changed.
        - `bool isObsoleteRecord` – Indicates if the record is obsolete.
        - `bool isAddedRecord` – Indicates if the record has been added.
    - **Description:** Overrides the base method to handle record changes and apply updates to manual summary calculations.

### Interfaces Used

- **IManualTotalSummaryArraySource**
    - The parent group must implement this interface to provide access to the manual summary arrays.

## Code Examples

The provided code snippet demonstrates the implementation of the `ManualTotalSummaryTable` class, including its constructor, property for managing total summaries, and the overridden `OnRecordChanged` method to handle record changes.

### Key Methods Explained

1. **Constructor**:
    ```csharp
    public ManualTotalSummaryTable(TableDescriptor tableDescriptor, Table parentRelationTable)
        : base((GridTableDescriptor)tableDescriptor, (GridTable)parentRelationTable)
    {
    }
    ```
    - Initializes the `ManualTotalSummaryTable` with the given table descriptor and parent relation table.

2. **TotalSummaries Property**:
    ```csharp
    ArrayList totalSummaries = new ArrayList();
    public ArrayList TotalSummaries
    {
        get
        {
            return this.totalSummaries;
        }
        set
        {
            this.totalSummaries = value;
        }
    }
    ```
    - Provides access to the collection of total summaries.

3. **OnRecordChanged Method**:
    ```csharp
    protected override void OnRecordChanged(Element r, bool isObsoleteRecord, bool isAddedRecord)
    {
        // Implementation details as described in the snippet.
    }
    ```
    - Handles record changes and applies deltas to the manual summaries.

## See also

- Other sections in the user guide that detail the use of `GridTable` and related interfaces.
- Documentation for `TableDescriptor` and `GroupEventArgs` for more context.

## References

- Original Copyright: © 2013 Syncfusion. All rights reserved.
- Documentation Version: 11.4.0.26

<!-- tags: [syncfusion, winforms, grid, total summary, manual summary, api, version 11.4.0.26] keywords: [ManualTotalSummaryTable, GridTable, TotalSummaries, OnRecordChanged, IManualTotalSummaryArraySource, TableDescriptor, GroupEventArgs] -->
```