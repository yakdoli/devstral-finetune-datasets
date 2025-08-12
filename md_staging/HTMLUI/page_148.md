```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: HTMLUI
page_number: 148
page_id: HTMLUI#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:41Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Scripting

### Overview

- This page introduces the concept of self-contained HTML documents where element events are handled through embedded C# scripts.
- Demonstrates the flexibility of changing program logic and interface by loading a new HTML file without recompiling.

### Content

#### Scripting Sample

The document is self-contained, with element events handled through C# script embedded in the HTML file itself. This allows for changes to the program logic and interface by simply loading a new HTML file without the need to recompile the assembly.

![Figure 53: HTMLUIScripting Sample](https://via.placeholder.com/600x250)

By default, this sample can be found under the following location:

```
C:\Documents and Settings\username\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\Samples\2.0\HTML Renderer\HTMLUIScripting
```

#### Note

The section explains how scripting can be used to dynamically handle HTML elements and provide flexibility in application design.

### Section: Text Selection

#### Overview

- Discusses the feature of accessing the selected text in the HTMLUI control.
- Explains how users can select required texts and use them within their applications.

#### Content

#### Text Selection

An interesting feature of the HTMLUI control is its ability to access the selected text. This feature helps the user to select required texts available in the HTMLUI control and use the selected text in the applications. The `SelectedText` property of the HTMLUI control is used for this purpose.

#### Code Examples

```csharp
// Return the selected text displayed in the control
this.label1.Text = this.htmluiControl1.SelectedText;
```

```vbnet
' No VB.NET code provided in the image.
```

### API Reference

- **Property**: `SelectedText`
  - Type: `String`
  - Description: Gets or sets the selected text in the HTMLUI control.

### Code Examples (continued)

The provided C# example demonstrates how to use the `SelectedText` property to retrieve and display the selected text within the HTMLUI control.

#### Note

Ensure that the HTMLUI control is properly configured to allow text selection.

## Conclusion

This section highlights the capability of the HTMLUI control to handle selected text dynamically, providing flexibility and enhanced functionality for Windows Forms applications.

<!-- tags: [syncfusion, winforms, htmlui, scripting, text selection, selectedtext, csharp, vb.net] keywords: [htmlui control, selected text, scripting, self-contained html, dynamic text selection, windows forms] -->
```