```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_219.jpeg
document_name: edit
page_number: 219
page_id: edit#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:12Z
fidelity: lossless
-->

Essential Edit for Windows Forms

```csharp
this.toolStripMenuItem3.Text = "&Open";
this.toolStripMenuItem3.Click += new System.EventHandler(this.toolStripMenuItem3_Click);

// menuItem4
this.toolStripMenuItem4.Index = 2;
this.toolStripMenuItem4.Text = "-";

// menuItem5
this.toolStripMenuItem5.Index = 3;
this.toolStripMenuItem5.Text = "Save";
this.toolStripMenuItem5.Click += new System.EventHandler(this.toolStripMenuItem5_Click);

// menuItem6
this.toolStripMenuItem6.Index = 4;
this.toolStripMenuItem6.Text = "SaveAs";
this.toolStripMenuItem6.Click += new System.EventHandler(this.toolStripMenuItem6_Click);
```

**Figure 69: Background Color and Border set for Text**

**Note:** Refer the **Text Border** topic to know how to set the border for the text.

## Removing Background Color for Individual Lines or Selected Blocks of Text

The following methods can be used to set the background color for individual lines or selected blocks of text.

| Edit Control Method                | Description                           |
| ----------------------------------- | ------------------------------------- |
| RemoveLineBackColor                | Removes line back color.              |
| RemoveSelectionBackColor           | Removes background coloring from the selected text. |

### [C#]

```csharp
// Removes line back color.
this.editControl.RemoveLineBackColor(4);
```

## Page-level Navigation/TOC (if applicable)

- [unclear]

## Cross References

See also:
- Text Border topic

## RAG Annotations

<!-- tags: [Essential Edit, Windows Forms, menuItem, background color, text border, removeLineBackColor, removeSelectionBackColor, C#] keywords: [background color, text border, menu item, line back color, selection back color, C# code sample] -->
```