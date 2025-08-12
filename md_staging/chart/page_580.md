```<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_580.jpeg
document_name: chart
page_number: 580
page_id: chart#page_580
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:07Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Specifies the image size mode using `CenterImage`.
- Demonstrates exporting a chart control to a form.

## Content

### Specifying Image Size Mode

```csharp
// Specify the image size mode.
Me.gridControl1(1, 1).ImageSizeMode = GridImageSizeMode.CenterImage
```

### Exporting Chart Control to a Form

6. Add the code given below in the form with the chart control to be exported.

#### C#

```csharp
[C#]

private Form2 gridForm;
this.gridForm= new Form2();

string fileName = Application.StartupPath+"\\chartexport";
string file = fileName + ".gif";

if (!System.IO.File.Exists(file))
    this.chartControl1.SaveImage(file);

// Specify the filename as the name of the form.
gridForm.Name = file;

// Shows the form with grid control with the chart exported.
gridForm.ShowDialog();
```

#### VB.NET

```vb
[VB.NET]

Private gridForm As Form2
Me.gridForm= New Form2()

Dim fileName As String = Application.StartupPath & "\chartexport"
Dim file As String = fileName & ".gif"

If (Not System.IO.File.Exists(file)) Then
    Me.chartControl1.SaveImage(file)
End If

' Specify the filename as the name of the form.
gridForm.Name = file

' Shows the form with grid control with the chart exported.
gridForm.ShowDialog()
```

### Sample Location

A sample demonstrating the above is available in our installation at the following location:

```
My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Chart.Windows\Samples\2.0\Export\Chart Export Data
```

### Summary

- Specifies the export process of a chart control to a form.
- Provides code snippets for both C# and VB.NET languages.
- Demonstrates the use of `SaveImage` method to export the chart as a GIF file.

## Code Examples

#### C#

```csharp
private Form2 gridForm;
this.gridForm= new Form2();

string fileName = Application.StartupPath+"\\chartexport";
string file = fileName + ".gif";

if (!System.IO.File.Exists(file))
    this.chartControl1.SaveImage(file);

gridForm.Name = file;
gridForm.ShowDialog();
```

#### VB.NET

```vb
Private gridForm As Form2
Me.gridForm= New Form2()

Dim fileName As String = Application.StartupPath & "\chartexport"
Dim file As String = fileName & ".gif"

If (Not System.IO.File.Exists(file)) Then
    Me.chartControl1.SaveImage(file)
End If

gridForm.Name = file
gridForm.ShowDialog()
```

## Tags and Keywords
```html
<!-- tags: [chart, windows forms, image export, grid control] keywords: [chart export, image size mode, center image, form2, startup path, filename, show dialog] -->
```
```