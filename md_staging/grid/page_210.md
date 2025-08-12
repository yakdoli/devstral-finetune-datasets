```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: grid
page_number: 210
page_id: grid#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:37Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

```csharp
RegisterCellModel.GridCellType(gridControl1, 
CustomCellTypes.CalculatorTextBox);
CalculatorControl c2 = new CalculatorControl();
c2.BorderStyle = Border3DStyle.RaisedOuter;
c2.BackColor = Color.BlanchedAlmond;
style = gridControl1[6, 2];
style.CellType = CustomCellTypes.CalculatorTextBox.ToString();
style.Control = c2;
```

### 2. Using VB.NET

```vb
[VB.NET]

RegisterCellModel.GridCellType(Me.gridControl1, 
CustomCellTypes.CalculatorTextBox)
Dim c2 As CalculatorControl = New CalculatorControl()
c2.BorderStyle = Border3DStyle.RaisedOuter
c2.BackColor = Color.BlanchedAlmond
style = gridControl1(6, 2)
style.CellType = CustomCellTypes.CalculatorTextBox.ToString()
style.Control = c2
```

![Calculator Text Box Cell](https://via.placeholder.com/150)

**Figure 109: Calculator Text Box Cell**

## References
- Syncfusion, Essential Grid for Windows Forms documentation.

<!-- tags: [Syncfusion, Windows Forms, Grid, Essential Grid, Calculator Text Box, Cell Type, Custom Cell Types] keywords: [RegisterCellModel, GridCellType, CalculatorControl, Border3DStyle, BlanchedAlmond, CellType, Control, dropdown, calculator TextBox, Cell, C-Sharp, VB.NET] -->
```