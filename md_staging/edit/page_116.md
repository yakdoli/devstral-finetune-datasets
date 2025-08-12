```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: edit
page_number: 116
page_id: edit#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:45Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
' Images that indicate the point at which the line is being wrapped.
Me.editControl1.CustomLineWrappingMarkingImage = (CType((resources.GetObject("$this.Blue_hills")), System.Drawing.Image))
' Indicate wrapped lines.
Me.editControl1.MarkWrappedLines = True
```

Figure 38: Wrapping Images indicating Wrapped Lines and Point of Wrapping

## 4.4.11.7 Read-Only Text

Edit Control allows you to specify read-only regions in the code, i.e., regions that are uneditable. This can be achieved through the following methods.

| Edit Control Method       | Description                                       |
|---------------------------|---------------------------------------------------|
| MarkAsReadOnly           | Sets text as read-only.                           |
| RemoveReadOnly           | Removes read-only status of specified region.     |

## API Reference

### Methods
- **MarkAsReadOnly()**
  - Sets the text as read-only.

- **RemoveReadOnly()**
  - Removes the read-only status of the specified region.

## See also:
- [MarkWrappedLines Property](#)
- [Line Wrapping in Syncfusion WinForms](#)
- [Syncfusion API Documentation](#)

<!-- tags: [syncfusion-sdk, windows-forms, editcontrol, line-wrapping, readonly, version-11.4.0.26] keywords: [markwrappedlines, markasreadonly, removereadonly, read-only, winforms, syncfusion, line-wrapping-images, essential-edit] -->
```