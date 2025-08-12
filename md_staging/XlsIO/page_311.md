```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_311.jpeg
document_name: XlsIO
page_number: 311
page_id: XlsIO#page_311
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:06Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to set the paper size in XlsIO.
- Explains the usage of `Page Setup` to configure the paper settings.
- Provides code examples in C# and VB.NET to set the paper type.

## Content

### Page Setup - Page [Paper Size]
Figure 111 illustrates the "Page Setup" dialog where various paper options can be configured.

![Figure 111: Page Setup - Page [Paper Size]](figures/figure111.png)

Following code example illustrates how to set the paper size in XlsIO.

#### Setting the Paper Size in XlsIO

##### C#
```csharp
// Setting the Paper Type.
sheet.PageSetup.PaperSize = ExcelPaperSize.PaperA3;
```

##### VB.NET
```vb
' Setting the Paper Type.
sheet.PageSetup.PaperSize = ExcelPaperSize.PaperA3
```

### 4.3.1.4 Breaks
This section further explores additional page layout configurations and breaks.

## API Reference

### Paper Size
- **Namespace:** Excel.PageSetup
- **Property:** PaperSize
- **Type:** ExcelPaperSize
- **Description:** Sets the size of the paper used for printing the worksheet.
- **Parameters:**
  - **ExcelPaperSize:** An enumeration representing various paper sizes such as `PaperA3`, `Letter`, `Legal`, etc.
  
## Code Examples

#### C# Example
```csharp
// Setting the Paper Type.
sheet.PageSetup.PaperSize = ExcelPaperSize.PaperA3;
```

#### VB.NET Example
```vb
' Setting the Paper Type.
sheet.PageSetup.PaperSize = ExcelPaperSize.PaperA3
```

## Cross References
See also:
- Page Setup Overview
- Advanced Page Layout Configuration

<!-- tags: [xlsio, winforms, paper size, page setup, printing, breaks] keywords: [paper type, c#, vb.net, api reference, code examples, printing configuration, layout] -->
```