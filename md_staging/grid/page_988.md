```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_988.jpeg
document_name: grid
page_number: 988
page_id: grid#page_988
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
pd.DefaultPageSettings.Landscape = True
ppv.ShowDialog()
```

## Code for Print Dialog Box

### [C#]

```csharp
GridPrintDocument pd = new GridPrintDocument(this.gridGroupingControl1.TableControl);
PrintDialog printDialog = new PrintDialog();
printDialog.Document = pd;
pd.DefaultPageSettings.Landscape = true;
if (printDialog.ShowDialog() == DialogResult.OK)
    pd.Print();
```

### [VB.NET]

```vb
Dim pd As New GridPrintDocument(Me.gridGroupingControl1.TableControl)
Dim printDialog As New PrintDialog()
printDialog.Document = pd
pd.DefaultPageSettings.Landscape = True
If printDialog.ShowDialog() = Windows.Forms.DialogResult.OK Then
    pd.Print()
End If
```

Given below are sample screen shots.

<!-- tags: [Syncfusion, Windows Forms, Grid, Print Dialog Box, Landscape, C#, VB.NET] keywords: [GridPrintDocument, PrintDialog, DefaultPageSettings, DialogResult, Document, ShowDialog, Print] -->
```