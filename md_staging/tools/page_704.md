```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_704.jpeg
document_name: tools
page_number: 704
page_id: tools#page_704
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Detailed description of the FolderBrowser control and its text settings.
- Explanation of the Description property and how it affects the text displayed in the FolderBrowser control.
- Examples provided in C# and VB.NET to demonstrate setting the Description property.

## Content

### Text Settings

The text settings of the FolderBrowser control are described below.

#### Setting Text in FolderBrowser

The text for the FolderBrowser can be set using the below given property.

| FolderBrowser Property | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| Description            | Gets / sets the text displayed above the tree control in the FolderBrowser Dialog. |

#### Description Property

The **Description** property of the FolderBrowser supports the 'AutoComplete' feature, that provides options that can be used to complete text even before it is entered.

##### C# Example

```csharp
this.folderBrowser1.Description = "Recent Documents";
```

##### VB.NET Example

```vb
Me.folderBrowser1.Description = "Recent Documents"
```

## API Reference

- **Property**: `Description`
  - **Type**: `string`
  - **Description**: Gets or sets the text displayed above the tree control in the FolderBrowser Dialog.
  - **Default**: Empty string

## Code Examples

### C#

```csharp
this.folderBrowser1.Description = "Recent Documents";
```

### VB.NET

```vb
Me.folderBrowser1.Description = "Recent Documents"
```

## Cross References

- See also: FolderBrowser control documentation for additional properties and methods.
- References to related controls and features within the Syncfusion.Windows.Forms.Tools namespace.

### Additional Notes

- The Description property supports AutoComplete, facilitating easier text entry for users.
- Ensure that the appropriate using directive is included in your project to use the FolderBrowser control.

<!-- tags: [FolderBrowser, Syncfusion, WindowsForms, AutoComplete, TextSettings, C# example, VB.NET example] keywords: [FolderBrowser control, text settings, Description property, AutoComplete feature, example code] -->
```