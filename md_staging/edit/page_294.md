```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_294.jpeg
document_name: edit
page_number: 294
page_id: edit#page_294
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:12:08Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to underline text using the essential edit control.
- Registers a new underline format and applies it to a specified text range within the control.
- Includes both C# and VB.NET code examples.

## Content

This section explains the process of underlining text in the essential edit control. The following steps illustrate how to convert offset values to virtual points, parse points, and coordinate points, and then apply a custom underline format to the specified text range.

### C#

```csharp
// Starting offset converted to virtual point
Point startVirtualPoint = this.editControl1.ConvertOffsetToVirtualPosition(startOffsetValue);

// Ending offset converted to virtual point
Point endVirtualPoint = this.editControl1.ConvertOffsetToVirtualPosition(endOffsetValue);

// Converting the VirtualPoints to ParsePoints
ParsePoint startParsePoint = new ParsePoint(startVirtualPoint.Y, startVirtualPoint.X, 0);
ParsePoint endParsePoint = new ParsePoint(endVirtualPoint.Y, endVirtualPoint.X, 0);

// Creating the associated CoordinatePoints that indicate the text range
CoordinatePoint startCoordinatePoint = new CoordinatePoint((ILexemParser)this.editControl1.Parser, startParsePoint, startVirtualPoint.Y, startVirtualPoint.X, true);
CoordinatePoint endCoordinatePoint = new CoordinatePoint((ILexemParser)this.editControl1.Parser, endParsePoint, endVirtualPoint.Y, endVirtualPoint.X, true);

ISnippetFormat format = editControl1.RegisterUnderlineFormat(Color.Red, UnderlineStyle.Wave, UnderlineWeight.Thick);
this.editControl1.SetUnderline(startCoordinatePoint, endCoordinatePoint, format);
```

### VB.NET

```vb
' Starting offset converted to virtual point
Dim startVirtualPoint As Point = Me.editControl1.ConvertOffsetToVirtualPosition(startOffsetValue)

' Ending offset converted to virtual point
Dim endVirtualPoint As Point = Me.editControl1.ConvertOffsetToVirtualPosition(endOffsetValue)

' Converting the VirtualPoints to ParsePoints
Dim startParsePoint As New ParsePoint(startVirtualPoint.Y, startVirtualPoint.X, 0)
Dim endParsePoint As New ParsePoint(endVirtualPoint.Y, endVirtualPoint.X, 0)

' Creating the associated CoordinatePoints that indicate the text range
Dim startCoordinatePoint As New CoordinatePoint(CType(Me.editControl1.Parser, ILexemParser), startParsePoint, startVirtualPoint.Y, startVirtualPoint.X, True)
Dim endCoordinatePoint As New CoordinatePoint(CType(Me.editControl1.Parser, ILexemParser), endParsePoint, endVirtualPoint.Y, endVirtualPoint.X, True)
```

<!-- tags: [Syncfusion, Windows Forms, Essential Edit, Underline, Format, Coordinate Points, Text Range] keywords: [Underline, Text Seed, Offset, Virtual Point, Parse Points, Coordinate Points, Essential Edit, Windows Forms] -->
```