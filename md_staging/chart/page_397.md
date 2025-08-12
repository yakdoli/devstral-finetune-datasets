```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_397.jpeg
document_name: chart
page_number: 397
page_id: chart#page_397
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section discusses the customization of axis labels in the Essential Chart for Windows Forms.
- Covers topics related to formatting, appearance, and positioning of axis labels.
- Provides a list of properties that can be used to enhance these aspects.

## Content

### 4.6.8 Axis Labels

This section talks about the customization of axis labels in the following topics:

#### 4.6.8.1 Axis Label Text Formatting, Appearance and Positioning

By default, the label texts are automatically determined based on the axis data points and the generated intervals. You can better the format, look, and positioning of the labels using the properties listed below.

| ChartAxis Property | Description |
| --- | --- |
| Format | If the data points are double values, then use this property to specify the format in which to render the double value. The specified format will be used in the Double.ToString method to arrive at the formatted string. Search MSDN documentation for Standard Numeric Format Strings for more information on the format strings. |
| DateTimeFormat | If the data points are DateTime values, then use this property to specify the format in which to render the date. The specified format will be used in the DateTime.ToString() method to arrive at the formatted string. Search MSDN documentation for Date and Time Format Strings for more information on the format strings. |
| ForeColor | Affects the labels and other text colors that get rendered in the axis. |
| Font | Specifies the font to use for label and other texts that get rendered in the axis. By default, it is set to Trebuchet, 9, regular. |
| ScaleLabels | Setting this to `true` will automatically resize the text if the chart size is expanded by the user. |
| LabelAlignment | Specifies if the label should be rendered Near, Far, or Center within the available area. Default is Center. |
| LabelRotate | Specifies whether or not labels should be rotated. Use the LabelRotateAngle to specify the angle. |

## API Reference (if applicable)
- The listed properties (Format, DateTimeFormat, ForeColor, etc.) are part of the ChartAxis class of the Syncfusion Windows Forms Chart control.

## Code Examples (multi-language supported)
- No code examples are provided in this section. However, these properties can be used in C# or other compatible code examples to customize chart axis labels.

## Page-level Navigation/TOC (if applicable)
- This section is part of a larger document, and no explicit local TOC is provided for this page.

## Cross References
- See also: Additional chart customization options for further enhancements.

<!-- tags: [chart, labels, formatting, appearance, position, axis, winforms, Essential] keywords: [format, datetime format, font, forecolor, scale labels, label alignment, label rotate] -->
```