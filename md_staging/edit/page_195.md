```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_195.jpeg
document_name: edit
page_number: 195
page_id: edit#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:40Z
fidelity: lossless
--> 

# Essential Edit for Windows Forms

## Overview
- Disables the default "Save Changes" prompt when closing forms with unsaved content.
- Provides examples in C# and VB.NET for managing save-on-close behavior.

## Content

### Disabling the Default Save Changes Prompt

The following code disables the default Save Changes prompt that appears when the form hosting the Edit Control containing unsaved contents is closed.

#### C#

```csharp
// Disables the default Save Changes prompt that appears when the form hosting Edit Control containing unsaved contents is closed.
this.editControl1.SaveOnClose = false;
```

#### VB.NET

```vb
' Disables the default Save Changes prompt that appears when the form hosting Edit Control containing unsaved contents is closed.
Me.editControl1.SaveOnClose = False
```

![Default Save Changes Prompt Dialog Box](https://i.imgur.com/ExampleImage.png)
*Figure 62: Default Save Changes Prompt Dialog Box*

### Saving Changes without Displaying the Save Changes Prompt

When the `SaveOnClose` property is set to `False`, the default Save Changes prompt does not appear. The user should perform a custom Save routine in the `Closing` event handler of the host form to save the unsaved contents in the Edit Control; otherwise, they will be lost.

#### C#

```csharp
private void Form1_Closing(object sender, 
                           System.ComponentModel.CancelEventArgs e)
{
    if (this.editControl1.SaveOnClose == false)
    {
        if (this.editControl1.SaveModified() == true)
        {
            // Perform custom Save routine or show custom Save Changes dialog or set Cancel to False.
            e.Cancel = false;
        }
        else
            e.Cancel = true;
    }
}
```

#### VB.NET

```vb
Private Sub Form1_Closing(ByVal sender As Object, _
                         ByVal e As System.ComponentModel.CancelEventArgs) Handles Me.Closing

    If Me.editControl1.SaveOnClose = False Then
        If Me.editControl1.SaveModified() = True Then
            ' Perform custom Save routine or show custom Save Changes dialog or set Cancel to False.
            e.Cancel = False
        Else
            e.Cancel = True
        End If
    End If
End Sub
```

#### Note:
- The custom Save routine or dialog should handle saving the unsaved changes in the `editControl1` before closing the form.
- If the user does not perform the custom save, the `Cancel` property can be set to `True` to prevent the form from closing, allowing the user to save changes first.

<!-- tags: [windows forms, edit control, save changes prompt, closing event, custom save routine] keywords: [save on close, unsaved content, dialog box, form closing, property setting, Syncfusion] -->
```