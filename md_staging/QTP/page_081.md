```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: QTP
page_number: 081
page_id: QTP#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:55Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Explains how to set the current cell in a Grid using the SetCurrentCell method.
- Covers use cases for GridControl, GridGroupingControl, and GridDataBoundControl.
- Demonstrates usage examples for QTP testing.

## Content

### 7.2.2 How to set the current cell in Grid

The `SetCurrentCell` method is used to set the current cell in Grid or activate a cell as the current cell in Grid. This method is used in `GridControl`, `GridGroupingControl`, and `GridDataBoundControl`.

**Use Case Scenarios**  
This method enables a Grid cell in QTP testing.

#### Methods Table

| Method           | Description                             | Parameters                                                                     | Return Type |
|------------------|-----------------------------------------|--------------------------------------------------------------------------------|-------------|
| SetCurrentCell   | Sets the location of current cell in Essential Grid             | For the Grid control: <br> `public void SetCurrentCell(int row, int col)` | Void        |
|                  |                                         | For the GridGrouping control: <br> `public void SetCurrentCell(object row, object col)` | Void        |
|                  |                                         | For GridDataBoundGrid control: <br> `public void SetCurrentCell(int row, int col)` | Void        |

**Note:** GridGrouping control uses iterated rows to set the current cell in the respective tables.

The following code examples illustrate how to use the `SetCurrentCell` method.

#### For GridControl
```csharp
SwfWindow("Form1").SwfObject("gridControl1").SetCurrentCell 3,1
```

#### For GridGroupingControl
```csharp
SwfWindow("Form1").SwfObject("gridGroupingControl1").SetCurrentCell 3,"Col2"
```

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridControl, GridGroupingControl, GridDataBoundControl
- **Method:** SetCurrentCell

#### Parameters
| Name | Type | Description | Default | Required |
|------|------|-------------|---------|----------|
| row  | int  | Row index of the cell | NA      | Yes     |
| col  | int/object | Column index or name of the cell | NA     | Yes     |

#### Returns
- `Type`: Void
- `Description`: No return value; sets the current cell.

## Code Examples (if applicable)
The code examples provided above illustrated the usage of the `SetCurrentCell` method in GridControl and GridGroupingControl.

## Page-level Navigation/TOC (if applicable)
- This page is part of the "Essential QuickTest Professional" section in the user guide, focusing on setting the current cell in a Grid.

<!-- tags: [Essential QuickTest Professional, GridControl, GridGroupingControl, GridDataBoundControl, SetCurrentCell] keywords: [set current cell, Grid, GridControl, GridGroupingControl, GridDataBoundControl, QTP testing, return type, parameters, method description] -->
```