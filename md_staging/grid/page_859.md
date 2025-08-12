```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_859.jpeg
document_name: grid
page_number: 859
page_id: grid#page_859
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:28Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- The GridColumnDescriptor Collection Editor allows for fine-tuning of grid columns through a visual interface or programmatically.
- Demonstrates the flexibility in controlling the appearance, behavior, and design of grid columns both visually and using code.

### Content

#### Figure 332: GridColumnDescriptor Collection Editor

![GridColumnDescriptor Collection Editor](#)
The image shows the **GridColumnDescriptor Collection Editor**, which is used to configure various properties of a grid's columns. The left side lists the members (columns), while the right side displays the properties of the selected column, including appearance, behavior, design, and layout settings.

##### Behavior and Layout of GridColumns

- **Appearance:** Controls how the column is visually styled.
- **AllowSort:** Determines whether the column can be sorted by the user.
- **SortByDisplayMember:** Indicates whether sorting should use the column's display member.
- **Design:** Includes settings such as the column's name and width.

#### Programmatically

You can control the appearance of the columns through code as well. Below is the code that applies different styles to the various columns in the grid.

```csharp
GridColumnDescriptor desc1 = new GridColumnDescriptor();
desc1.MappingName = "ProductName";
```

This code snippet demonstrates how to create and configure a `GridColumnDescriptor` object for a column named "ProductName". Additional properties can be set to further customize the column's behavior and appearance.

### API Reference

#### GridColumnDescriptor
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Members:**
  - **MappingName:** String representing the property name to map the column to.

### Code Examples

#### C#

The following example shows how to programmatically define a `GridColumnDescriptor`.

```csharp
GridColumnDescriptor desc1 = new GridColumnDescriptor();
desc1.MappingName = "ProductName";
```

### Cross References

- See also: [GridColumnDescriptor Properties](#)
- [GridColumnDescriptor Methods](#)
- [GridColumnDescriptor Events](#)

### RAG Annotations

<!-- tags: [syncfusion, grid, windows forms, gridcolumndescriptor, programmatically] keywords: [GridColumnDescriptor, MappingName, ProductName, AllowSort, SortByDisplayMember, Design, Layout] -->
```