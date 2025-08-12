```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_594.jpeg
document_name: chart
page_number: 594
page_id: chart#page_594
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:56Z
fidelity: lossless
-->

## Overview
- This section explains how to use the PrintPreviewDialog in Windows Forms to preview a chart before printing it.
- It includes code examples in both C# and VB.NET for integrating print preview functionality.
- The PrintDocument provided by the chart control is utilized to generate the print preview.

## Content

### 4.16 Printing and Print Preview

#### Print Preview

The chart provides a `PrintDocument` that can be sent to the .NET `PrintPreviewDialog` to get a preview of the chart that gets printed. Here is some code that shows how this is done.

```csharp
[C#]

PrintPreviewDialog printPreviewDialog1 = new PrintPreviewDialog();
printPreviewDialog1.Document = this.chartControl1.PrintDocument;
printPreviewDialog1.ShowDialog();
```

```vb
[VB.NET]

Me.printPreviewDialog1 = New System.Windows.Forms.PrintPreviewDialog
printPreviewDialog1.Document = Me.chartControl1.PrintDocument
printPreviewDialog1.ShowDialog()
```

The code above demonstrates how to display a print preview dialog for the chart. The chart's `PrintDocument` is set as the document source for the `PrintPreviewDialog`, allowing users to preview the chart layout and settings before printing.

#### Print Preview Dialog Box

The following image shows the Print Preview Dialog Box for a chart.

![Figure 361: Print Preview Dialog Box](image.png)

Figure 361: Print Preview Dialog Box

The Print Preview Dialog Box provides options to zoom in and out, rotate the page, and navigate through multiple pages of the chart, ensuring that the layout and appearance are correct before finalizing the print.

## API Reference
- **Namespaces**: System.Windows.Forms
- **Classes**: PrintPreviewDialog, PrintDocument
- **Methods**: ShowDialog()

## Code Examples

The provided examples demonstrate how to integrate print preview functionality for chart controls in Windows Forms applications using both C# and VB.NET. The `PrintDocument` associated with the chart is used as the source for the print preview, offering an intuitive and interactive way to review the chart before printing.

## RAG Annotations
<!-- tags: [WinForms, PrintPreviewDialog, PrintDocument, ChartControl, chart] keywords: [PrintPreviewDialog, PrintDocument, PrintPreview, chart, Windows Forms] -->
```