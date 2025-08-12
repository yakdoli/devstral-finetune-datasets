```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: edit
page_number: 109
page_id: edit#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:53Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

- **WrapByChar** - wraps the text by individual characters
- **WrapByWord** - wraps the text by individual words

The default value is `WrapByWord`.

### Code Examples

```csharp
// WordWrap property set.
this.editControl1.WordWrap = true;

// WordWrapType property set.
this.editControl1.WordWrapType = Syncfusion.Windows.Forms.Edit.Enums.WrapByChar;
```

```vb.net
' WordWrap property set.
Me.editControl1.WordWrap = True

' WordWrapType property set.
Me.editControl1.WordWrapType = Syncfusion.Windows.Forms.Edit.Enums.WordWrapType.WrapByChar
```

## Wordwrap Mode

The following properties are associated with setting the mode of Word Wrapping.

| Edit Control Property   | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| WordWrapMode            | Gets / sets state of the word wrapping mode. The options provided are:   |
|                         | - **WordWrapMargin** - wraps text at the boundary between text area and wordwrap margin of the Edit Control |
|                         | - **Text Area**: The area beyond the text area in the Edit Control is referred to as |

## Cross References

- **See also:**
  - [Syncfusion documentation](https://www.syncfusion.com/documentation/windows-forms/edit-control)
  - [Word Wrapping in the Edit Control](https://www.syncfusion.com/documentation/windows-forms/edit-control/word-wrapping)

<!-- tags: [Syncfusion, WinForms, Edit Control, WordWrap, Text Formatting, C#, VB.NET] keywords: [Syncfusion, WinForms, Edit Control, WordWrapMode, WordWrapType, C#, VB.NET] -->
```