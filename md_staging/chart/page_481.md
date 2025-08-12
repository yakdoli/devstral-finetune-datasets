```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_481.jpeg
document_name: chart
page_number: 481
page_id: chart#page_481
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:24Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```vb.net
cursor1 = New ChartInteractiveCursor(Me.chartControl1.Series(0))
Me.chartControl1.ChartArea.InteractiveCursors.Add(cursor1)
cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal
cursor1.HorizontalCursorColor = Color.Red
```

The interactive cursor as described earlier can be set in three different orientations.  

To draw the interactive cursor in horizontal orientation, you need to set the cursor orientation to "Horizontal" as shown in the following code snippets:

### Setting Horizontal Orientation

#### [C# .NET]
```csharp
cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal;
```

#### [VB.NET]
```vb.net
cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal
```

The same step is repeated for "vertical" and "both" cursor orientations except for the naming "Vertical" and "Both" respectively.

### Customizing Cursor Colors

You can also add color(s) to individual interactive cursor. The default color (base color) is Red. You can change the default color by using `Color`, `HorizontalCursorColor`, and `VerticalCursorColor` properties. When you use the `Color` property, the interactive cursor will be drawn based on the color specified by the `Color` property (assuming this as base/parent color) regardless of the colors specified for `Horizontal` and `Vertical` cursor orientations. This is shown in the following code snippets:

#### [C# .NET]
```csharp
cursor1.CursorOrientation = InteractiveCursorOrientation.Both;
cursor1.Color = Color.Blue;
```

## API Reference

### Properties

- `CursorOrientation`: Determines the orientation of the interactive cursor.  
  - Type: `InteractiveCursorOrientation`
  - Possible values: `Horizontal`, `Vertical`, `Both`

- `Color`: Specifies the base color for the interactive cursor.  
  - Type: `Color`

- `HorizontalCursorColor`: Specifies the color for the horizontal cursor.  
  - Type: `Color`

- `VerticalCursorColor`: Specifies the color for the vertical cursor.  
  - Type: `Color`

### Methods

None

### Events

None

## Code Examples

#### Adding a Horizontal Interactive Cursor

#### [C# .NET]
```csharp
ChartInteractiveCursor cursor1 = new ChartInteractiveCursor(chartControl1.Series[0]);
chartControl1.ChartArea.InteractiveCursors.Add(cursor1);
cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal;
cursor1.HorizontalCursorColor = Color.Red;
```

#### [VB.NET]
```vb.net
Dim cursor1 As New ChartInteractiveCursor(Me.chartControl1.Series(0))
Me.chartControl1.ChartArea.InteractiveCursors.Add(cursor1)
cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal
cursor1.HorizontalCursorColor = Color.Red
```

#### Adding Both Horizontal and Vertical Interactive Cursors with Custom Color

#### [C# .NET]
```csharp
ChartInteractiveCursor cursor1 = new ChartInteractiveCursor(chartControl1.Series[0]);
chartControl1.ChartArea.InteractiveCursors.Add(cursor1);
cursor1.CursorOrientation = InteractiveCursorOrientation.Both;
cursor1.Color = Color.Blue;
```

## Summary

The documentation covers how to configure and customize interactive cursors in Syncfusion Chart for Windows Forms. It explains setting orientations and colors for the interactive cursor, providing examples in both C# .NET and VB.NET.

<!-- tags: [chart, windowsforms, interactivecursor, cursororientation, interactivecursors, horizontal, vertical, both, color, horizontalcursorcolor, verticalcursorcolor] keywords: [interactive cursor, chart, windows forms, cursor orientation, horizontal, vertical, both, color] -->
```