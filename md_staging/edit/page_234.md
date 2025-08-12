```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_234.jpeg
document_name: edit
page_number: 234
page_id: edit#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:19Z
fidelity: lossless
-->

## Page Preview Border Control

### Overview
- Customization of page border parameters in page preview.
- Methods to set and remove the page border in page preview.

## Control Method and Description

| Edit Control Method      | Description                                      |
|--------------------------|--------------------------------------------------|
| SetPageBorder           | Sets parameters of border that's drawn in page preview. |
| RemovePageBorder        | Removes border drawing in page preview.           |

### Code Examples

#### C#
```csharp
// Set the page border.
this.editControl1.SetPageBorder(Syncfusion.Windows.Forms.Edit.Enums.FrameBorderStyle.DashDot, Color.Red,
    Syncfusion.Windows.Forms.Edit.Enums.BorderWeight.Bold);

// Remove the page border.
this.editControl1.RemovePageBorder();
```

#### VB.NET
```vbnet
' Set the page border.
Me.editControl1.SetPageBorder(Syncfusion.Windows.Forms.Edit.Enums.FrameBorderStyle.DashDot, Color.Red,
    Syncfusion.Windows.Forms.Edit.Enums.BorderWeight.Bold)

' Remove the page border.
Me.editControl1.RemovePageBorder()
```

Refer to the Printing Demo sample for more information in this regard.

### Printing Demo Path

```
..My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Edit.Windows\Samples\2.0\Printing Support\PrintingDemo
```

## 4.12 Performance

This section discusses the fast load mode of the Edit Control.

### Quick File Loading

The Edit Control loads files extremely quickly, and hence its performance is unmatched by any of our competitors or the Visual Studio.NET IDE.
```

<!-- tags: [Syncfusion, Winforms, Edit Control, Printing, Performance, Fast Load] keywords: [SetPageBorder, RemovePageBorder, FrameBorderStyle, BorderWeight, Printing Demo, Quick File Loading] -->
```