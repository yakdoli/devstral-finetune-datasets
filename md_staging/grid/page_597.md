```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_597.jpeg
document_name: grid
page_number: 597
page_id: grid#page_597
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Here are some code samples that will create a `DataTable` and bind it to a Grid Grouping control. Once you have a `DataTable` object populated, you can use the `GridGroupingControl.DataSource` property to implement the binding.

## Overview
- Include the required namespace.
- Create an instance of Grid Grouping control and specify its size.
- Set up the Data Source.

## Content

### Step 1: Include the Required Namespace

#### C#
```csharp
using Syncfusion.Windows.Forms.Grid.Grouping;
```

#### VB.NET
```vb.net
Imports Syncfusion.Windows.Forms.Grid.Grouping
```

### Step 2: Create an Instance of Grid Grouping Control and Specify Its Size

#### C#
```csharp
private Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl gridGroupingControl;

this.gridGroupingControl = new Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl();
this.gridGroupingControl.Size = new System.Drawing.Size(160, 200);
```

#### VB.NET
```vb.net
Private gridGroupingControl As Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl

Me.gridGroupingControl = New Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl()
Me.gridGroupingControl.Size = New System.Drawing.Size(160, 200)
```

### Step 3: Set Up the Data Source

#### C#
```csharp
DataTable myDataTable = new DataTable("MyDataTable");

// Declare the Data Column and Data Row variables.
DataColumn myDataColumn;
DataRow myDataRow;

// Create a new Data Column, set the Data Type and Column Name and add
```

## API Reference
- `GridGroupingControl.DataSource`: Property to bind the `DataTable` to the grid.

## Code Examples
- Example includes creating a `DataTable`, adding columns, populating data rows, and setting the `DataSource` of the `GridGroupingControl`.

## See also
- Grid Grouping Control Documentation
- DataTable Creation and Population

<!-- tags: [Syncfusion Winforms, Essential Grid, GridGroupingControl, DataTable, DataBinding, Windows Forms] keywords: [DataTable, DataBinding, GridGroupingControl, Windows Forms, Essential Grid] -->
```