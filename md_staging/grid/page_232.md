```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: grid
page_number: 232
page_id: grid#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.1.4.5.3 Workbook

The worksheets in a workbook can be displayed as tabs for easier view and selection of worksheets, similar to Excel. This is achieved by using the Tab Bar Splitter control. You can add any number of Tab Bar pages to the Tab Bar Splitter control, and then add the Grid control to each Tab Bar page, to get the appearance similar to the Workbook in Excel.

#### Using C#

```csharp
[C#]

this.tarBarSplitterControl1.Controls.Add(this.tarBarPage1);
this.tarBarSplitterControl1.Controls.Add(this.tarBarPage2);
this.tarBarSplitterControl1.Controls.Add(this.tarBarPage3);

// Adding Grid controls to the Tab Bar Pages.
this.tarBarPagel.Controls.Add(this.gridControl1);
this.tarBarPage2.Controls.Add(this.gridControl2);
this.tarBarPage3.Controls.Add(this.gridControl3);
```

#### Using VB.NET

```vbnet
[VB.NET]

Me.tarBarSplitterControl1.Controls.Add(Me.tarBarPage1)
Me.tarBarSplitterControl1.Controls.Add(Me.tarBarPage2)
Me.tarBarSplitterControl1.Controls.Add(Me.tarBarPage3)

' Adding Grid controls to the Tab Bar Pages.
Me.tarBarPagel.Controls.Add(Me.gridControl1)
Me.tarBarPage2.Controls.Add(Me.gridControl2)
Me.tarBarPage3.Controls.Add(Me.gridControl3)
```

## API Reference

### Code Examples

#### C# Example

```csharp
this.tarBarSplitterControl1.Controls.Add(this.tarBarPage1);
this.tarBarSplitterControl1.Controls.Add(this.tarBarPage2);
this.tarBarSplitterControl1.Controls.Add(this.tarBarPage3);

this.tarBarPagel.Controls.Add(this.gridControl1);
this.tarBarPage2.Controls.Add(this.gridControl2);
this.tarBarPage3.Controls.Add(this.gridControl3);
```

#### VB.NET Example

```vbnet
Me.tarBarSplitterControl1.Controls.Add(Me.tarBarPage1)
Me.tarBarSplitterControl1.Controls.Add(Me.tarBarPage2)
Me.tarBarSplitterControl1.Controls.Add(Me.tarBarPage3)

Me.tarBarPagel.Controls.Add(Me.gridControl1)
Me.tarBarPage2.Controls.Add(Me.gridControl2)
Me.tarBarPage3.Controls.Add(Me.gridControl3)
```

## RAG Annotations

<!-- tags: [workbook, tab bar splitter, grid control, syncfusion windows forms, syncfusion sdk] keywords: [workbook, tab bar, grid, control, excel, appearance, syncfusion winforms] -->
```