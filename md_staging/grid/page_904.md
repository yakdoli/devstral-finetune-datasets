```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_904.jpeg
document_name: grid
page_number: 904
page_id: grid#page_904
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:22Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains how to create column sets to span columns in the grid.
- Guide on using the GridColumnSetDescriptor Collection Editor and GridColumnSpanDescriptor Collection Editor for span configuration.
- Demonstrates managing column properties and address spans within a grid control.

## Content

### Setting Column Sets and Spans

#### Figure 362: Creating Column Sets to Span Columns in the Grid

The grid control interface shown in the figure includes several key components and configuration steps for creating column sets to span columns. The following are the primary elements and their descriptions:

1. **Properties Window**:
   - Displays the properties for the `gridGroupingControl1` control. Key properties shown include:
     - **Columns**: A dropdown menu labeled `Columns`.
     - **ColumnSets**: A dropdown menu labeled `ColumnSets` with a property count of 3.

2. **GridColumnSetDescriptor Collection Editor**:
   - **Members**:
     - Lists the column set members:
       - **0**: ColumnSet ID
       - **1**: ColumnSet Name
       - **2**: ColumnSet Address
   - **ColumnSet Address properties**:
     - Allows manipulation of column set addresses.
     - Lists column descriptors:
       - **TableDescriptors**:
         - **Name**: "ColumnSet Address"
         - **Count**: 3
         - **ColumnSpans**: Indicates the span count.

3. **GridColumnSpanDescriptor Collection Editor**:
   - **Members**:
     - Lists the column span members:
       - **0**: Address
       - **1**: City
       - **2**: Country
     - Includes options to **Add** or **Remove** column span members.
   - **Address properties**:
     - Lists column descriptors:
       - **TableDescriptors**:
         - **Name**: "Address"
         - **Range**: "R0C0:R0C1"

This interface facilitates the configuration of column spans, enabling precise control over the layout and structure of the grid.

---

### Key Configuration Steps
- Use the **GridColumnSetDescriptor Collection Editor** to define column sets and their addresses.
- Utilize the **GridColumnSpanDescriptor Collection Editor** to manage column spans by adding or removing members.
- Adjust the span ranges as needed to ensure proper alignment and layout of the grid.

## API Reference

### Namespaces and Classes
- **Syncfusion.Windows.Forms.Grid.Grouping**

### Properties
- **ColumnSets**: Represents an address property for configuring column sets.
- **TableDescriptors**: Contains properties like `Name` and `Count` for defining column span descriptors.

## Code Examples

#### Example: Configuring Column Sets and Spans in C#
```csharp
// Example demonstrating how to configure column sets and spans in a grid.
using Syncfusion.Windows.Forms.Grid;

// Initialize the grid control
GridGroupingControl gridGroupingControl = new GridGroupingControl();

// Configure ColumnSets
GridColumnSetDescriptor columnSet = new GridColumnSetDescriptor();
columnSet.Name = "Address_Set";
columnSet.ColumnSpan = "R0C0:R0C1";

// Add the column set to the grid
gridGroupingControl.GridColumnSetDescriptors.Add(columnSet);

// Update the grid settings
gridGroupingControl.Refresh();
```

---

## Cross References
- For more information on grid properties, refer to the Grid API documentation.
- See additional examples for configuring grids in the Syncfusion WinForms user guide.

<!-- tags: [grid, windows forms, column sets, column spans, Syncfusion] keywords: [grid grouping control, column descriptors, span configuration, gridspan, gridset] -->
```