```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_700.jpeg
document_name: tools
page_number: 700
page_id: tools#page_700
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:16Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The following are the valid enumeration values for `FolderBrowserFolder.StartLocation` property:

| Enumeration Name                           | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| CommonMusic                                | Represents a predefined start location for the FolderBrowserDialog. |
| CommonPictures                             | Represents a predefined start location for the FolderBrowserDialog. |
| CommonVideo                                | Represents a predefined start location for the FolderBrowserDialog. |
| Resources                                  | Represents a predefined start location for the FolderBrowserDialog. |
| ResourcesLocalized                         | Represents a predefined start location for the FolderBrowserDialog. |
| CommonOemLinks                             | Represents a predefined start location for the FolderBrowserDialog. |
| CDBurnArea                                | Represents a predefined start location for the FolderBrowserDialog. |
| ComputersNearMe                            | Represents a predefined start location for the FolderBrowserDialog. |
| CustomStartLocation                        | Represents a custom start location for the FolderBrowserDialog.    |
| FlagPerUserInit                            | Represents a flag indicating preferences are set on a per-user basis. |
| FlagNoAlias                                | Represents a flag indicating no alias handling for the selected location. |
| FlagDontVerify                             | Represents a flag indicating no verification for the selected location. |
| FlagCreate and FlagMask                    | Represents flags for additional options related to folder creation and masking. |
| **CustomStartLocation**                    | Gets / sets custom start location for showing the dialog.                     |
| **SelectLocation**                         | Gets / sets the selected location for showing the dialog.                     |
| **DirectoryPath**                          | Retrieves the location of the selected folder.                                  |

### Note: For the `SelectLocation` property to take effect, the `StartLocation` property must be set to `CustomStartLocation`.

#### Code Example

```csharp
// Set the enumeration value FolderBrowserFolder.CustomStartLocation
// for Folder.StartLocation property.
this.folderBrowser1.StartLocation = 
    Syncfusion.Windows.Forms.FolderBrowserFolder.CustomStartLocation;
this.folderBrowser1.CustomStartLocation = "C:";

// SelectLocation property for Automatic Scroll and Highlight of 
// desired path.
this.folderBrowser1.SelectLocation = "C:\\Program 
Files\\Syncfusion\\Essential Studio";
```

<!-- tags: [FolderBrowserFolder, CustomStartLocation, SelectLocation, DirectoryPath, Syncfusion.Windows.Forms] keywords: [CustomStartLocation, SelectLocation, DirectoryPath, FolderBrowserDialog, EnumerationValues] -->
```