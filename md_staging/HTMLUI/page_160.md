```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: HTMLUI
page_number: 160
page_id: HTMLUI#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:31Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- This section explains how to modify the HTML document's rendering by changing the font used by the HTMLUI control.
- Demonstrates altering the default font and image references in the HTMLUI control using its features.

## Content

### Overview of Syncfusion HTMLUI

**Figure 55: Changing Image Reference by using the PreRenderDocument Event of the HTMLUI Control**

![Syncfusion HTMLUI](image.png)

*Description:*
- **Syncfusion HTMLUI** provides a robust suite of tools for Windows Forms applications, offering advanced functionality for rendering HTML content.
- The image showcases the features and capabilities of the Essential Studio libraries, highlighting the integration with .NET technologies.

### How To Change the Default Font Used For Rendering the HTML Document In the HTMLUI Control?

#### 5.7 How To Change the Default Font Used For Rendering the HTML Document In the HTMLUI Control?

HTMLUI uses a default font to render the text from the HTML document, in cases where there are no specifications for the font to be used. You can change this default font by using the `DefaultFormat.Font` property, written while initializing the HTMLUI control.

#### Example Code in C#

```csharp
htmluiControl1 = new Syncfusion.Windows.Forms.HTMLUI.HTMLUIControl();
htmluiControl1.DefaultFormat.Font = new Font("Pristina", 16);
```

#### Explanation
- **Initialization**: The `htmluiControl1` is initialized as a new instance of `HTMLUIControl` provided by the Syncfusion.Windows.Forms library.
- **Property Setting**: The `DefaultFormat.Font` property is set to specify the default font to be used by the control. In this example, the font is set to "Pristina" with a size of 16.

## API Reference

The following API element is used in this section:

- **DefaultFormat.Font**
  - **Description**: Specifies the default font to be used for rendering the HTML content in the HTMLUI control.
  - **Type**: `System.Drawing.Font`
  - **Usage**: Set this property when initializing the HTMLUI control to change the default font.

## Code Examples

#### Example 1: Changing the Default Font
- **Purpose**: Demonstrates how to set the default font for the HTMLUI control.

```csharp
// Create a new HTMLUI control
htmluiControl1 = new Syncfusion.Windows.Forms.HTMLUI.HTMLUIControl();

// Set the default font to Pristina with size 16
htmluiControl1.DefaultFormat.Font = new Font("Pristina", 16);
```

## Cross References

See also:
- `PreRenderDocument` event: Useful for modifying the HTML document before it is rendered.
- `HTMLUIControl` class: Provides methods and properties for managing HTML content rendering in Windows Forms.

<!-- tags: [web, controls, windows forms, html, htmlui, font, rendering, syncfusion, winforms, .NET essentials] keywords: [font, html document, rendering, default font, HTMLUI, Syncfusion, Windows Forms, C# code, pre-render document, .NET Essentials, Pristina, font size] -->
```