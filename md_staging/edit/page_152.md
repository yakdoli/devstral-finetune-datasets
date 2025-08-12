```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_152.jpeg
document_name: edit
page_number: 152
page_id: edit#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:47Z
fidelity: lossless
-->

## Interactive Features

### Overview
- The section discusses the customizable context menu feature of the Edit Control available in Syncfusion Winforms.
- Topics covered include enabling advanced features such as indent selection, comment selection, and bookmarking.

### Content

#### Customizable Context Menu

Edit Control has a built-in context menu which is enabled by default. This context menu allows you to edit the contents and open or create a new file. It includes some advanced features like indent selection, comment selection, adding bookmarks, and much more. This is enabled by using the `EditControl1.ContextMenuManager.Enabled` property.

The context menu has the standard VS.NET-like appearance and can optionally be provided with the Office 2003 appearance.

![Figure 53: Edit Control's Context Menu in Office2003 Style](image.png)

Set the appearance of the context menu by specifying the desired `ContextMenuProvider`.

```csharp
// Code example will be included here if available
```

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Controls
- **Class**: EditControl
- **Property**: `ContextMenuManager.Enabled`
- **Description**: Enables or disables the context menu functionality.
- **Default**: `true`
- **Parameters**:
  - **Type**: None
  - **Description**: This property controls the visibility of the context menu.

## Code Examples

### Example 1: Enabling and Customizing the Context Menu

```csharp
using Syncfusion.Windows.Forms;

EditControl editControl1 = new EditControl();
editControl1.ContextMenuManager.Enabled = true;
// Additional customization can be applied here
```

## Cross References

See also:
- [Edit Control Overview](edit#page_1#overview-of-edit-control)
- [Customizing the Editing Experience](edit#page_150#customizing-editing-experience)
- [Adding Advanced Editing Features](edit#page_154#advanced-editing-features)

<!-- tags: [Syncfusion Winforms, Edit Control, Interactive Features, Context Menu, Advanced Features, Office 2003 Style, Customization, Code Example] keywords: [EditControl, ContextMenuManager, Customizable Context Menu, Advanced Features, Office 2003, Customization, CodeExamples, InteractiveFeatures] -->
```