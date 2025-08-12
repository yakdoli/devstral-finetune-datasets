```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: diagram
page_number: 168
page_id: diagram#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:54Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates line styles in Windows Forms.
- Explains how to customize connection points and set their sizes.

## Content

### Figure 101: Line Style
#### C#
```csharp
m_styleLine = new LineStyle();
m_styleLine.LineColor = Color.Blue;
m_styleLine.LineWidth = 0;
m_styleLine.DashStyle = DashStyle.Dash;
```

#### VB
```vb
m_styleLine = New LineStyle()
m_styleLine.LineColor = Color.Blue
m_styleLine.LineWidth = 0
m_styleLine.DashStyle = DashStyle.Dash
```

The below images illustrate the above settings.

#### Figure 102: Customized Connection Point
![Customized Connection Point](attachment:custom_connection_point)

### ConnectionPointSize

This property allows us to set the size of the Ports for the current ConnectionPoint. This property accepts a ConnectionPointSize enumerator, which has three predefined sizes as follows:

- Large (12 * 12)
- Medium (9 * 9)
- Small (6 * 6)

### Position

## API Reference (if applicable)

### ConnectionPointSize Enumeration
- **Large**: 12 * 12
- **Medium**: 9 * 9
- **Small**: 6 * 6

## Code Examples

#### Customized Connection Point Example
```csharp
// Example code to demonstrate customizing connection points
ConnectionPointSize size = ConnectionPointSize.Medium;
// Use the ConnectionPointSize in a suitable context
```

## Tags and Keywords
<!-- tags: Syncfusion Winforms, Diagram, Connection Point, Line Style, Position keywords: ConnectionPointSize, LineStyle, DashStyle, Windows Forms, Custom Connection Points -->
```