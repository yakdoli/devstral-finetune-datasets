```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_737.jpeg
document_name: grid
page_number: 737
page_id: grid#page_737
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

At design time, the data can be sorted by accessing the `SortedColumns` property under the TableDescriptor section in the property grid of the Grid Grouping control. This will open the SortColumnDescriptorCollection Editor. In that Editor, clicking the Add button will add the existing columns into the collection. The `Name` and `SortDirection` in the property window of the editor will let you specify your desired field name to sort and the sort order. The image given below illustrates this process.

![SortColumnDescriptor Collection Editor](#image)

Figure 294: SortColumnDescriptor Collection Editor

### Programmatically

Sorting can be applied to the grid data by specifying the desired field name to the `TableDescriptor.SortedColumns.Add()` method.

## API Reference

### Sorting Data

- To sort data programmatically, use the following method:

   ```csharp
   TableDescriptor.SortedColumns.Add("FieldName" [, "SortDirection"]);
   ```

   Where:
   - `FieldName`: The name of the field to sort by.
   - `SortDirection`: The direction of sorting, either `Ascending` or `Descending`.

### Example

Here is an example of how to sort by a specific field programmatically:

```csharp
// Assuming gridGroupingControl is the instance of the Grid Grouping Control
gridGroupingControl.TableDescriptor.SortedColumns.Add("QuantityPerUnit", "Descending");
```

## Code Examples

**Design-Time Sorting Example:**

1. Open the Grid Grouping control's property grid and access the `TableDescriptor` section.
2. Click on the `SortedColumns` property.
3. In the SortColumnDescriptorCollection Editor, click the `Add` button to add the existing columns.
4. In the property window, select the desired field (`Name`) and specify the `SortDirection`.

**Programmatic Sorting Example:**

```csharp
// Example of adding a sorted column to the Grid Grouping Control
gridGroupingControl.TableDescriptor.SortedColumns.Add("FieldName", "SortDirection");
```

## Page-level Navigation/TOC (if applicable)

- [x] Design-Time Sorting
- [x] Programmatically Sorting

## Cross References

See also:
- Grid Grouping Control
- Property Grid
- SortColumnDescriptorCollection Editor

## RAG Annotations

<!-- tags: grid, windows forms, sorting, designer, programmatically, syncfusion windows forms, tabledescriptor, sortedcolumns, sortcolumndescriptorcollection editor, design time, run time keywords: grid, tabledescriptor, sortedcolumns, sortcolumn, add(), sortdirection, descending, ascending, designer, programmatic sorting -->
```