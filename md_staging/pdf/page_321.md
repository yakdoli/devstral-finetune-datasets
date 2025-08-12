```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_321.jpeg
document_name: pdf
page_number: 321
page_id: pdf#page_321
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:35Z
fidelity: lossless
-->

## AutoDetectPageBreak

### Overview
- This page explains how to enable and utilize the `AutoDetectPageBreak` property in the HtmlConverter to handle custom page breaks using standard CSS styles.
- Demonstrates enabling custom page breaks for both C# and VB.NET languages.

### Content

#### Overview of AutoDetectPageBreak Feature
The `HtmlConverter` supports custom page breaks with standard CSS styles like `page-break-before:always` and `page-break-after:always` that can be applied to any HTML object. You can enable custom page breaks by setting the `AutoDetectPageBreak` property to `True`.

##### Code Example in C#
The following code example illustrates how to enable and use custom page breaks in C#:

```csharp
[C#]

HtmlConverter html = new HtmlConverter();

// Activate the Page Break
html.AutoDetectPageBreak = true;

// Convert the Html file as an image
HtmlToPdfResult result = html.Convert(txtUrl.Text, ImageType.Metafile, (int)width, -1, AspectRatio.KeepWidth);

// Specify the quality of the metafile
PdfMetafile mf = new PdfMetafile(result.RenderedImage as Metafile);
mf.Quality = 100;

PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat();
format.Break = PdfLayoutBreakType.FitPage;
format.Layout = PdfLayoutType.Paginate;

//Render the image in PDF document
mf.Draw(page, new PointF(0, 0), format);
```

##### Code Example in VB.NET
Similarly, here is the equivalent example in VB.NET:

```vb.net
[VB.NET]

Dim html As HtmlConverter = New HtmlConverter()

' Activate the Page Break
html.AutoDetectPageBreak = True

' Convert the Html file as an image
Dim result As HtmlToPdfResult = html.Convert(txtUrl.Text, ImageType.Metafile, CInt(Fix(width)), -1, AspectRatio.KeepWidth)

' Specify the quality of the metafile
```

## API Reference
- **Property:** `AutoDetectPageBreak`
  - **Type:** `Boolean`
  - **Description:** Enables or disables the detection of custom page breaks in the HTML content.
  - **Default:** `False`
  - **Required:** Optional

## Code Examples

### C# Example
```csharp
HtmlConverter html = new HtmlConverter();
html.AutoDetectPageBreak = true;
// Conversion and rendering logic as demonstrated above
```

### VB.NET Example
```vb.net
Dim html As HtmlConverter = New HtmlConverter()
html.AutoDetectPageBreak = True
' Conversion and rendering logic as demonstrated above
```

<!-- tags: [Syncfusion, WinForms, HtmlConverter, AutoDetectPageBreak, C#, VB.NET] keywords: [custom page breaks, CSS styles, page-break-before, page-break-after, HtmlConverter, AutoDetectPageBreak, C#, VB.NET] -->
```