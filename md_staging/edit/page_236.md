```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_236.jpeg
document_name: edit
page_number: 236
page_id: edit#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:40Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates the localization functionality of the Edit Control in Windows Forms.
- Explains how to localize dialog boxes associated with the Edit Control to any desired language.
- Provides a step-by-step guide to localizing the Neutral Resource files.

## Content

![Find dialog localized to Spanish](#)
**Figure 79: Find dialog localized to Spanish**

The Edit Control supports complete localization of all dialog boxes associated with it to any desired language. The Neutral Resource files for the Edit Control are available in the directory `Edit.Windows\Src\LocalizationSet`. Follow the steps below to localize the Neutral Resources files:

### Steps to Localize Neutral Resources Files

1. **Locate Neutral Resources**
   - The neutral resource of every Syncfusion Edit Control is present in the Localization folder of the Edit.Windows source code.
   - Assuming `C:\Program Files\` is the installation path for the Syncfusion components, the path is:
     ```
     C:\Program Files\Syncfusion\Essential Studio\x.x.x.x\Windows\Edit.Windows\Src\LocalizationSet v1.1
     ```

2. **Inside the LocalizationSet Folder**
   - There will be a number of resource files corresponding to the various dialog boxes of the Edit Control package.
   - These resources will contain the form representation of English (Default & Neutral) culture.

3. **Open WinRes**
   - Open WinRes from the following location:
     ```
     C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\bin\winRes.exe
     ```

4. **Use WinRes**
   - WinRes is used to work with the Windows Forms resources.
   - The ResEdit tool cannot be used to edit Windows Forms resources because it can be used to work with image and string-based resources only.

5. **Replace English Strings**
   - Open the resources using the WinRes utility and replace the English strings with the culture equivalent.

### Example of Localization
For example, the following figure shows the `Syncfusion.Windows.Forms.Edit.Dialogs.frmFindDialog.resources` file that is opened in the WinRes tool, showing strings in German (strings are converted using some language converter).

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Edit
- **Class**: Dialogs
- **Method**: frmFindDialog.resources

### Parameters
- **Neutral Resource Files**
  - Located in the `LocalizationSet` folder.
  - Format: `.resources` file.

### Example

```csharp
// Example of using WinRes to localize resources
string culture = "de-DE"; // German culture
LocalizationTools.LocalizeResource("frmFindDialog.resources", culture);
```

## Code Examples

### C# Example
```csharp
using Syncfusion.Windows.Forms.Edit;
using System.Resources;

// Assuming you have the Neutral Resource files and WinRes is set up
public void LocalizeFindDialog()
{
    // Replace English strings with German equivalents
    string germanStrings = "German equivalents here"; // Placeholder for actual German strings
    LocalizationTools.LocalizeResource("frmFindDialog.resources", "de-DE", germanStrings);
}
```

## Cross References
- See also: "Localization Overview for Syncfusion Controls"
- Reference: "Edit Control Documentation"

<!-- tags: localization, editcontrol, windowsforms, resources, localizationset, winres, culture, syncfusion, 11.4.0.26 -->
```