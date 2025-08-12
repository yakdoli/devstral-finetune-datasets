```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_118.jpeg
document_name: edit
page_number: 118
page_id: edit#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:22Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Customizing text within the Edit Control.
- Exploring methods to alter text color and text borders.
- Detailed examples in C# and VB.NET.

## Content

### 4.4.12 Customizing Text

The following text customization features are discussed in this section:

#### 4.4.12.1 Text Color

This section discusses how the text color of the Edit Control can be changed.

The text color of the Edit Control is set by using the `SetTextColor` method.

```csharp
// Set the color of the text for the Edit Control.
this.editControl1.SetTextColor(new Point(1, 1), new Point(5, 5), Color.Orange);
```

```vb.net
' Set the color of the text for the Edit Control.
Me.editControl1.SetTextColor(New Point(1, 1), New Point(5, 5), Color.Orange)
```

#### 4.4.12.2 Text Border

This section discusses how borders can be set for the text in the Edit Control.

Edit Control supports borders for its text by using the methods given below.

| Edit Control Method      | Description                              |
|--------------------------|------------------------------------------|
| `SetTextBorder`         | Sets border around text.                |
| `RemoveTextBorder`      | Removes border around text with given coordinates. |

## API Reference

### Methods

#### `SetTextColor`
- **Parameters**: 
  - `startPoint` (Point): Starting point of the text range.
  - `endPoint` (Point): Ending point of the text range.
  - `color` (Color): Color to set for the text.
  
#### `SetTextBorder`
- **Description**: Sets a border around the text.

#### `RemoveTextBorder`
- **Parameters**: 
  - `startPoint` (Point): Starting point of the text range.
  - `endPoint` (Point): Ending point of the text range.
  
## Code Examples

### C#
```csharp
// Example: Setting text color for a specific range.
this.editControl1.SetTextColor(new Point(1, 1), new Point(5, 5), Color.Orange);
```

### VB.NET
```vb.net
' Example: Setting text color for a specific range.
Me.editControl1.SetTextColor(New Point(1, 1), New Point(5, 5), Color.Orange)
```

## Page-level Navigation/TOC

- 4.4.12 Customizing Text
  - 4.4.12.1 Text Color
  - 4.4.12.2 Text Border

<!-- tags: [Syncfusion, WindowsForms, EditControl, TextColor, TextBorder] keywords: [SetTextColor, RemoveTextBorder, Point, Color] -->
```