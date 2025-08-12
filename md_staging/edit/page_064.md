```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: edit
page_number: 064
page_id: edit#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:51Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Column Guides are used to highlight columns with special meaning, and Syncfusion's Essential Edit supports an unlimited number of column guides.
- Each column guide can be customized with a unique color and position.
- The `ShowColumnGuides` property is used to enable or disable the rendering of column guides in the Edit Control.
- Column guides' color and position are set using the `ColumnGuideItem Collection Editor`.

## Content

### Column Guides in Essential Edit
Column Guides are used to highlight columns with special meaning. Essential Edit supports an unlimited number of column guides.

Each column guide can be provided with a custom color and location. This can be done by setting the `ShowColumnGuides` property of the Edit Control to `True`, and then specifying the color and the location of the Column Guides using `ColumnGuideItem Collection Editor`. The font used to calculate the column location is customized by using the `ColumnGuidesMeasuringFont` property.

### Properties of the Edit Control

| Edit Control Property                  | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| **ShowColumnGuides**                   | Gets / sets value that indicates whether column guides should be drawn. |
| **ColumnGuideItems**                   | Gets / sets array of `ColumnGuideItem` objects.                          |
| **ColumnGuidesMeasuringFont**          | Gets / sets font that is used while measuring the position of the column guides. |

### Code Example in C#
```csharp
[C#]

// Enable Column Guides.
this.editControl1.ShowColumnGuides = true;

// Specify the color and the location of the Column Guides.
ColumnGuideItem[] columnGuideItem = new ColumnGuideItem[2];
columnGuideItem[0] = new ColumnGuideItem(20, Color.Yellow);
columnGuideItem[1] = new ColumnGuideItem(40, Color.IndianRed);
this.editControl1.ColumnGuideItems = columnGuideItem;

// Font used to calculate the column location.
this.editControl1.ColumnGuidesMeasuringFont = new Font("Microsoft Sans Serif", 12);
```

### Code Example in VB.NET
```vbnet
[VB.NET]

' Enable Column Guides.
Me.editControl1.ShowColumnGuides = True

' Specify the color and the location of the Column Guides.
Dim columnGuideItem() As ColumnGuideItem = New ColumnGuideItem(2)
columnGuideItem(0) = New ColumnGuideItem(20, Color.Yellow)
columnGuideItem(1) = New ColumnGuideItem(40, Color.IndianRed)
Me.editControl1.ColumnGuideItems = columnGuideItem

' Font used to calculate the column location.
```

### Summary

This section details how to use column guides in the Essential Edit Control for Windows Forms. It covers enabling column guides, setting their appearance and position, and specifying the font used for calculating column guide positions.

<!-- tags: [Syncfusion, Windows Forms, Edit Control, Column Guides] keywords: [Edit Control, Column Guides, ShowColumnGuides, ColumnGuideItems, ColumnGuidesMeasuringFont] -->
```