```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: edit
page_number: 115
page_id: edit#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:00Z
fidelity: lossless
-->

## Overview
- This document explains the line wrapping and marking features in Windows Forms using custom images.
- Focuses on how to indicate the wrapped lines and wrapping points by setting various properties in the Edit Control.

## Content

2. Images that indicate the point at which the line is being wrapped. This can be set by using the `CustomLineWrappingMarkingImage` property.

Additionally, to indicate whether wrapped lines should be marked, the `MarkWrappedLines` property can be used.

### Table: Edit Control Properties and Descriptions

| Edit Control Property                      | Description                                                                 |
|--------------------------------------------|-----------------------------------------------------------------------------|
| MarkLineWrapping                           | Specifies whether line wrapping should be marked.                          |
| MarkWrappedLines                           | Specifies whether wrapped lines should be marked.                          |
| CustomWrappedLinesMarkingImage             | Gets / sets custom image that marks wrapped lines.                         |
| CustomLineWrappingMarkingImage             | Gets / sets custom image that marks wrapping lines.                        |

### C# Code Example

```csharp
[C#]
// Enable images to indicate line wrapping.
this.editControl1.MarkLineWrapping = true;

// Images that indicate the line that is being wrapped.
this.editControl1.CustomWrappedLinesMarkingImage =
    ((System.Drawing.Image)(resources.GetObject("$this.Sunset")));

// Images that indicate the point at which the line is being wrapped.
this.editControl1.CustomLineWrappingMarkingImage =
    ((System.Drawing.Image)(resources.GetObject("$this.Blue_hills")));

// Indicate wrapped lines.
this.editControl1.MarkWrappedLines = true;
```

### VB.NET Code Example

```vb
[VB.NET]
' Enable images to indicate line wrapping.
Me.editControl1.MarkLineWrapping = True

' Images that indicate the line that is being wrapped.
Me.editControl1.CustomWrappedLinesMarkingImage = 
    CType((resources.GetObject("$this.Sunset")), System.Drawing.Image)
```

### Notes

- The `MarkLineWrapping` property must be set to `true` to enable line wrapping marking.
- The `CustomWrappedLinesMarkingImage` and `CustomLineWrappingMarkingImage` properties should be set to a custom image to visually indicate wrapped lines and wrapping points, respectively.
- The `MarkWrappedLines` property, if set to `true`, will mark wrapped lines, providing a clear visual indication.

## Page-level Navigation/TOC

- **Main Title**: Essential Edit for Windows Forms
- **Section 1**: Introduction to Line Wrapping and Marking
- **Section 2**: Properties for Line Wrapping and Marking
- **Section 3**: Code Examples

## Cross References
- Refer to the section on [Properties Overview] for more details on other Edit Control properties.
- For design-time and runtime differences, see the [Design-Time Concepts] section.

<!-- tags: [WinForms, line wrapping, marking images, Edit Control, properties] keywords: [markLineWrapping, customWrappedLinesMarkingImage, customLineWrappingMarkingImage, markWrappedLines, C#, VB.NET, images] -->
```