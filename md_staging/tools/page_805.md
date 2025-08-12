```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_805.jpeg
document_name: tools
page_number: 805
page_id: tools#page_805
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Overview of multiline feature properties in textboxes.
- Explanation of WordWrap and ScrollBar functionalities.
- Details on how to configure a textbox for multiline input with automatic scrolling and wrapping.

## Content

### Multiline Feature Properties

| Property        | Description                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------|
| WordWrap        | Setting this property to `true` will automatically wrap the text if the textbox is resized.          |
| ScrollBar       | We can show scrollbars for the control when multiline feature is enabled. The different options are: |
|                 |                                                                                                      |
|                 | - Horizontal - Displays horizontal scrollbar,                                                          |
|                 | - Vertical - Displays vertical scrollbar,                                                             |
|                 | - Both - Enables horizontal scrollbar when `WordWrap = false` and enables vertical scrollbar when `WordWrap` is set to `true`, |
|                 | - None.                                                                                              |

### Implementation Examples

#### C#
```csharp
this.currencyTextBox1.Multiline = true;
this.currencyTextBox2.Text = "$12,456,456,456,456,456,456,456.00";
this.currencyTextBox2.WordWrap = "true";
this.currencyTextBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both;
```

#### VB.NET
```vb
Me.currencyTextBox1.Multiline = True
Me.currencyTextBox2.Text = "$12,456,456,456,456,456,456,456.00"
Me.currencyTextBox2.WordWrap = True
Me.currencyTextBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both
```

### Figure 507: Multiline = "True"

Figure: A textbox with the `Multiline` property set to "True".

---

## API Reference

### Properties

- **Multiline**: Enables or disables the multiline feature in a textbox.
- **WordWrap**: Controls whether text wraps within the textbox.
- **ScrollBars**: Specifies which scrollbars to display in a textbox.

### Methods
None listed in this context.

---

## Code Examples

Refer to the C# and VB.NET code snippets provided above for implementing multiline, word wrap, and scrollbars in a textbox.

---

### References
- See also: [TextBox Control in Windows Forms](#)
- [Properties of TextBox Control](#)

<!-- tags: [winforms, textbox, multiline, wordwrap, scrollbars] keywords: [textbox, multiline property, wordwrap, scrollbars, implementation, csharp, vb.net] -->
```