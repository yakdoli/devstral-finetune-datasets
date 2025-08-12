```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_315.jpeg
document_name: XlsIO
page_number: 315
page_id: XlsIO#page_315
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:20Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Provides guidance on managing sheet backgrounds in XlsIO to avoid excessive file size increases.
- Explains setting Watermark using Headers and Footers in Print Preview.
- Demonstrates inserting background images using the `BackgroundImage` property in C# and VB.NET.

## Content

### Background Images and File Size Considerations
**Note:** The sheet backgrounds may tremendously increase the file size of the workbooks.

- Background images set in this manner cannot be printed.
- To set a Watermark that can be printed, use Headers and Footers.
- This feature is visible only in the Print Preview option and not in the Normal view.

### Inserting Background Images
XlsIO provides support for inserting background images through the `BackgroundImage` property of `IPageSetup`.

#### Code Example: Inserting a Background Image

```csharp
[C#]
// Setting the Paper Type.
sheet.PageSetup.BackgroundImage = image;
```

```vbnet
[VB.NET]
' Setting the Paper Type.
sheet.PageSetup.BackgroundImage = image
```

### Conclusion
The snippet demonstrates how to programmatically insert a background image into an Excel sheet using XlsIO in both C# and VB.NET.

## API Reference

### `BackgroundImage`
- **Description:** Specifies the image to be used as a background for the sheet.

### Parameters
- `image`: The image object to be set as the background.

### Returns
- None

## Code Examples

### C# Example

```csharp
[C#]
// Setting the Paper Type.
sheet.PageSetup.BackgroundImage = image;
```

### VB.NET Example

```vbnet
[VB.NET]
' Setting the Paper Type.
sheet.PageSetup.BackgroundImage = image
```

## Cross References
- Refer to the XlsIO documentation for detailed information on working with sheets and formatting.

## RAG Annotations
<!-- tags: [xlsio, watermark, headers, footers, backgroundimage, xlsio-winforms] keywords: [watermark, headers, footers, backgroundimage, file size, print preview, normal view] -->
```