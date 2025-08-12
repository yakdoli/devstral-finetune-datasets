```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_114.jpeg
document_name: edit
page_number: 114
page_id: edit#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:10Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

```vb
Me.editControl1.WordWrapMarginLineStyle = System.Drawing.Drawing2D.DashStyle.Dash

// Specifies the line color of the wordwrap margin.
Me.editControl1.WordWrapMarginLineColor = System.Drawing.Color.Green

// Specifies the BrushInfo object that is used when the area situated after
// the text area is drawn.
Me.editControl1.WordWrapMarginBrush = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal, System.Drawing.Color.White, System.Drawing.Color.LightSalmon)
```

![Edit Control with Character Wrapping and Custom Painted Wordwrap Margin](image1.png)

Figure 37: Edit Control with Character Wrapping and Custom Painted Wordwrap Margin

### Line Wrapping Images

It is also possible to associate images to indicate line wrapping. This feature can be turned on by setting the `MarkLineWrapping` property to `True`. There can be two types of image indicators:

1. Images that indicate the line that is being wrapped. These are displayed at the beginning of the line being wrapped. This can be set by using the `CustomWrappedLinesMarkingImage` property.

## Page-level Navigation/TOC (if applicable)

- Essential Edit for Windows Forms

### Related Sections

- [Previous Section](#)
- [Next Section](#)

<!-- tags: [Syncfusion Winforms, WordWrap, LineWrapping, EditControl, LineStyling] keywords: [wordwrap margin, gradient style, brush info, line indication, image association, custom painting, wrapped lines] -->
```