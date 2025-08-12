```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_185.jpeg
document_name: edit
page_number: 185
page_id: edit#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:13Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Provides excellent support for viewport navigation, including intellimouse scrolling.
- Fully supports keyboard navigation functions like PAGE UP/PAGE DOWN keys, ARROW keys, and CTRL+ARROW keys.

## Content

### Viewport Navigation Support

Essential Edit provides excellent support for viewport navigation, including intellimouse scrolling. Commonly used keyboard navigation functions like PAGE UP/PAGE DOWN keys, ARROW keys, and CTRL+ARROW keys are fully supported by Essential Edit.

#### Figure: Preview of Intellimouse in Edit Control

```plaintext
------ The main entry point for the application.
 /// </summary>
 [STAThread]
 static void Main()
 {
      Application.Run(new Form1());
 }
```

* **Figure 60:** Preview of Intellimouse in Edit Control

### See Also

Some of the intellisense features:

- Code Snippets
- Context Choice
- Context Prompt
- Context Tooltip

### 4.6.6.2.5 Drag-and-drop

The Edit Control fully supports the file drop functionality. Any text file can be dragged onto the Edit Control, which then displays the contents of the file, as if the file had been opened with the Edit Control.

The Edit Control also supports the text drag-and-drop functionality. In other words, you can drag a piece of text from one region in the Edit Control to another. You can also drag text from other editor controls like the RichTextBox onto the Edit Control. These features are supported out of the box, and no explicit handling of drag-and-drop operations are required.

#### Enable Drag-and-Drop Functionality

Make sure to set the `AllowDrop` property of the Edit Control to `True` for this purpose.

#### Code Examples

##### C#

```csharp
// Enable drag and drop.
this.editControl1.AllowDrop = true;
```

##### VB.NET

```vbnet
' Enable drag and drop.
this.editControl1.AllowDrop = true
```

## Page-level Navigation/TOC (if applicable)
- Not applicable in this page's content.

## Cross References
- See Also: Code Snippets, Context Choice, Context Prompt, Context Tooltip

<!-- tags: [Windows Forms, Drag-and-Drop, Edit Control, intellimouse, Keyboard Navigation, Syncfusion Winforms] keywords: [drag and drop, allowdrop, intellimouse, text file, text editor, editor control] -->
```