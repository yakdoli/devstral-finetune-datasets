```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: diagram
page_number: 060
page_id: diagram#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:33Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp

{
    PageBorderDialog borderDialog = new PageBorderDialog();
    borderDialog.PageBorderStyle = diagram1.View.PageBorderStyle; // It will show existing border set up
    if (borderDialog.ShowDialog() == DialogResult.OK)
    {
        diagram1.View.PageBorderStyle = borderDialog.PageBorderStyle;
        // It will update the modified set up.
        diagram1.View.RefreshPageSettings();
        diagram1.UpdateView();
    }
}
```

## Overview

- **Focus**: Integration of custom page borders in diagrams.
- **Key Feature**: Use of `PageBorderDialog` to customize border styles.
- **Result**: Updated diagram with personalized border settings.

## Content

### Diagram Page Borders Dialog Box

The **Page Borders Dialog Box** allows users to customize the appearance of diagram page borders. This dialog provides options for **Round Corners**, **Line Style**, and **Transparency**, enabling precise control over the border appearance.

#### Figure 32: Diagram Page Borders Dialog Box

![](attachment:Screen_Shot_2023-08-21_at_12.39.27_AM.png)

### 3. Header and Footers

The **Header and Footer** dialog provides an interactive form-based interface for initializing the **Header and Footer settings** of a diagram.

#### Overview

The **Header and Footer** dialog enables users to configure visible elements at the top and bottom of the diagram, enhancing the layout and organization.

#### Code Snippet for Header and Footer Dialog

The following code snippet can be used for creating the **Header and Footer** dialog.

```csharp
[C#]
if (diagram1 != null && diagram1.Model != null)
{
    HeaderFooterDialog dlgHF = new HeaderFooterDialog();
}
```

## API Reference (if applicable)

This page does not contain direct API references. However, the APIs used for configuring headers, footers, and page borders in diagrams are part of the standard Syncfusion WinForms API.

### WinForms-specific Implementation

- **PageBorderDialog**: For configuring page borders.
- **HeaderFooterDialog**: For initializing headers and footers.

## Code Examples (multi-language supported)

This section provides the code examples shown in the image, demonstrating how to implement the dialog boxes for configuring diagram settings.

### 1. Page Border Configuration

```csharp
PageBorderDialog borderDialog = new PageBorderDialog();
borderDialog.PageBorderStyle = diagram1.View.PageBorderStyle;
if (borderDialog.ShowDialog() == DialogResult.OK)
{
    diagram1.View.PageBorderStyle = borderDialog.PageBorderStyle;
    diagram1.View.RefreshPageSettings();
    diagram1.UpdateView();
}
```

### 2. Header and Footer Initialization

```csharp
[C#]
if (diagram1 != null && diagram1.Model != null)
{
    HeaderFooterDialog dlgHF = new HeaderFooterDialog();
}
```

## Cross References

- See also: Diagram properties and methods for further customization.
- Additional details on dialog box functionality can be found in the **Syncfusion WinForms Documentation**.

## RAG Annotations

<!-- tags: [diagram, winforms, page borders, header, footer, setting custom border styles] keywords: [PageBorderDialog, HeaderFooterDialog, EditBox, diagram1, PageBorderStyle, dialogbox] -->
```