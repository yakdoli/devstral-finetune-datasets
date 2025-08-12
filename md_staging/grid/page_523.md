```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_523.jpeg
document_name: grid
page_number: 523
page_id: grid#page_523
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:09Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- The `CanCut` method checks for selected ranges that can be cut or if the current cell's content can be cut. It returns a Boolean value indicating whether the content in the selected range of cells or the current cell's content can be cut. If no selected range is available for cutting, it returns false.
- The `Cut` method cuts the content of the selected cells and the current cell, pasting them to the clipboard.
- The `CutRange` method cuts the content of a specified range of cells and pastes it to the clipboard.

### Content

#### CanCut Method
- This method checks if there are selected ranges that can be cut or if the current cell's contents can be cut. The return type of this method is Boolean. If it returns true, it indicates that the content in the selected range of cells or the current cell's content can be cut. This method returns false, when no selected range is available to cut.

**Note:** Any content cut is pasted to the clipboard by default.

The following code examples show how to call this method:

**Using C#**
```csharp
this.gridControl1.Model.CutPaste.CanCut();
```

**Using VB.NET**
```vb
Me.gridControl1.Model.CutPaste.CanCut()
```

#### Cut Method
- This method cuts the content of the selected cells and the current cell, and pastes them to the clipboard.

The following code examples show how to call this method:

**Using C#**
```csharp
this.gridControl1.Model.CutPaste.Cut();
```

**Using VB.NET**
```vb
Me.gridControl1.Model.CutPaste.Cut()
```

#### CutRange Method
- This method cuts the content of a specified range of cells and pastes it to the clipboard. The range of cells to be cut is specified as a parameter.

The following code examples show how to call this method:

**Using C#**
```csharp
this.gridControl1.Model.CutPaste.CutRange(rangelist);
```

**Using VB.NET**
```vb
Me.gridControl1.Model.CutPaste.CutRange(rangelist)
```

### Page-level Navigation/TOC (if applicable)
- This page details methods for cutting content in the Grid control, including `CanCut`, `Cut`, and `CutRange`, along with code examples for both C# and VB.NET.

### Cross References
See also: grid control, clipboard operations, cell selection, Windows Forms controls.

<!-- tags: [Syncfusion, Winforms, Grid, Clipboard Operations, Cell Selection] keywords: [Essential Grid, CanCut, Cut, CutRange, Windows Forms] -->
```