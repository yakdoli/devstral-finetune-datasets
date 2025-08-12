```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_343.jpeg
document_name: tools
page_number: 343
page_id: tools#page_343
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of the "Redo" button type with various border styles.
- Explains how to enable visual styles for the `ButtonAdv` control using the `UseVisualStyle` property.
- Describes the different visual styles available and their settings through the `Appearance` property.

## Content

### Figure 154: "Redo" ButtonType, ButtonAdvControls with Different Border Styles (Appearance="Office2003")

This figure illustrates various border styles available for the "Redo" `ButtonType` in `ButtonAdvControls` when the `Appearance` is set to "Office2003". The styles include: Dashed, Dotted, Inset, Outset, Bump, Etched, Flat, Raised, RaisedInner, RaisedOuter, Sunken, SunkenInner, and SunkenOuter. 

#### Border Styles Examples
- **Dashed**: Displays a dashed border.
- **Dotted**: Displays a dotted border.
- **Inset**: Displays an inset effect.
- **Outset**: Displays an outset effect.
- **Bump**: Displays a bump effect.
- **Etched**: Displays an etched effect.
- **Flat**: Displays a flat design.
- **Raised**: Displays a raised effect.
- **RaisedInner**: Displays a raised inner effect.
- **RaisedOuter**: Displays a raised outer effect.
- **Sunken**: Displays a sunken effect.
- **SunkenInner**: Displays a sunken inner effect.
- **SunkenOuter**: Displays a sunken outer effect.

#### See Also
- [Visual Styles, Button Types](Visual Styles, Button Types)

### 3.5.2.1.3.1.3 Visual Styles

The section delves into how visual styles for the `ButtonAdv` control can be enabled and customized.

#### Enabling Visual Styles
- **Property**: `UseVisualStyle`
  - When set to `true`, the `ButtonAdv` control uses the visual styles defined by the `Appearance` property.

#### Visual Styles Configuration
- **Property**: `Appearance`
  - This property determines the visual style applied to the `ButtonAdv` control when `UseVisualStyle` is `true`. The available styles include:
    - **Classic**
    - **Office2000**
    - **WindowsXP**
    - **OfficeXP**
    - **Office2003**
    - **Office2007**

#### Table: Visual Styles Property Description

| Property       | Description                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------|
| Appearance     | Sets the visual styles for the control when `UseVisualStyle` property is true. The styles are:       |
|                | **Classic**, **Office2000**, **WindowsXP**, **OfficeXP**, **Office2003**, and **Office2007**.       |

### Code Examples

#### C#
The section includes a placeholder for C# code examples related to configuring visual styles for the `ButtonAdv` control.

```csharp
// Example code for enabling visual styles
buttonAdv1.UseVisualStyle = true;
buttonAdv1.Appearance = ButtonAppearance.Office2003;
```

## API Reference

### Properties
- **Appearance**: Type - `ButtonAppearance`  
  Description: Defines the visual style of the `ButtonAdv` control when `UseVisualStyle` is enabled.  
  Default: `ButtonAppearance.Classic`  
  Required: No  

- **UseVisualStyle**: Type - `bool`  
  Description: When set to `true`, the `ButtonAdv` control uses the visual styles defined in the `Appearance` property.  
  Default: `false`  
  Required: No  

### Events
- **Click**: Occurs when the button is clicked.

### Methods
- **ApplyAppearance**: Applies the specified visual style to the button.  

## RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, ButtonAdv, Visual Styles, Typography] keywords: [Redo, Dashed, Dotted, Inset, Outset, Bump, Etched, Flat, Raised, RaisedInner, RaisedOuter, Sunken, SunkenInner, SunkenOuter, Classic, Office2000, WindowsXP, OfficeXP, Office2003, Office2007] -->
```
