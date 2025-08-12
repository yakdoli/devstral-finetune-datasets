```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_283.jpeg
document_name: edit
page_number: 283
page_id: edit#page_283
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:48Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## 5.4 How To Convert Offset Values Into Text Range In the Edit Control

This section explains how to get the associated CoordinatePoint values from text offset values. This can be done as follows.

You have to convert offset values into VirtualPoints, and then VirtualPoints to ParsePoints before converting them to CoordinatePoints.

The following code snippet illustrates this:

### C# Code Example

```csharp
// Starting offset converted to virtual point.
Point startVirtualPoint = 
    this.editControl1.ConvertOffsetToVirtualPosition(startOffsetValue);

// Ending offset converted to virtual point.
Point endVirtualPoint = 
    this.editControl1.ConvertOffsetToVirtualPosition(endOffsetValue);

// Converting the VirtualPoints to ParsePoints.
ParsePoint startParsePoint = new ParsePoint(startVirtualPoint.Y, 
    startVirtualPoint.X, 0);
ParsePoint endParsePoint = new ParsePoint(endVirtualPoint.Y, 
    endVirtualPoint.X, 0);

// Creating the associated CoordinatePoints that indicate the text range.
CoordinatePoint startCoordinatePoint = new CoordinatePoint(
    this.editControl1.Parser as ILexemParser, 
    startParsePoint, 
    startVirtualPoint.Y, 
    startVirtualPoint.X, 
    true);
CoordinatePoint endCoordinatePoint = new CoordinatePoint(
    this.editControl1.Parser as ILexemParser, 
    endParsePoint, 
    endVirtualPoint.Y, 
    endVirtualPoint.X, 
    true);
```

### VB.NET Code Example

```vb
' Starting offset converted to virtual point.
Dim startVirtualPoint As Point = 
    Me.EditControl1.ConvertOffsetToVirtualPosition(startOffsetValue)

' Ending offset converted to virtual point.
Dim endVirtualPoint As Point = 
    Me.EditControl1.ConvertOffsetToVirtualPosition(endOffsetValue)
```
```html
<!-- tags: [Syncfusion Winforms, Edit Control] keywords: [offset values, VirtualPoints, ParsePoints, CoordinatePoints, text range, conversion] -->
```