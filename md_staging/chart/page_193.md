```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_193.jpeg
document_name: chart
page_number: 193
page_id: chart#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:40Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- **Daily Performance Chart**: Displays task completion percentages across daily reviews.
- **Column Chart Customization**: Demonstrates setting ColumnFixedWidth for consistent bar sizes.
- **ColumnType Property**: Explains how to specify rendering as bars or cylinders.

## Content

### Daily Performance Chart

The image below illustrates a `ColumnChart` with a fixed width of 45 units for each column.

![Daily Performance ColumnChart](#)

**Figure 106: ColumnChart with ColumnFixedWidth = "45"**

#### See Also
- `Column charts`
- `BoxAndWhiskerChart`
- `ColumnWidthMode`
- `Candle Charts`

### 4.5.1.7 ColumnType

#### Overview
Specifies whether the columns should be rendered as bars or cylinders.

#### Details

| **Attribute**            | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Possible Values**       | - `Box`: Renders the columns as boxes.<br>- `Cylinder`: Renders the columns as cylinders. |
| **Default Value**         | `Box`                                                                          |
| **2D / 3D Limitations**  | 3D only                                                                        |
| **Applies to Chart Element** | All series                                                                   |

## API Reference

### ColumnType Property

#### Summary
Configures the rendering style of chart columns as either bars or cylinders.

#### Parameters

| Name              | Type                  | Description                                                                 | Default      | Required |
|-------------------|-----------------------|-----------------------------------------------------------------------------|--------------|----------|
| ColumnType        | `string`              | Specifies the type of column to render.<br>Possible values: `Box` or `Cylinder`. | `Box`        | Yes      |

#### Returns
- `void`: Configures the column rendering style.

#### Exceptions
- None.

## Code Examples

### Example: Setting ColumnType to Cylinder

```csharp
// Assuming 'chart' is a reference to the Chart control
chart.Series[0].ColumnType = ChartColumnType.Cylinder;
```

## Page-level Navigation/TOC

- **4.5.1.7 ColumnType**
  - Overview
  - Details

## Cross References

#### See Also
- `Column charts`
- `BoxAndWhiskerChart`
- `ColumnWidthMode`
- `Candle Charts`

<!-- tags: [chart, columnchart, windowsforms, syncfusion] keywords: [columnchart, dailyreview, columnwidth, columnfixedwidth, columntype, cylinder, box, 3dchart, series, performance, taskcompletion] -->
```