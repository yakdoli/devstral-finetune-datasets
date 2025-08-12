```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_574.jpeg
document_name: chart
page_number: 574
page_id: chart#page_574
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:33Z
fidelity: lossless
-->

## Overview

- **Editing Chart Titles**: Shows how to edit chart titles in Photoshop using EPS format.
- **Exporting Charts**: Explains the process of exporting charts to Word documents programmatically.
- **Note on Chart Wrapping**: Highlights limitations in wrapping and formatting charts within EPS images.

## Content

### Figure 353: EPS Chart with Editable Text

![Figure 353: EPS Chart with Editable Text](https://example.com/eps-chart-editable-text.png)

**Note**: Chart wrapping and formatting will not be possible in the EPS image by enabling this property.

### 4.14.2 Exporting to Word Doc

The chart control can be exported to a Word doc file as an image using Essential DocIO. The chart control provides APIs to convert it to an image, while DocIO lets you insert this image into a Word Document file programmatically.

## API Reference

### Exporting Chart to Image

The chart control provides APIs to convert the chart to an image. These APIs can be used to generate the chart as a bitmap or other image formats that can then be inserted into a Word document.

### Inserting Image into Word Document

Using Essential DocIO, you can programmatically insert the generated image into a Word document. This involves using the DocIO APIs to create a new document or modify an existing one, and then adding the chart image at the desired location.

## Code Examples

### Example 1: Exporting Chart to Image
```csharp
// Code to export chart to image
// Example usage of chart control's API to generate image
```

### Example 2: Inserting Image into Word Doc
```csharp
// Code to insert image into Word document using DocIO
// Programmatically adding the chart image to the Word document
```

## RAG Annotations
<!-- tags: [chart, eps, word doc, essential docio, export, formatting, syncfusion winforms, version: 11.4.0.26] 
keywords: [chart title editing, eps chart export, word document insertion, chart wrapping, essential docio, programmatically insert image, chart control api, word doc export] -->
```