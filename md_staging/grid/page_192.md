```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: grid
page_number: 192
page_id: grid#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:01Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Text Color

The text color can be changed for the grid cells dynamically by setting the `TextColor` property of individual cells.

#### Using C#

```csharp
gridControl[ rowIndex,  colIndex ].TextColor = Color.Red;
```

#### Using VB.NET

```vbnet
gridControl( rowIndex,  colIndex ).TextColor = color.Red
```

### Border

The border for a cell can be customized by setting the `Border` property to an instance of `GridBorder`. The `GridBorder` class contains the formatting details for borders of the cell.

#### Using C#

```csharp
gridControl[ rowIndex,  colIndex ].Borders.All = new
GridBorder( GridBorderStyle.DashDotDot, Color.Red );
```

#### Using VB.NET

```vbnet
gridControl( rowIndex,  colIndex ).Borders.All = New
GridBorder( GridBorderStyle.DashDotDot, color.Red )
```

### Orientation

The orientation of the grid cell text can be specified, thus controlling the angle at which the text is displayed.

#### Using C#

```csharp
gridControl[3,  4].Font.Orientation = 270;
```

#### Using VB.NET

```vbnet
gridControl(3,  4).Font.Orientation = 270
```

This section outlines how to modify the appearance of grid cells in the Syncfusion Windows Forms Grid control by adjusting text color, border, and orientation settings dynamically.
```