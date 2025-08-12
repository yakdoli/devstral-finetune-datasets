```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: HTMLUI
page_number: 037
page_id: HTMLUI#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:45Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- This page explains how to load an HTML file from disk using HTMLUI and demonstrates working with links between HTML documents.
- Includes a sample implementation for file loading and jump links functionality.
- Demonstrates the use of HTMLUI for integrating with Windows Forms applications.

## Content

### 4.1.2.1.1 Load File From Disk Sample

This sample demonstrates the implementation of Loading a file from Disk by using HTMLUI.

#### Figure 16: LoadFileFromDisk Sample

![LoadFileFromDisk Sample](#unclear)

##### Description

The example showcases how an HTML file from the user's drive can be easily loaded into the HTMLUI control. The sample includes the following code snippet:

```csharp
this.liteHtml.Cursor = System.Windows.Forms.Cursors.WaitCursor;
this.liteHtml.Location = new System.Drawing.Point(8, 8);
this.liteHtml.Name = "liteHtml";
this.liteHtml.Size = new System.Drawing.Size(640, 224);
this.liteHtml.StartupDocument = @"D:\work\syncfusion\suitevss\Products\Devalog.log";
```

#### Default Location

By default, this sample can be found under the following location:

```
C:\Documents and Settings\<username>\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\Samples\2.0\Loading HTMLUILoadFileFromDisk
```

### 4.1.2.2 As Links From One HTML Document To Another

The HTMLUI supports the `Link` property. Links in HTML code are easily invoked in HTMLUI Control. The main document that contains links to other documents is loaded into the HTMLUI control. The linked document is loaded by clicking the respective link in the main document.

---

## API Reference (if applicable)
- `Namespace: Syncfusion.Windows.Forms.HTMLUI`
- `Class: HTMLUI`
- `Properties:`
  - `Cursor: Cursor`
  - `Location: Point`
  - `Name: string`
  - `Size: Size`
  - `StartupDocument: string`
- `Methods/Events: None explicitly shown in this context.`

## Code Examples

### C# Example for Loading a File

```csharp
// Setting up the HTMLUI control
liteHtml.Cursor = System.Windows.Forms.Cursors.WaitCursor;
liteHtml.Location = new System.Drawing.Point(8, 8);
liteHtml.Name = "liteHtml";
liteHtml.Size = new System.Drawing.Size(640, 224);
liteHtml.StartupDocument = @"D:\work\syncfusion\suitevss\Products\Devalog.log";
```

## Page-level Navigation/TOC (if applicable)
- 4.1.2.1.1 Load File From Disk Sample
- 4.1.2.2 As Links From One HTML Document To Another

## Cross References
- See also: HTMLLinkClicked event, HTMLUI documentation, Syncfusion Essential Studio for Windows Forms.

<!-- tags: [syncfusion, windows forms, htmlui, html, file loading, links, startup document, essentialsstudio version number] keywords: [load file, htmlui control, links, document loading, html code, startup document, file location] -->
```