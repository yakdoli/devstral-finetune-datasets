```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_441.jpeg
document_name: grid
page_number: 441
page_id: grid#page_441
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:54Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- This page discusses the `Buttons3D` property in the Essential Grid control, detailing how it affects the appearance of row and column headers. It provides code examples in C# and VB.NET to demonstrate how to enable or disable this property.

## Content

### Buttons3D Property

- **Functionality**: Specifies whether the row and column headers should have a three-dimensional look, enhancing their visual appeal. If set to `false`, the headers appear flat. The default value is set to `true`.

#### Code Examples for Setting the `Buttons3D` Property

1. **Using C#**

```csharp
// [C#]

// Enable Buttons3D property.
this.gridControl1.Properties.Buttons3D = false;
```

2. **Using VB.NET**

```vb
' [VB.NET]

' Enable Buttons3D property.
Me.gridControl1.Properties.Buttons3D = False
```

### Visual Transformation

- The following illustration shows the transformation of the Grid in "Figure 1" when the `Properties.Buttons3D` property is set to `false`.

## API Reference

### Properties

- **Buttons3D**: A Boolean property that determines the three-dimensional appearance of the row and column headers.

#### Parameters

| Name        | Type    | Description                                                                                                                                                                                                                     | Default | Required |
|-------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------|
| Buttons3D   | Boolean | Specifies whether the row and column headers should have a three-dimensional appearance. If set to `false`, the headers will appear flat. The default value is `true`. | true    | Yes      |

### Returns

- `type`: Unit
- Description: No return value; this property modifies the visual appearance of the grid headers.

### Exceptions

- No specific exceptions are mentioned.

## Code Examples (continued)

- Refer to the provided examples in C# and VB.NET for practical usage of the `Buttons3D` property.

### Visual Representation

- The page includes a detailed explanation and code examples to demonstrate the effect of enabling or disabling the `Buttons3D` property.

## Conclusion

- The `Buttons3D` property allows developers to customize the visual style of the grid headers, offering a choice between a three-dimensional or flat appearance.

## RAG Annotations

- <!-- tags: [Essential Grid, Windows Forms, Buttons3D, Visual Styling, C#, VB.NET, Grid Control] keywords: [Buttons3D, three-dimensional headers, flat headers, grid appearance, development examples] -->
```