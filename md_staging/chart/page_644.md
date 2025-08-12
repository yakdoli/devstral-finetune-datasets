```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_644.jpeg
document_name: chart
page_number: 644
page_id: chart#page_644
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:54Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- The document explains how to print a chart using a specified range with multiple pages.
- It details the PrintPage event and provides a sample link to view the implementation.

## Content

### Notes
The initial page will be printed based on the specified minimum and maximum value. In further pages, the minimum value will be the maximum value of the previous page, and the maximum will be the sum of the current page minimum value and the specified maximum value in the Range.

### Events

#### Table 5: Event Table

| Event     | Description                                                               | Arguments      | Type       | Reference links |
|-----------|---------------------------------------------------------------------------|----------------|------------|-----------------|
| PrintPage | This event will be triggered when the chart is printed.                | PrintPageEventArgs | Server side | NA             |

### Sample Link
To view a sample:
1. Open the Syncfusion Dashboard.
2. Click the Windows Forms drop-down list and select Run Locally Installed Samples.
3. Navigate to Chart Samples -->Print -->Multiple Page Printing.

---

## API Reference
None

## Code Examples
None

## Page-level Navigation/TOC
N/A

## Cross References
None

## RAG Annotations
<!-- tags: [charts, windows forms, printpage event, multiple page printing, syncfusion dashboard] keywords: [charts, windows forms, print, print page event, multiple pages, sample link, syncfusion dashboard] -->
```