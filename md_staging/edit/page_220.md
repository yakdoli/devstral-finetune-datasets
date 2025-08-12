```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_220.jpeg
document_name: edit
page_number: 220
page_id: edit#page_220
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:44Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

// Removes background coloring from the selected text.  
this.editControl1.RemoveSelectionBackColor();

### VB.NET

' Removes line back color.  
Me.editControl1.RemoveLineBackColor(4)

' Removes background coloring from the selected text.  
Me.editControl1.RemoveSelectionBackColor()

A sample which demonstrates Text Highlighting is available in the following sample location.

```
.\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Edit.Windows\Samples\2.0\Advanced Editor Functions\TextHighlightingDemo
```

## See Also

- [Line Numbers and Current Line Highlighting](Line Numbers and Current Line Highlighting)

### 4.9.4 Font Customization

The font customization in the Edit Control works slightly different from the regular text processing the control. The font customization is done only at the **Formats** level, and not at a word level or selected text level. Edit Control is more of a text parsing / syntax highlighting control, and less of a text editing control. Edit Control supports customization of fonts both through the configuration file and dynamically through a run-time **Formats Editor** dialog.

The Edit Control supports customization of fonts through the configuration file, as shown in the below code snippet.

### XML

```xml
<format name="Text" Font="Courier New, 10pt" FontColor="Black" />
<format name="SelectedText" Font="Courier New, 10pt" BackColor="Highlight" FontColor="HighlightText" />
<format name="String" Font="Courier New, 10pt, style=Bold" FontColor="Red" />
<format name="Whitespace" Font="Courier New, 10pt" FontColor="Black" />
<format name="Operator" Font="Courier New, 10pt" FontColor="DarkCyan" />
```

### Copyright

© 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion, Windows Forms, Text Highlighting, Font Customization, Edit Control] keywords: [Text Highlighting, Font Customization, Edit Control, Syntax Highlighting, Configuration File, Formats Editor, Font Properties, Text Control] -->
```