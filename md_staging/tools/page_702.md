```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_702.jpeg
document_name: tools
page_number: 702
page_id: tools#page_702
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:32Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### FolderBrowserDialog Properties

| FolderBrowser Property | Description                                                                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Style                   | Specifies the options for the FolderBrowser Dialog. <br> The options included are as follows: <br> RestrictToFilesystem, <br> RestrictToSubfolders, <br> RestrictToDomain, <br> BrowseForComputer, <br> BrowseForEverything, <br> BrowseForPrinter, <br> NewDialogStyle, <br> AllowUrls, <br> ShowAdministrativeShares, <br> ShowShares, <br> ShowTextBox, <br> StatusText, <br> UAHint and <br> Validate. |

### Overview

- The **Style** property of the FolderBrowserDialog allows developers to customize the behavior and display options of the dialog based on specific requirements. By setting various flag options, developers can control what types of folders or resources are displayed, along with additional features like URLs or administrative shares.

### FolderBrowserDialog Style Options Explained

The various options of the **Style** property are described below:

- **RestrictToFilesystem** - Restricts selection to file system directories.
- **RestrictToSubfolders** - Returns only file system ancestors.
- **RestrictToDomain** - Excludes network folders below the domain level.
- **BrowseForComputer** - Displays only computers.
- **BrowseForEverything** - Displays files as well as folders.
- **BrowseForPrinter** - Displays only printers.
- **NewDialogStyle** - Uses the new resizable folder selection dialog.
- **AllowUrls** - Displays URLs. 'NewDialogStyle' and 'BrowseForEverything' must be set along with this flag.
- **ShowAdministrativeShares** - Displays administrative shares existing on the remote system.
- **ShowShares** - Displays shareable resources existing on the remote system.

### Usage Considerations

Developers should choose the appropriate combination of these flags based on the specific functionality required in their application. For example, if an application needs to allow users to browse shared resources over the network, both `ShowShares` and `BrowseForEverything` might be useful.

### Example Usage

Here’s an example of setting the `Style` property:

```csharp
FolderBrowserDialog folderDialog = new FolderBrowserDialog();
folderDialog.Style = FolderBrowserDialogStyle.RestrictToFilesystem | FolderBrowserDialogStyle.NewDialogStyle;
folderDialog.ShowDialog();
```

This code snippet demonstrates setting the `Style` property to restrict selection to filesystem directories and using the new resizable folder selection dialog.

### Conclusion

The `Style` property of the FolderBrowserDialog is a powerful tool for controlling how users interact with folder selection dialogs. By combining the appropriate flags, developers can fine-tune the behavior to meet the exact needs of their applications.

### API Reference

For a full list of available flags and detailed explanations, refer to the [Syncfusion WinForms documentation on FolderBrowserDialog](https://help.syncfusion.com/windowsforms).

### Code Examples

To incorporate these features into your application, you can use the following code snippet:

```csharp
using Syncfusion.Windows.Forms.Tools;

public void OpenFolderSelectionDialog()
{
    FolderBrowserDialog folderDialog = new FolderBrowserDialog();
    folderDialog.Style = FolderBrowserDialogStyle.RestrictToFilesystem | FolderBrowserDialogStyle.NewDialogStyle;
    if (folderDialog.ShowDialog() == DialogResult.OK)
    {
        string selectedPath = folderDialog.SelectedPath;
        // Additional logic to handle the selected path
    }
}
```

### Summary

The **Style** property of the FolderBrowserDialog allows for extensive customization of the dialog's functionality, enabling developers to tailor it to specific use cases such as file selection, network browsing, or administrative tasks.

<!-- tags: [Syncfusion, WindowsForms, FolderBrowserDialog, Style property, Development] keywords: [folder selection, dialog customization, network resources, file system, print selection, URL display, administrative shares, shareable resources] -->
```