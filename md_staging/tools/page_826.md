```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_826.jpeg
document_name: tools
page_number: 826
page_id: tools#page_826
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:15Z
fidelity: lossless
-->

## Overview
- Associate Button, TextBox, and ListBox with the EditableList control.
- Specify the size of the EditableList control and add it to the Form.
- Populate and edit the list through DataSource or manually in the property editor.

## Content

### Step 3: Associate Button, TextBox, and ListBox with the EditableList control
```csharp
this.editableList1.Controls.Add(this.editableList1.Button);
this.editableList1.Controls.Add(this.editableList1.ListBox);
this.editableList1.Controls.Add(this.editableList1.TextBox);
```

```vbnet
Me.editableList1.Controls.Add(Me.editableList1.Button)
Me.editableList1.Controls.Add(Me.editableList1.ListBox)
Me.editableList1.Controls.Add(Me.editableList1.TextBox)
```

### Step 4: Specify the size of the EditableList control and add it to the Form
```csharp
this.editableList1.Size = new System.Drawing.Size(144, 40);
this.Controls.Add(this.editableList1);
```

```vbnet
Me.editableList1.Size = New System.Drawing.Size(144, 40)
Me.Controls.Add(Me.editableList1)
```

### 3.5.8.7.3 Concepts and Features: Populating and Editing the List

#### Populate the list

The List can be populated in 2 ways. One is to specify the DataSource, and another is to edit the list manually in the property editor.

#### To populate through DataSource

```csharp
// Specifies the DataSource.
editableList1.ListBox.DataSource=<DataSource>;
```

```vbnet
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [EditableList, Button, TextBox, ListBox, DataSource, Form, Syncfusion WinForms, C#, VB.NET] -->
```