```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_483.jpeg
document_name: chart
page_number: 483
page_id: chart#page_483
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:27Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to configure interactive cursor orientation, vertical cursor color, and horizontal cursor color in a Windows Forms Chart control.
- Provides examples in both C# and VB.NET for customizing the cursor properties.

## Content

### Configuring Cursor Properties

The following code snippets show how to set the orientation and colors of the interactive cursor in a Chart control.

#### C# Code Example
```csharp
cursor1.CursorOrientation = InteractiveCursorOrientation.Both ;
cursor1.VerticalCursorColor = Color.Green;
cursor1.HorizontalCursorColor = Color.Red;
```

#### VB.NET Code Example
```vb
cursor1.CursorOrientation = InteractiveCursorOrientation.Both
cursor1.VerticalCursorColor = Color.Green
cursor1.HorizontalCursorColor = Color.Red
```

### Example Chart with Interactive Cursor

The image below illustrates a Chart control with an interactive cursor. The cursor allows users to click on the line and drag it to different series points. The chart displays product sales per month over an 18-month period.

**Figure: Chart with Interactive Cursor**
- **Title:** Product Sales per Month
- **Axes:**
  - **X-axis:** Months (2 through 18)
  - **Y-axis:** Sales (Range 200 to 500)
- **Data Points:**
  - 382 at Month 2
  - 321 at Month 4
  - 425 at Month 6
  - 382 at Month 8
  - 437 at Month 10
  - 490 at Month 12
  - 422 at Month 14
  - 185 at Month 16
  - 461 at Month 18
- **Interactive Cursor Features:**
  - The cursor orientation is set to `Both`, enabling both horizontal and vertical lines.
  - The vertical cursor is colored green.
  - The horizontal cursor is colored red.
  - Users can interact with the cursor by clicking and dragging it to different data points.

## API Reference

### Namespace: Syncfusion.Windows.Forms.Chart

#### Properties
- **CursorOrientation:**
  - Type: `InteractiveCursorOrientation`
  - Default: `InteractiveCursorOrientation.Both`
  - Description: Specifies the orientation of the interactive cursor.
- **VerticalCursorColor:**
  - Type: `Color`
  - Default: `Color.Black`
  - Description: Sets the color of the vertical cursor line.
- **HorizontalCursorColor:**
  - Type: `Color`
  - Default: `Color.Black`
  - Description: Sets the color of the horizontal cursor line.

## Code Examples

The code snippets provided in both C# and VB.NET demonstrate how to configure the interactive cursor properties in a Chart control.

### C# Example
```csharp
// Assuming 'cursor1' is an instance of the cursor element in the Chart
cursor1.CursorOrientation = InteractiveCursorOrientation.Both;
cursor1.VerticalCursorColor = Color.Green;
cursor1.HorizontalCursorColor = Color.Red;
```

### VB.NET Example
```vb
' Assuming 'cursor1' is an instance of the cursor element in the Chart
cursor1.CursorOrientation = InteractiveCursorOrientation.Both
cursor1.VerticalCursorColor = Color.Green
cursor1.HorizontalCursorColor = Color.Red
```

## Tags and Keywords
<!-- tags: [Essential Chart, Windows Forms, Interactive Cursor, Cursor Orientation, Vertical Cursor Color, Horizontal Cursor Color] keywords: [Syncfusion, C#, VB.NET, Windows Forms Chart, InteractiveCursorOrientation, Color] -->
```