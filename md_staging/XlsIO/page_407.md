```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_407.jpeg
document_name: XlsIO
page_number: 407
page_id: XlsIO#page_407
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:19Z
fidelity: lossless
-->

# Chapter: Essential XlsIO

## Overview
- Explains the feature to zoom in and out in Excel using the XlsIO library.
- Demonstrates setting and retrieving display scales in a worksheet.
- Describes methods to show or hide worksheet elements like Grid Lines, Headings, and Scroll Bars.

## Content

### Zooming in XlsIO

XlsIO allows to zoom a worksheet by using the **Zoom** property of **IWorksheet**. It returns or sets the display size of the window as a percentage (100 equals normal size, 200 equals double size, and so on).

Following code example illustrates how to zoom a worksheet to 150 percent.

```csharp
[C#]

// Zooming to 150 percent.
sheet.Zoom = 150;
```

```vb
[VB]

// Zooming to 150 percent
sheet.Zoom = 150
```

#### 4.7.3 Show/Hide Worksheet Elements

This topic describes how to show/hide the elements in a worksheet and workbook.

- Grid Lines
- Headings
- Scroll Bar

## API Reference (if applicable)

The **Zoom** property of the **IWorksheet** interface is used to get or set the zoom level of the worksheet.

### Parameters:
- **sheet.Zoom**: Sets the display scale as a percentage.
  
### Example:
- **C#**:
  ```csharp
  sheet.Zoom = 150;
  ```
- **VB.NET**:
  ```vb
  sheet.Zoom = 150
  ```

<!-- tags: [XlsIO, zoom, worksheet, elements, grid lines, headings, scroll bar] keywords: [display_size, zoom_level, worksheet_elements, show_hide_elements] -->
```