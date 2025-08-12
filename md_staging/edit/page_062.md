```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: edit
page_number: 062
page_id: edit#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:42Z
fidelity: lossless
-->

## Coordinate Conversion Methods

### Overview
- Converts logical coordinates (virtual point) to physical coordinates using C# and VB.NET samples.
- Demonstrates bidirectional conversion between physical and virtual coordinates.
- Includes offset calculations for precise positioning.

### WinForms Coordinate Conversion in C#

```csharp
Point virtualPosition = 
this.editControl1.ConvertOffsetToVirtualPosition(offset);

// Converts point in virtual coordinates to coordinate point.
this.editControl1.ConvertVirtualPointToCoordinatePoint(int Column, int line);
```

### WinForms Coordinate Conversion in VB.NET

```vb
' Convert coordinates associated with mouse position to virtual coordinates.
Dim virtualPosition As Point = 
Me.editControl1.PointToVirtualPosition(Control.MousePosition)

' Converts coordinates associated with mouse position to physical coordinates.
Dim physicalPosition As Point = 
Me.editControl1.PointToPhysicalPosition(Control.MousePosition)

' Converts virtual coordinates to physical coordinates.
Dim physicalPosition As Point = 
Me.editControl1.ConvertVirtualPositionToPhysical(virtualPosition)

' Converts virtual coordinates to offset value.
Dim offset As Long = 
Me.editControl1.ConvertVirtualPositionToOffset(virtualPosition)

' Converts the offset value to virtual coordinates.
Dim virtualPosition As Point = 
Me.editControl1.ConvertOffsetToVirtualPosition(offset)

' Converts point in virtual coordinates to coordinate point.
Me.editControl1.ConvertVirtualPointToCoordinatePoint(Integer Column, Integer line)
```

---

<!-- tags: [WinForms, coordinate conversion, virtual coordinates, physical coordinates, offset calculations, C#, VB.NET] keywords: [editControl1, PointToVirtualPosition, PointToPhysicalPosition, ConvertVirtualPositionToPhysical, ConvertVirtualPositionToOffset, ConvertOffsetToVirtualPosition, ConvertVirtualPointToCoordinatePoint] -->
```