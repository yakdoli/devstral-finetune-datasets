```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_931.jpeg
document_name: grid
page_number: 931
page_id: grid#page_931
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:27Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Provides detailed information on focused selection modes and multiple record selection in Grid controls.
- Demonstrates how to configure selection modes in the Grid Table, with examples including "Focused Selection" and "Multiple Record Selection."
- Explains the use of the `SelectedRecords` collection for managing and iterating through selected records in the Grid Table.

## Content

### Focused Selection Demonstration

#### Selection Modes
The Grid Table supports various selection modes:

- **Default**: Standard selection behavior.
- **Row Only**: Selects only the rows.
- **Row and Column**: Highlights both rows and columns of the selection.
- **Cell Only**: Selects individual cells.
- **Column Only**: Selects entire columns.
- **None**: No selection mode is active.

#### Table Example
The figure illustrates a Grid Table with selection mode set to "Row and Column," focusing on the row with `ID = 5`.

| ID | losses | School         | Sport      | ties | wins |
|----|--------|----------------|------------|------|------|
| 1  | 7      | Duke           | Basketball | 0    | 26   |
| 2  | 10     | Maryland       | Basketball | 0    | 21   |
| 3  | 6      | Wake Forest    | Basketball | 0    | 25   |
| 4  | 15     | Georgia Tech   | Basketball | 0    | 16   |
| **5** | **16** | **Virginia** | **Basketball** | **0** | **16** |
| 6  | 13     | NC State       | Basketball | 0    | 18   |
| 7  | 16     | North Carolina | Basketball | 0    | 19   |
| 8  | 13     | Clemson        | Basketball | 0    | 15   |
| 9  | 15     | Florida State  | Basketball | 0    | 14   |
| 10 | 7      | Duke           | Football   | 0    | 3    |
| 11 | 3      | Maryland       | Football   | 0    | 6    |

---

**Figure 344: Focused Selection Illustrated**

---

**Note:** For more details, refer to the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Selection\Focused Selection Demo
```

---

### Multiple Record Selection

#### Overview
- The Grid Table supports the selection of multiple records.
- Each selected record is added to the `SelectedRecords` collection, which manages the selected records.
- Iteration through the `SelectedRecords` collection allows stepping through all marked records.
- The grid raises the `SelectedRecordsChanging` and `SelectedRecordsChanged` events when records are added or removed from the collection.

#### Selecting Multiple Records
This section demonstrates how to work with the `SelectedRecords` collection.

## API Reference

### SelectedRecords
- **Namespace**: `Syncfusion.Windows.Forms.Grid`
- **Class**: `GridGroupingControl`
- **Property**: `SelectedRecords`

#### Parameters
- **Type**: `List<RowDescriptor>`

#### Methods
1. `SelectedRecordsChanged`  
   - **Event**: Raised after the selected records have been changed.
2. `SelectedRecordsChanging`  
   - **Event**: Raised before the selected records are changed.

## Code Examples

### C# Example: Handling Multiple Record Selection

```csharp
// Subscribe to the SelectedRecordsChanged event
gridGroupingControl1.SelectedRecordsChanged += GridGroupingControl_SelectedRecordsChanged;

private void GridGroupingControl_SelectedRecordsChanged(object sender, SelectedRecordsChangedEventArgs e)
{
    // Iterating through selected records
    foreach (var record in e.NewRecords)
    {
        // Perform actions on the selected record
        Console.WriteLine($"Selected record: {record.Index}");
    }
}

// Subscribe to the SelectedRecordsChanging event
gridGroupingControl1.SelectedRecordsChanging += GridGroupingControl_SelectedRecordsChanging;

private void GridGroupingControl_SelectedRecordsChanging(object sender, SelectedRecordsChangingEventArgs e)
{
    // Perform actions before the records are changed
    foreach (var record in e.NewRecords)
    {
        Console.WriteLine($"Changing record selection: {record.Index}");
    }
}
```

## Page-level Navigation/TOC
- [Focused Selection Demonstration](#focused-selection-demonstration)
- [Multiple Record Selection](#multiple-record-selection)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

## Cross References
- See also: [Syncfusion Documentation on Grid Controls](https://www.syncfusion.com/documentation)

<!-- tags: [Grid, Selection Modes, Windows Forms, Syncfusion, Multiple Record Selection, Focused Selection, API Reference, SelectedRecords, Events] keywords: [Selection Modes, Focused Selection, Multiple Record Selection, Grid, Windows Forms, SelectedRecords, SelectedRecordsChanged, SelectedRecordsChanging] -->
```