```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_124.jpeg
document_name: pdf
page_number: 124
page_id: pdf#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:05Z
fidelity: lossless
-->

## Content

### Overview

- PdfPageTemplateElement class supports alignment and docking functionalities.
- Alignment uses the Alignment property, while docking uses the Dock property.
- Docking priority is similar to Windows Forms Docking functionality, with Top and Bottom taking precedence.
- Docking stamp elements do not have priorities, and their appearance depends on their order in the collection.

### Detailed Functionality

- **Alignment vs. Docking**: Alignment has higher priority than Docking in the template element, but Docking resets the Alignment.

 subtly. If you try setting it you could see undesirable - disproportionately large borders, or stretched content in the of the rendered PDF. "That's not the design."

- **Avoid stretching**: Docked elements stick to their respective page sides and reset the alignment. Avoid printing content that can be stretched where pages have different sizes.

- **Define sizes**: Sizes of docked elements should be aligned to their docking style.

- **Workarounds for alignment**: If you want an element to be in position without stretching, set the Alignment property after assigning the Dock property or alignment settings to it.

### Note on Alignment Property Restrictions

- **Alignment with Docking**: If you set an element as Top, the allowed values for Alignment are TopLeft, TopCenter, and TopRight. Setting any other value could lead to inconsistency with the Docking style.

### Z-Order of the Layers

Each page can have multiple layers, including document page templates, section page templates, and various stamp and layer elements. The order of rendering from back to top is as follows:

1. **Document page templates with Background set to True** (Left, Top, Right, Bottom).
2. **Document stamp elements with Background set to True**.
3. **Section page templates with Background set to True** (Left, Top, Right, Bottom).
4. **Section stamp elements with Background set to True**.
5. **Page layers**.
6. **Section page templates with Foreground set to True** (Left, Top, Right, Bottom).
7. **Section stamp elements with Foreground set to True**.
8. **Document page templates with Foreground set to True** (Left, Top, Right, Bottom).
9. **Document stamp elements with Foreground set to True**.

## API Reference

- **PdfsPageTemplateElement**: This class provides functionality for alignment and docking.
- **Alignment Property**: Used to set the alignment of the template element.
- **Dock Property**: Used to set the docking behavior of the template element.
- **Background Property**: Determines whether a template element appears behind page content.
- **Foreground Property**: Determines whether a template element appears on top of page content.

<!-- tags: [PdfPageTemplateElement, Alignment, Dock, Z-Order, Stamp, Layer, Syncfusion Winforms] keywords: [alignment, docking, z-order, template element, background, foreground, Syncfusion] -->
```