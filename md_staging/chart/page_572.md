<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_572.jpeg
document_name: chart
page_number: 572
page_id: chart#page_572
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:34Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes how to launch and save charts in various formats.
- Explains the editable text support for EPS images and how to export them using the Chart control.

## Content

### File Launch and Supported Formats

`' Launches the file.`  
```csharp
System.Diagnostics.Process.Start(exportFileName)
```

**Usage:** Based on the filename extension, the chart has built-in support to save the image in the following formats:

| File Extension | File Type |
|----------------|-----------|
| .bmp          | BMP       |
| .jpg          | JPEG      |
| .jpeg         | JPEG      |
| .gif          | GIF       |
| .tiff         | TIFF      |
| .Wmf          | WMF       |
| .emf          | EMF       |
| .svg          | SVG (Scalable Vector Graphics) |
| .eps          | Post Script |

**Note:** If the specified extension is none of the above, then the chart is exported as a bitmap.

During runtime, the Chart control can be saved as a file using the **Chart Toolbar** save option.

### Editable Text Support for EPS Images

**Description:** The Chart control can export an EPS image with editable text by setting the `EditableText` property to `true`.

**Code Example:**
```csharp
[CS]
ToPostScript toPostScript = new ToPostScript();
toPostScript.EditableText = true;
using (Graphics g =
    toPostScript.GetRealGraphics(this.chartControl1.Size))
{
    this.chartControl1.Draw(g, this.chartControl1.Size);
    g.Dispose();
}
```

## API Reference

### Namespace and Class
- `System.Diagnostics`
- `Syncfusion.Windows.Forms.Chart`
- `ToPostScript` (for EPS export)

### Properties
- `EditableText` (Boolean): Determines if the text in the EPS image is editable.

### Methods
- `GetRealGraphics(Size)`: Retrieves the Graphics object for rendering.
- `Draw(Graphics, Size)`: Draws the chart onto the specified Graphics object.

## Code Examples

The example demonstrates how to export a chart as an EPS file with editable text.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Chart Control, EPS Export, Editable Text] keywords: [Essential Chart, File Formats, Save Options, PostScript, WMF, EMF, SVG, GIF, TIFF, JPEG, BMP] -->