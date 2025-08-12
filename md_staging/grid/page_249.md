```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_249.jpeg
document_name: grid
page_number: 249
page_id: grid#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
If s1 <> "" Then
    If Double.TryParse(s1, NumberStyles.Number, Nothing, d) AndAlso d > 0 Then
        sum += d
    End If
End If
Next r
Return sum.ToString()
End If
Return ""
End Function
```

### Adding Your Formula to the Library

1. The last step is to actually add your formula to the library. You should do this after the grid has been created, say in a Form.Load event handler.

#### C#

```csharp
GridFormulaCellModel cellModel =
    this.gridControl1.CellModels["FormulaCell"] as GridFormulaCellModel;

// Add a formula named SumPosNums to the Library.
cellModel.Engine.AddFunction("SumPosNums", new GridFormulaEngine.LibraryFunction(ComputeSumPosNums));
```

#### VB.NET

```vb
Dim cellModel As GridFormulaCellModel =
    Me.gridControl1.CellModels("FormulaCell")

' Add a formula named SumPosNums to the Library.
cellModel.Engine.AddFunction("SumPosNums", New GridFormulaEngine.LibraryFunction(AddressOf ComputeSumPosNums))
```

### 4.1.4.6.6 Function Reference Section

In this section, the library functions that are shipped in the Essential Calculate library are discussed. The arguments required by each of these functions are listed in bold text. Optional arguments are listed in a normal text.

Following functions are discussed under this section:
```