```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_701.jpeg
document_name: tools
page_number: 701
page_id: tools#page_701
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to set the `StartLocation` property of a FolderBrowserFolder to `CustomStartLocation` in VB.NET.
- Provides code snippets for configuring folder browsing settings in a Windows Forms application.
- Explains the use of the `SelectLocation` property for automatically scrolling and highlighting desired paths.

## Content

### Location Settings of FolderBrowser

[VB.NET]

```vb
' Set the enumeration value FolderBrowserFolder.CustomStartLocation for
' Folder.StartLocation property.
Me.folderBrowser1.StartLocation =
Syncfusion.Windows.Forms.FolderBrowserFolder.CustomStartLocation
Me.folderBrowser1.CustomStartLocation = "C:"

' SelectLocation property for Automatic Scroll and Highlight of desired
' path.
Me.folderBrowser1.SelectLocation = "C:\\Program
Files\\Syncfusion\\Essential Studio"
```

#### Figure 436: Location Settings of FolderBrowser

The image includes a folder browser dialog with the location settings configured as described in the code. The `CustomStartLocation` is set to `C:`, and the `SelectLocation` is defined as `"C:\\Program Files\\Syncfusion\\Essential Studio"`.

A sample demonstrating the Location Settings of FolderBrowser is available in the following sample installation path:

```
..My Documents\\Syncfusion\\EssentialStudio\\Version
Number\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\FolderBrowserDemo
```

---

### 3.5.7.1.3.2 Style Settings

The style settings that are available for the FolderBrowser Dialog are given below.

## API Reference

- `Syncfusion.Windows.Forms.FolderBrowserFolder.StartLocation`
- `Syncfusion.Windows.Forms.FolderBrowserFolder.CustomStartLocation`
- `Syncfusion.Windows.Forms.FolderBrowserFolder.SelectLocation`

## Code Examples (multi-language supported)

The provided VB.NET code snippet demonstrates how to configure the `StartLocation` and `SelectLocation` properties of a `FolderBrowserFolder` control.

---

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms
  - Location Settings of FolderBrowser
  - Style Settings

---

<!-- tags: [syncfusion-sdk, winforms, toolbox, folderbrowser, configuration, VB.NET, style settings] -->
```