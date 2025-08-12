```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_706.jpeg
document_name: tools
page_number: 706
page_id: tools#page_706
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

| Members                             | Description                                                                 |
|-------------------------------------|----------------------------------------------------------------------------|
| Dismiss                             | Specifies whether the dialog is either dismissed or retained depending upon this value. |
| FolderBrowserCallbackSetState       | Gets / sets the Folder Browser dialog's state.                               |
| BrowseCallbackText                 | Gets / sets the contextual string based upon the FolderBrowserCallbackSetState property. |
| FolderBrowserMessage               | Returns a value identifying the event.                                           |
| Path                                | Returns valid or invalid folder name.                                          |
| Window                              | Returns window handle of browser dialog box.                                      |

It can be handled when browser validation is required.

This handler is functionally equivalent to the Win32 BrowseCallbackProc callback function.

## Code Examples

### C#

```csharp
private void folderBrowser1_BrowseCallback(object sender,
    Syncfusion.Windows.Forms.FolderBrowserCallbackEventArgs e)
{
    // We can log the events and Folder Browser Message to the Label control.
    this.label1.Text = String.Format("Event: {0}, Path: {1}",
    e.FolderBrowserMessage, e.Path);
    if (e.FolderBrowserMessage == FolderBrowserMessage.ValidateFailed)
    {
        e.Dismiss = e.Path != "NONE";
    }
}
```

### VB.NET

```vb
Private Sub folderBrowser1_BrowseCallback(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.FolderBrowserCallbackEventArgs)
    ' We can log the events and Folder Browser Message to the Label control.
    Me.label1.Text = String.Format("Event: {0}, Path: {1}",
    e.FolderBrowserMessage, e.Path)
    If e.FolderBrowserMessage = FolderBrowserMessage.ValidateFailed Then
        e.Dismiss = e.Path <> "NONE"
    End If
End Sub
```

## Page-level Navigation/TOC (if applicable)
None

## Cross References
See also: None

<!-- tags: [product, module, control, api, version?] keywords: [Windows Forms, Folder Browser, Callback, validation, Syncfusion, 11.4.0.26] -->
```