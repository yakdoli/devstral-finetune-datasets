```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_223.jpeg
document_name: edit
page_number: 223
page_id: edit#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:23Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### Figure 71: Edit Control with SingleLineMode Turned On

Refer to the Single Line Mode Demo sample in the following sample installation location, for more information in this regard.

**..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Appearance\\SingleLineModeDemo**

### 4.9.6 Customizable Find Dialog

Essential Edit now enables you to create a new find dialog by inheriting Essential Edit's find dialog. You can customize the **Find Dialog** by changing the properties and triggers the events of the buttons such as **Find**, **Mark All**, and **Close**. You can also easily localize the captions of the controls in the **Find Dialog**.

#### Creating a Class for Own Find Dialog

Create a class for own find dialog that inherits the `frmFindDialog` class. The following code illustrates this.

```csharp
// Inherits the frmFindDialog
public class FindDialogExt : Syncfusion.Windows.Forms.Edit.Dialogs.frmFindDialog
```

```vb.net
' Inherits the frmFindDialog.
Public Class FindDialogExt
    Inherits Syncfusion.Windows.Forms.Edit.Dialogs.frmFindDialog
End Class
```

#### FindComplete Event

---

## Page-level Navigation/TOC (if applicable)

- Refer to the **Single Line Mode Demo** sample for more information.
- File path: **..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Appearance\\SingleLineModeDemo**

#### Customizable Find Dialog

- Overview of find dialog customization.
- Inheriting `frmFindDialog` class.
- Customizing buttons and their captions.
- Localization of dialog controls.

## API Reference (if applicable)

- **frmFindDialog**: Base class for creating a customized find dialog.
- **FindComplete Event**: Event triggered on completion of find operation.

## Code Examples (multi-language supported)

Unsupported: Inline code examples presented separately for **C#** and **VB.NET**,miştir bedeninden başına iktva'ta da var.toString()

## RAG Annotations

- **Tags:** product, module, control, api, version
- **Keywords:** Edit Control, SingleLineMode, Find Dialog, Customization, Localization, frmFindDialog, FindComplete Event
<!-- tags: [product, module, control, api, version?] keywords: [Edit Control, SingleLineMode, Find Dialog, Customization, Localization, frmFindDialog, FindComplete Event] -->
```