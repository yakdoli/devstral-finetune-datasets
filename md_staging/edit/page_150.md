```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: edit
page_number: 150
page_id: edit#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:08Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes how to configure the visual appearance of scroll bars in the Edit Control to match the Office 2007 style.
- Explains how to set the `ScrollVisualStyle` property to achieve the Office 2007 look.
- Details the use of `ScrollColorScheme` property to apply predefined or custom color schemes.

## Content

### 4.6.6.1 Office 2007 Visual Style

Edit Control enables to provide Office 2007 appearance to scroll bars by setting the `ScrollVisualStyle` property to `Office2007`.

It supports all the three Office 2007 Color Schemes (Black, Blue and Silver), which can be set by using the `ScrollColorScheme` property. Also, custom colors can be applied to the scroll bars of the Edit Control. This can be done by setting the `ScrollColorScheme` property to `Managed`.

#### Table: Edit Control Property Descriptions

| Edit Control Property     | Description                                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------|
| `ScrollVisualStyle`       | Specifies the visual style of the scroll bar.                                                                  |
| `ScrollColorScheme`       | Specifies the scroll bar color scheme when `Office2007` or `Office2007Generic` Style is set. The options provided are: |
|                           | - Black                                                                                                          |
|                           | - Blue                                                                                                           |
|                           | - Silver                                                                                                         |
|                           | - Managed                                                                                                        |

#### Code Examples

```csharp
this.editControl1.ScrollVisualStyle = ScrollBarCustomDrawStyles.Office2007;
this.editControl1.ScrollColorScheme = Office2007ColorScheme.Blue;

// Set custom color for the scroll bar.
this.editControl1.ScrollColorScheme = Office2007ColorScheme.Managed;
Syncfusion.Windows.Forms.Office2007Colors.ApplyManagedColors(this, Color.Green);
```

```vb
' To be filled based on the C# example provided.
```

## API Reference

### `ScrollVisualStyle` Property
- **Type**: `ScrollBarCustomDrawStyles`
- **Description**: Specifies the visual style for the scroll bar in the Edit Control.
- **Possible Values**:
  - `Office2007`: Office 2007 style.

### `ScrollColorScheme` Property
- **Type**: `Office2007ColorScheme`
- **Description**: Specifies the color scheme for the scroll bar.
- **Possible Values**:
  - `Black`: Black color scheme.
  - `Blue`: Blue color scheme.
  - `Silver`: Silver color scheme.
  - `Managed`: Allows applying custom colors to the scroll bar.

#### Methods
- **`ApplyManagedColors`**
  - **Namespace**: `Syncfusion.Windows.Forms.Office2007Colors`
  - **Parameters**:
    - `Control`: The control to which the managed colors are applied.
    - `Color`: The custom color to be applied.
  - **Description**: Allows setting custom colors for the scroll bars when `ScrollColorScheme` is set to `Managed`.

## Code Examples (Continued)

The above examples demonstrate how to set the visual style and color scheme for the scroll bars in the Edit Control.

<!-- tags: [product, windows forms, edit control, visual style, office 2007, scroll bar, color scheme, managed colors] keywords: [essentialEdit, ScrollVisualStyle, ScrollColorScheme, Office2007, custom colors, managed colors] -->
```