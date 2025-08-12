```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_285.jpeg
document_name: edit
page_number: 285
page_id: edit#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:35Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Demonstrates how to databind an `EditControl` to a `DataSet`.
- Explains how to disable keyboard shortcuts in the EditControl.

## Content

### Databinding Example

```csharp
this.editControl1.DataBindings.Add("Text", this.dataset.Tables[0], "Code");
```

#### [VB.NET]

```vb
' Create a new DataSet.
Me.dataset = New DataSet("MyDataSet")

' Create a new DataTable.
Me.table = New DataTable("MyDataTable")

' Create a new DataColumn and add it to the DataTable.
Me.datacolumn = New DataColumn("Code", System.Type.GetType("System.String"))
Me.table.Columns.Add(Me.datacolumn)

' Create a new DataRow, and assign it to the specific column.
' Assign a string value 'program' to that DataRow-DataColumn field.
Me.datarow = Me.table.NewRow()
Me.datarow(Me.datacolumn) = program

' Add this DataRow to the DataTable.
Me.table.Rows.Add(Me.datarow)

' Add this DataTable to the DataSet.
Me.dataset.Tables.Add(Me.table)

' Databinding EditControl.Text to the DataColumn "Code",
' where "Code" contains the program to be displayed in the EditControl.
Me.editControl1.DataBindings.Add("Text", Me.dataset.Tables(0), "Code")
```

#### 5.6 How To Disable Keyboard Shortcuts For the Edit Control

> To disable keyboard shortcuts, first you must remove them from the context menu. Here is an example for removing the F5 shortcut.

#### [C#]

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    ContextMenu cm = this.editControl1.ContextMenu;
    foreach (MenuItem mi in cm.MenuItems)
    {
        this.RemoveShortcutInEditControl(mi);
    }
}
```

## API Reference (if applicable)

### Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

- See also: [other relevant sections or documents].

<!-- tags: [product, module, control, api, version?] keywords: [databinding, keyboard shortcuts, editcontrol, windows forms, DisableKeyboardShortcuts, Syncfusion Winforms, version 11.4.0.26] -->
```