```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: edit
page_number: 036
page_id: edit#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:01Z
fidelity: lossless
-->

## Clipboard Operations in Edit Control

### Code Examples (C#)

```csharp
// Indicates whether it is possible to perform paste operation in Edit Control.
bool canPaste = this.editControl1.CanPaste;

// Clears all contents in the clipboard associated with Essential Edit.
this.editControl1.ClearClipboard();
```

### Code Examples (VB.NET)

```vb
' Copies the selected text into the clipboard.
Me.editControl1.Copy()

' Cuts the selected text contents from Edit Control and places it into the clipboard.
Me.editControl1.Cut()

' Retrieves copied contents from the clipboard and pastes it into Edit Control.
Me.editControl1.Paste()

' Indicates whether it is possible to perform copy operation in Edit Control.
Dim canCopy As Boolean = Me.editControl1.CanCopy

' Indicates whether it is possible to perform cut operation in Edit Control.
Dim canCut As Boolean = Me.editControl1.CanCut

' Indicates whether it is possible to perform paste operation in Edit Control.
Dim canPaste As Boolean = Me.editControl1.CanPaste

' Clears all contents in the clipboard associated with Essential Edit.
Me.editControl1.ClearClipboard()
```

### 4.2.3.1 EnableMD5

#### Overview
- The EditControl is mainly based on the MD5 algorithm.
- By default, the `EnableMD5` property is enabled in EditControl.

#### FIPS
- The system's cryptography is based on the FIPS compliant algorithms for encryption, hashing, and security.
- When FIPS is enabled, the Clipboard Operations of EditControl are affected as EditControl uses the MD5 algorithm.
- To avoid issues, before enabling FIPS, you must disable the EditControl's MD5 algorithm by setting the `EnableMD5` property to `false`.

<!-- tags: [product, winforms, editcontrol, clipboard, md5, fips] keywords: [enablemd5, clipboard operations, md5 algorithm, fips, cryptography, encryption, hashing, security, essential edit, editcontrol] -->
```