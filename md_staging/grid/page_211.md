```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_211.jpeg
document_name: grid
page_number: 211
page_id: grid#page_211
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to add and customize a Calendar cell type in the Grid control using the RegisterCellModel class.
- Demonstrates setting the cell type to Calendar using code examples in C# and VB.NET.
- Illustrates the appearance of the Calendar cell with a visual figure.

## Content

### 4.1.4.4 Calendar

The Calendar cell type by can be added by registering the cell model by using the RegisterCellModel class.

The following code examples illustrate how to set the cell type to Calendar.

#### 1. Using C#

```csharp
GridStyleInfo style;
style = gridControl1[row, 2];
style.CellType = CustomCellTypes.Calendar.ToString();
style.Control = new MonthCalendar();
```

#### 2. Using VB.NET

```vb
Dim style As GridStyleInfo
style = gridControl1(row, 2)
style.CellType = CustomCellTypes.Calendar.ToString()
style.Control = New MonthCalendar()
```

### Figure 110: Calendar Cell

![Figure 110: Calendar Cell](#image)

The image shows a Calendar cell within a grid, displaying the month of April 2007. The current date is highlighted as the 4th, and the date "Heute: 4/4/2007" is indicated below the calendar.

## Cross References
- See also: RegisterCellModel, CustomCellTypes, MonthCalendar

<!-- tags: [Syncfusion, Grid, Calendar, Cell Type, WinForms] keywords: [Calendar Cell, RegisterCellModel, CustomCellTypes, MonthCalendar, Grid, Windows Forms, Code Examples] -->
```