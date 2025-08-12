```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: diagram
page_number: 127
page_id: diagram#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:55Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Lists various properties for adjusting and formatting text labels in Windows Forms.
- Includes functionality to control text alignment, rotation, wrapping, and direction.
- Provides options to handle text case, formatting, and positioning.

## Content

### Control Properties and Settings

The following table details the properties and their descriptions:

| Property              | Description                                                                 | Default | Type           | Remarks |
|----------------------|-----------------------------------------------------------------------------|---------|----------------|---------|
| UpdatePosition       | Gets or Sets whether default positioning has to be used.                 | NA      | Boolean        | NA      |
| AdjustRotationAngle  | Gets or Sets whether the label should remain horizontal on rotation of the node. | NA      | Boolean        | NA      |
| TextCase             | Gets or sets the case of the text in the label.                          | NA      | TextCases      | NA      |
| HorizontalAlignment  | Gets or sets the horizontal alignment of the text.                      | NA      | StringAlignment| NA      |
| VerticalAlignment    | Gets or sets the vertical alignment of the text.                        | NA      | StringAlignment| NA      |
| FormatFlags          | Gets the flags used to format the text.                                | NA      | StringFormatFlags| NA      |
| WrapText             | Gets or sets a value indicating whether text should be wrapped, when it exceeds the width of the bounding box. | NA      | Boolean        | NA      |
| DirectionRightToLeft | Gets or sets a value indicating whether the text is right to left.      | NA      | Boolean        | NA      |
| DirectionVertical    | Gets or sets a value indicating whether the text is vertical.          | NA      | Boolean        | NA      |

### Example Usage

Here is a sample usage of some of these properties in C#:

```csharp
// Creating a label control
var label = new Label();

// Adjust text alignment
label.HorizontalAlignment = StringAlignment.Center;

// Enable text wrapping
label.WrapText = true;

// Check if the text should be formatted for right-to-left languages
label.DirectionRightToLeft = true;

// Control text case
label.TextCase = TextCases.UpperCase;
```

### API Reference

#### Namespace: Syncfusion.Windows.Forms.Controls
- Class: `Label`
  - Properties:
    - `UpdatePosition`: Boolean
    - `AdjustRotationAngle`: Boolean
    - `TextCase`: TextCases
    - `HorizontalAlignment`: StringAlignment
    - `VerticalAlignment`: StringAlignment
    - `FormatFlags`: StringFormatFlags
    - `WrapText`: Boolean
    - `DirectionRightToLeft`: Boolean
    - `DirectionVertical`: Boolean

### Code Examples

#### Adjusting Text Alignment

```csharp
public void AdjustTextAlignment(Label label, StringAlignment alignment)
{
    label.HorizontalAlignment = alignment;
}

// Example usage
Label myLabel = new Label();
AdjustTextAlignment(myLabel, StringAlignment.Far);
```

#### Handling Text Direction

```csharp
public void SetTextDirection(Label label, bool isVertical)
{
    label.DirectionVertical = isVertical;
}

// Example usage
Label verticalLabel = new Label();
SetTextDirection(verticalLabel, true);
```

### Cross References
- See also: [Formatting Text in Diagram Controls]
- See also: [Properties and Methods Overview]

## RAG Annotations
<!-- tags: [winforms, diagram, label, text formatting, alignment, rotation, text direction, text alignment] keywords: [UpdatePosition, AdjustRotationAngle, TextCase, HorizontalAlignment, VerticalAlignment, FormatFlags, WrapText, DirectionRightToLeft, DirectionVertical] -->
```