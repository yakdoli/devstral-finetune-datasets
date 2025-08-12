```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_393.jpeg
document_name: chart
page_number: 393
page_id: chart#page_393
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

| Setting         | Supported Modes         | Supported Types | Description                                                                                                          | Default Value |
|------------------|--------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------|---------------|
| N/A             | N/A                      | N/A             | "ForceZero" setting instead. Default value is true.                                                                 | true          |
| ForceZero       | Auto                     | Double          | Indicates whether one boundary of the calculated range should always be tweaked to zero. Default value is true. | true          |
| CustomOrigin    | Auto and Set             | Double, DateTime | Lets you use the properties Origin and OriginDate below. Default value is false.                                    | false         |
| Origin          | Auto and Set             | Double          | Lets you specify a custom origin (double value) for the axis. Use this property when the data points are of double type. The interval and range will then be calculated automatically. Remember to set CustomOrigin to true. Default value is 0.0. | 0.0           |
| OriginDate      | Auto and Set             | DateTime        | Lets you specify a custom origin (double value) for the axis. Use this property when the data points are of double type. The interval and range will then be calculated automatically. Remember to set CustomOrigin to true. Default value is DateTime.MinValue. | DateTime.MinValue |
| Offset          | Auto and Set             | Double and DateTime | Specifies the offset that should be applied to the automatically calculated start of the range.                 | N/A           |
| OffsetDateTime  | Auto                     | DateTime        | Specifies the offset that should be applied to the automatically calculated start of the range.                 | N/A           |
| DateTimeInterval.Offs| Set                     | DateTime        | Use this instead of Offset if                                                                  | N/A           |

## API Reference

- **Properties:**
  - **ForceZero:** Indicate whether one boundary of the calculated range should always be tweaked to zero. (Default: true)
  - **CustomOrigin:** Enable the use of the Origin and OriginDate properties. (Default: false)
  - **Origin:** Specify a custom origin (double value) for the axis, applicable to double-type data points. (Default: 0.0)
  - **OriginDate:** Specify a custom origin (DateTime value) for the axis, applicable to DateTime-type data points. (Default: DateTime.MinValue)
  - **Offset:** Apply an offset to the automatically calculated start of the range.
  - **OffsetDateTime:** Apply an offset to the automatically calculated start of the range, applicable to DateTime-type data points.

## Code Examples

### Example: Setting Custom Origin

```csharp
chart1.PrimaryXAxis.CustomOrigin = true;
chart1.PrimaryXAxis.Origin = 5.0;
```

### Example: Using Offset

```csharp
chart1.PrimaryYAxis.Offset = 3.0;
```

## RAG Annotations

<!--
tags: [Syncfusion Winforms, Chart, Axis Settings, Customize Axis]
keywords: [ForceZero, CustomOrigin, Origin, OriginDate, Offset, OffsetDateTime, DateTimeInterval]
-->

```