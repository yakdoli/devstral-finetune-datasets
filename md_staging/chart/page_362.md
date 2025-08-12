```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_362.jpeg
document_name: chart
page_number: 362
page_id: chart#page_362
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:31Z
fidelity: lossless
-->

## Chart Control Documentation

### Overview
- Detailed documentation on the `XType` property in `Syncfusion.Windows.Forms.Chart` controls.
- Explanation of the `XType` property settings, possible values, and sample code snippets in both C# and VB.NET.
- Describes how to retrieve and display the x-value type of any chart series programmatically.

## Content

### 4.5.1.91 XType

#### Description
Returns the x-value type that is being rendered. It is a read-only property.

#### Details

| **Property**           | **Description**                                                                 |
|------------------------|--------------------------------------------------------------------------------|
| **Possible Values**    | - **Double** - Specifies Double values <br> - **DateTime** - Specifies Date and Time values <br> - **Logarithmic** - Specifies Logarithmic values <br> - **Custom** - Specifies Custom values |
| **Default Value**      | Double                                                                 |
| **2D / 3D Limitations** | No                                                                      |
| **Applies to Chart Element** | Any Series                                                             |
| **Applies to Chart Types** | All Chart Types                                                         |

#### Sample Code Snippet

Here is sample code snippet using `XType`.

- **C#**
  
```csharp
autoLabel1.Text = this.chartControl1.Series[0].XType.ToString();
```

- **VB.NET**
  
```vb
Private autoLabel1.Text = Me.chartControl1.Series(0).XType.ToString()
```

## Cross References
- `Pie Chart`

## API Reference

### Properties
- **XType**
  - **Description**: Returns the x-value type of the rendered chart series.
  - **Type**: Read-only property.
  - **Possible Values**:
    - **Double**: Specifies Double values.
    - **DateTime**: Specifies Date and Time values.
    - **Logarithmic**: Specifies Logarithmic values.
    - **Custom**: Specifies Custom values.
  - **Default Value**: Double
  - **Applies to**:
    - **Chart Element**: Any Series.
    - **Chart Types**: All Chart Types.

## Code Examples

### Example 1: Displaying XType Value
```csharp
// C#
autoLabel1.Text = this.chartControl1.Series[0].XType.ToString();
```

```vb
' VB.NET
Private autoLabel1.Text = Me.chartControl1.Series(0).XType.ToString()
```

<!-- tags: [syncfusion, windowsforms, chart, xtype, property, api, version: 11.4.0.26] keywords: [xtype, read-only, chart series, double, datetime, logarithmic, custom, chart control, chart elements, all chart types, programmatically retrieve, csharp, vb.net, sample code, data types] -->
```