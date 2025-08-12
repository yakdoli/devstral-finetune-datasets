```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: edit
page_number: 131
page_id: edit#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:01Z
fidelity: lossless
-->


# **Essential Edit for Windows Forms**

## Overview
- This page demonstrates how to use the Language Coloring Configuration Editor in a Windows Forms application.
- It explains how to programmatically invoke the Configuration Customization Dialog Box for customizing syntax highlighting settings.

## Content

### Figure 43: Configuration Customization Dialog Box

The Language Coloring Configuration Editor can be invoked programmatically as follows:

#### **C#**
```csharp
IConfigLanguage activeLang = this.editControl.Parser.Formats as IConfigLanguage;

// Create an instance of ConfigurationDialog.
ConfigurationDialog editConfig = new ConfigurationDialog(this.editControl.Configurator, activeLang);
if (editConfig.ShowDialog(this) == DialogResult.OK && activeLang != null)
{
    IConfigLanguage newLang =
        editConfig.Configurator.KnownLanguageNames.Contains(activeLang.Language) ?
            editConfig.Configurator[activeLang.Language] :
            editConfig.Configurator.DefaultLanguage;
    if (newLang != null)
    {
        // Additional custom logic can be added here.
    }
}
```

### Explanation
- The `IConfigLanguage` instance represents the active language in the editor.
- The `ConfigurationDialog` is used to display the configuration editor dialog.
- The `ShowDialog` method opens the dialog, and if the user clicks "OK," the new configuration settings are applied.

## Cross References
- Refer to the full user guide for more detailed explanations and examples of configuration dialog customization.

<!-- tags: [windowsforms, configurationeditor, syntaxhighlighting, editcontrol, csharp] keywords: [configurationdialog, IConfigLanguage, Language Coloring Configuration Editor, DialogBox, C#] -->
```