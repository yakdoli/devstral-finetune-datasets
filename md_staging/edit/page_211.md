```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_211.jpeg
document_name: edit
page_number: 211
page_id: edit#page_211
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:39Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

Me.editControl1.MarkChangedLines = True

```csharp
using System;
using System.Drawing.Bitmap;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
```

**Figure 66:** Saved Changes in Green and Unsaved Changes in Yellow

Refer to the Selection Margin Demo sample in the following sample installation location, for more information in this regard.

```
..\My Documents\Syncfusion\EssentialStudio\Version
Number\Windows\Edit.Windows\Samples\2.0\Advanced Editor
Functions\SelectionMarginDemo
```

## 4.9.2.2 User Margin

Edit Control supports the User Margin feature, which can be used to display additional information regarding the contents in the Edit Control. Information can also be displayed on a line-by-line basis.

The User Margin feature can be turned on by setting the `ShowUserMargin` property to `True`. The user margin can be customized using the following properties.

| Edit Control Property         | Description                                                               |
| ----------------------------- | ------------------------------------------------------------------------- |
| UserMarginWidth               | Get / sets the width of the user margin.                              |
| UserMarginPlacement           | Specifies placement of user margin.                                   |

```csharp
this.editControl1.UserMarginWidth = 100;

// Sets the User Margin to the Left.
this.editControl1.UserMarginPlacement =
    Syncfusion.Windows.Forms.Edit.Enums.MarginPlacement.Left;
```

## API Reference (if applicable)
- None provided in this section.

## Code Examples (multi-language supported)
- The code examples are provided in the section above.

## Page-level Navigation/TOC (if applicable)
- None provided in this section.

## Cross References
- Refer to the Selection Margin Demo sample in the following sample installation location.

<!-- tags: [syncfusion-winform, edit-control, user-margin-feature, version-11.4.0.26] keywords: [essential edit, windows forms, user margin, saved changes, unsaved changes, selection margin demo, edit control properties, margin placement, width customization, demo sample] -->
```