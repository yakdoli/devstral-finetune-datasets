```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_703.jpeg
document_name: tools
page_number: 703
page_id: tools#page_703
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:22Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### FolderBrowser Dialog Styles

- **ShowTextBox** - Displays textbox in the FolderBrowser Dialog.
- **StatusText** - Includes status area in the dialog box. StatusText can be specified in the FolderBrowserCallBack event handler. This style does not apply to 'NewDialogStyle'.
- **UAHint** - Adds an usage hint to the folder dialog. It can be applied only with 'NewDialogStyle'.
- **Validate** - Typing invalid name in the textbox triggers FolderBrowserCallBack event.

### Code Examples

#### C#

```csharp
this.folderBrowser1.Style = 
Syncfusion.Windows.Forms.FolderBrowserStyles.ShowTextBox;
```

#### VB.NET

```vb
Me.folderBrowser1.Style = 
Syncfusion.Windows.Forms.FolderBrowserStyles.ShowTextBox
```

### Figure Example

![](Figure_437.png)

**Figure 437:** "ShowTextBox" Style of FolderBrowser

#### Summary

A Sample which demonstrates the Style Settings of FolderBrowser is available in the below sample installation path.

<!-- Page-level Navigation/TOC (if applicable) -->

<!-- tags: [winforms, folderbrowser, dialogstyles, showtextbox, statustext, uahint, validate] keywords: [folderbrowserdialog, style settings, event handler, textbox, status area, usage hint, invalid name validation] -->
```