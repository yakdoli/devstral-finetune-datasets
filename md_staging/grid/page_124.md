```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: grid
page_number: 124
page_id: grid#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:40:19Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Feature Support Table

The following table summarizes the support for specific accessibility features in the Essential Grid for Windows Forms:

| Criteria                                                                                                                                                                                                 | Supporting Features         | Remarks                                                                                  | Explanations                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (c) A well-defined on-screen indication of the current focus shall be provided that moves among interactive interface elements as the input focus changes. The focus shall be programmatically exposed so that Assistive Technology can track focus and focus changes. | Fully Supported             | The focusing indication is applied to the individual cells.                                  | The border of the current cell can be highlighted if the grid has the focus on the specific cell.                                                                 |
| (d) Sufficient information about a user interface element including the identity, operation and state of the element shall be available to Assistive Technology. When an image represents a program element, the information conveyed by the image must also be available in text. | Not Applicable              | It is application-oriented, where the information to be provided on an individual component depends on the event of the grid. |                                                                                                                                                                 |
| (e) When bitmap images are used to identify controls, status indicators, or other programmatic elements, the meaning assigned to those images shall be                                                                                                                                                              | Fully Supported             | Supports on design time to identify the control.                                                | The dependent property has been provided, where the property window will identify the control and specify its own attributes.                                      |

### Summary

This page discusses the accessibility features supported by the Essential Grid for Windows Forms, focusing on:

- Clear focus indication for assistive technology.
- Sufficient information for user interface elements.
- Identification of controls through bitmap images with meaningful meanings.

### WinForms-specific Notes

- The support for assistive technology is crucial for ensuring usability and accessibility of the grid control.
- Feature support varies, with some features being fully supported while others are not applicable based on the application context.

### API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Grid`
- **Class**: `GridControl`
- **Properties**:
  - `CurrentCell` - Represents the currently active cell.
  - `FocusIndicatorStyle` - Indicates how the focus is displayed.
  - `Accessibility` - Manages accessibility features.

### Code Examples

```csharp
// Example: Setting focus to a specific cell
gridControl.CurrentCell = new GridRange(1, 1);

// Example: Providing text alternative for an image
imageControl.AccessibleDescription = "Add a Product";
```

### Page-level Navigation/TOC

- [Accessibility Support](#accessibility-support)
- [Feature Details](#feature-details)

### Cross References

- See also: [Understanding Accessibility](#understanding-accessibility)

### RAG Annotations

<!-- tags: [essential grid, windows forms, accessibility, assistive technology, feature support] keywords: [border highlight, assistive technology, focus tracking, grid control, focus indicator, text alternative, programmatic elements] -->
```