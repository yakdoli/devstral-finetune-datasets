```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_425.jpeg
document_name: chart
page_number: 425
page_id: chart#page_425
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:02Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Stripline Properties

The following are the properties related to configuring a stripline in the chart control:

| Property      | Description                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------|
| Enabled       | Enables the Stripline.                                                                         |
| End           | Gets/sets the end range (in double) of the stripline. Use this if the axis range type is Double. Also see EndDate. |
| EndDate       | The end date of the stripline. Use this if the axis range type is DateTime. Also see End. |
| Font          | The Font style in which the stripline text, if any, will be rendered.                          |
| FixedWidth    | Specifies a fixed width for the chart stripline. Normally, the width of the stripline changes when the axis range changes. You can also set the width to be fixed irrespective of the AxisRange, by specifying a width in this property. After setting a fixed width, the stripline width will not vary beyond/less than the value that is set. |
| Interior      | Interior brush information for the stripline.                                                   |
| Offset        | Gets/sets the offset of the stripline if the chart's PrimaryX-axis is of type Double and StartAtAxisPosition is true. Also see DateOffset. |
| Period        | Gets/sets the period (width of the range) over which the stripline appears.                     |
| PeriodDate    | Gets/sets the period (time span) over which the stripline appears if the value is DateTime. |
| Start         | Gets/sets the start of the stripline. Also see End.                                            |
| StartAtAxisPosition | Indicates whether the Stripline will start at the start of the axis range.               |
| StartDate     | The start date of the stripline.                                                               |
| Text          | The text in the stripline.                                                                     |
| TextAlignment | Alignment of the text in the stripline.                                                        |
| TextColor     | The color of the text in the stripline.                                                        |
| Vertical      | Indicates whether stripline is rendered vertically.                                             |
| Width         | The width of the stripline.                                                                    |
| WidthDate     | Gets/sets the width of the stripline in a Time span.                                          |

### Drawing a Stripline with DateTime Values

The following is the code to draw a stripline from the x-axis with DateTime values.

```csharp
// Code example to draw a stripline with DateTime values
// (Implementation details would go here)
```

## Page-level Navigation/TOC (if applicable)

- Stripline Properties
- Drawing a Stripline with DateTime Values

## Cross References

See also:
- Chart Striplines
- DateTime Axis Configuration

<!-- tags: [Syncfusion Winforms, Control, Stripline, DateTime, Version 11.4.0.26] keywords: [Stripline, Chart, DateTime, Axis, Range, Font, FixedWidth, Interior, Offset, Period, Start, Alignment, Text, Color, Vertical, Width, DateOffset, AxisRange] -->
```