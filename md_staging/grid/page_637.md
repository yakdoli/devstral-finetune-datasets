```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_637.jpeg
document_name: grid
page_number: 637
page_id: grid#page_637
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:58Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

```csharp
{
    object obj = r.GetValue(field);
    if (obj != null && !(obj is DBNull))
    {
        double d = Convert.ToDouble(obj);
        total += d;
    }
}
else
{
    foreach (Group g in group.Groups)
    {
        IManualTotalSummaryArraySource tsa = g as IManualTotalSummaryArraySource;
        ManualTotalSummary mt = tsa.GetManualTotalSummaryArray()[this.FieldIndex];
        if (mt == null)
            mt = new ManualTotalSummary(g, field);
        double d = mt.Total;
        total += d;
    }
}
}

public void ApplyDelta(Element r, bool isObsoleteRecord, bool isAddedRecord, ChangedFieldInfo ci)
{
    if (Dirty)
        return;

    ManualTotalSummary mt = this;

    if (isObsoleteRecord)
    {
        if (ci.OldValue != null && !(ci.OldValue is DBNull))
            mt.Total -= Convert.ToDouble(ci.OldValue);
    }
    else if (isAddedRecord)
    {
        if (ci.NewValue != null && !(ci.NewValue is DBNull))
            mt.Total += Convert.ToDouble(ci.NewValue);
    }
    else
        mt.Total += ci.Delta;
}
```

### Overview
- Overview of the code snippet demonstrating how to calculate totals for a grid in a Windows Forms application using Essential Grid.
- Explanation of how the `ApplyDelta` method handles updates to the total summary based on record changes.
- Code example showing the use of `ManualTotalSummary` to manage manual summarization of grid data.

### Content
The provided code snippet illustrates how to perform manual summarization of grid data in a Windows Forms application using Syncfusion's Essential Grid control. 

- **Main Logic**:
  - The first part of the code calculates the total for a field in a record (`r`) by checking if the value is not null or `DBNull`.
  - It then converts the value to a double and adds it to a running total.
  - If the record is part of a group, it iterates through each group to calculate the total summary, handling cases where the summary might not exist and creating it if necessary.

- **ApplyDelta Method**:
  - This method is responsible for updating the summary total based on changes to records.
  - It checks whether a record is obsolete, newly added, or modified, and adjusts the total accordingly using the `ChangedFieldInfo` object (`ci`).
  - The method ensures that only valid (non-null and non-`DBNull`) values are processed to avoid runtime errors.

### WinForms-specific conventions
- **Namespace and Class**: The code is likely part of a larger class that implements summarization logic for the grid control.
- **Properties and Methods**:
  - `GetValue`: A method that retrieves the value of a specific field from a record.
  - `Total`: A property that tracks the running total for the summary.
  - `Dirty`: A flag indicating whether the summary has been modified but not yet committed.
- **Event Handling**: The `ApplyDelta` method is likely called in response to data changes in the grid, ensuring that the summary remains accurate.

### API Reference
- **Namespace**: Likely part of `Syncfusion.Windows.Forms.Grid`, or similar.
- **Class**: Likely a custom class for handling grid summarization.
- **Properties**:
  - `Dirty`: A boolean indicating whether the summary has changes that need to be applied.
  - `Total`: A double representing the accumulated total for the summary.
- **Methods**:
  - `ApplyDelta`: Updates the summary total based on record changes.
  - `GetManualTotalSummaryArray`: Retrieves an array of manual summaries for a group.

### Code Examples
The provided code snippet demonstrates how to implement manual summarization in a grid. It includes handling of null and `DBNull` values, as well as logic for updating the summary based on record changes.

### RAG Annotations
<!-- tags: [grid, windows-forms, summarization, essential-grid, syncfusion] keywords: [ManualTotalSummary, ChangedFieldInfo, ApplyDelta, IManualTotalSummaryArraySource, Grid, record, total, double] -->
```