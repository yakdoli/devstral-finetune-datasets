```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_450.jpeg
document_name: XlsIO
page_number: 450
page_id: XlsIO#page_450
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:32Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- The page explains how to browse and zip folders using a dialog box within an application.
- It demonstrates a code example for handling folder selection and enabling features based on the selection.
- Discusses support for client profiles and the required assemblies to use Essential XlsIO in applications targeting Client profile.

## Content

### Folder Selection and Zipping

```vb
' Browse folder.
Private Sub button2_Click(ByVal sender As Object, ByVal e As EventArgs)
    ' Select the folder to be zipped.
    Dim flrdDialog As New FolderBrowserDialog()
    flrdDialog.Description = "Select the folder to zip. Note: All its subfolders and its files will zip too."
    If flrdDialog.ShowDialog() = Windows.Forms.DialogResult.OK Then
        Me.textBox1.Text = flrdDialog.SelectedPath
        Me.button1.Enabled = True
    End If
End Sub

' Close
Private Sub button3_Click(ByVal sender As Object, ByVal e As EventArgs)
    Close()
End Sub
```

**Figure 168: SyncZip dialog box to zip the files**

![](SyncZip_dialog-box.png)

### Does Essential XlsIO provide support for Client profile?

#### Overview
Yes, Essential XlsIO provides support for Client profile. In order to use Essential XlsIO in an application (which targeted to Client profile), the user should include the following assemblies:

#### Required Assemblies
- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.XlsIO.ClientProfile.dll

## Page-level Navigation/TOC (if applicable)

- 5.2.7 Does Essential XlsIO provide support for Client profile?

## Cross References

- See also: [folder selection], [zipping], [client profile support]

<!-- tags: [Essential XlsIO, FolderBrowserDialog, SyncZip, Client Profile, Syncfusion.Core.dll, Syncfusion.Compression.Base.dll, Syncfusion.XlsIO.ClientProfile.dll] keywords: [folder selection, zipping, dialog box, client profile, support, assemblies] -->
```