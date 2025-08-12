```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_966.jpeg
document_name: tools
page_number: 966
page_id: tools#page_966
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the various properties and styles related to borders in Windows Forms.
- Describes options such as `Etched`, `Bump`, `Sunken`, `Adjust`, and `Flat` for `BorderStyles`.
- Details border colors and styles like `Dotted`, `Dashed`, `Solid`, `Inset`, `Outset`, and `None`.
- Covers the `BorderColor`, `BorderSingle`, `BorderStyle`, and `HotBorderColor` properties.

## Content

| Property         | Description                                                                                                                                                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BorderStyle      | Indicates the specific border style. The options included are as follows: <br> `Etched`, `Bump`, `Sunken`, `Adjust`, and `Flat`. <br> The default value is set to 'Sunken'. |
| BorderColor      | Specifies the color of the 2D border.                                                                                                                                                                                                  |
| BorderSingle     | Indicates the 2D border style. The options included are as follows: <br> `Dotted`, `Dashed`, `Solid`, `Inset`, `Outset`, and `None`. <br> The BorderStyle property should be set to `FixedSingle`. |
| BorderStyle      | Indicates whether the panel should have a border. The options included are given below: <br> `FixedSingle`, `Fixed3D`, and `None`.                                                                                                    |
| HotBorderColor   | Specifies the color of the FixedSingle border when MouseOver.                                                                                                                                                                         |

## Code Examples

```csharp
[C#]
```

## API Reference

### BorderStyle Property
- `Namespace`: Syncfusion.Windows.Forms.Tools
- `Type`: Enumeration
- **Options**:
  - `Etched`
  - `Bump`
  - `Sunken`
  - `Adjust`
  - `Flat`
- **Default Value**: `Sunken`

### BorderColor Property
- `Namespace`: Syncfusion.Windows.Forms.Tools
- `Type`: System.Drawing.Color
- **Description**: Specifies the color of the 2D border.

### BorderSingle Property
- `Namespace`: Syncfusion.Windows.Forms.Tools
- `Type`: System.Drawing.Drawing2D.DashStyle
- **Options**:
  - `Dotted`
  - `Dashed`
  - `Solid`
  - `Inset`
  - `Outset`
  - `None`
- **Default Setting**: `FixedSingle`

### HotBorderColor Property
- `Namespace`: Syncfusion.Windows.Forms.Tools
- `Type`: System.Drawing.Color
- **Description**: Specifies the color of the FixedSingle border when the mouse is over it.

## RAG Annotations
<!-- tags: [Border, Windows Forms, Syncfusion, 2D Border Styles, BorderSingle, BorderColor, BorderStyle] keywords: [Etched, Bump, Sunken, Adjust, Flat, Dotted, Dashed, Solid, Inset, Outset, None, FixedSingle, Fixed3D, HotBorderColor] -->
```