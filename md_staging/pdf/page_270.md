```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_270.jpeg
document_name: pdf
page_number: 270
page_id: pdf#page_270
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:32Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This page describes how to set up PDF page labels with different numbering styles for sections in VB.NET using Syncfusion PDF tools.

## Content

This section shows a VB.NET snippet that assigns different numbering styles to sections in a PDF document, using `PdfPageLabel` objects to configure page labels for each section.

### Setting Up Page Labels for Sections
- The code iterates through each section of the document, assigning a unique `PdfNumberStyle` based on the section index.

#### Code Example

```vb
Dim k As Integer = 0, i1 As Integer = 0
While k < ldoc.Section.Count
    Dim label As New PdfPageLabel()
    label.StartNumber = 1
    If k = 0 Then
        label.NumberStyle = PdfNumberStyle.Numeric
    ElseIf k = 1 Then
        label.NumberStyle = PdfNumberStyle.LowerLatin
    ElseIf k = 2 Then
        label.NumberStyle = PdfNumberStyle.UpperLatin
    End If

    label.Prefix = i1 & "-"
    ldoc.LoadedPageLabel = label
    i1 += 1
    k += 1
End While
```

- **Explanation**:
  - `k` is used to iterate over each section.
  - `i1` is used as a prefix for the page labels.
  - The `PdfNumberStyle` property is set based on the section index.
  - Each section's page label is configured with a different numbering style.
  - The `Prefix` property adds a numbered prefix to the page label.

## API Reference

### Methods Used
- **`PdfPageLabel()`**: Instantiates a new `PdfPageLabel` object.
- **`PdfPageLabel.StartNumber`**: Sets the starting page number for the label.
- **`PdfPageLabel.NumberStyle`**: Specifies the numbering style for the label (e.g., Numeric, LowerLatin, UpperLatin).
- **`PdfPageLabel.Prefix`**: Sets a prefix for the page label.
- **`PdfDocument.LoadedPageLabel`**: Assigns the page label to the current section.

## Code Examples

The provided VB.NET snippet demonstrates how to apply different numbering styles to sections in a PDF document, ensuring each section has a unique and visually distinct page labeling format.

<!-- tags: [Syncfusion, WinForms, PDF, numbering styles, page labels, VB.NET] keywords: [PdfPageLabel, PdfNumberStyle, prefix, sections, document, numbering, styles, labels] -->
```