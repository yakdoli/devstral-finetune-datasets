```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_128.jpeg
document_name: edit
page_number: 128
page_id: edit#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:18Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Demonstrates configuring language settings for the Edit Control in Syncfusion WinForms.
- Examples include setting various languages such as Pascal, HTML (light), VB.NET, XML, and C#.
- Illustrates both using array indexing and file extensions to select languages.

## Content

### Language Configuration for the Edit Control

```csharp
// Set the Edit Control to use the configuration settings for Pascal.
this.editControl.ResetColoring(this.editControl.Configurator.KnownLanguages[2] as IConfigLanguage);

// Set the Edit Control to use the configuration settings for Pascal using the file extension.
this.editControl.ResetColoring(this.editControl.Configurator.GetLanguage("pas") as IConfigLanguage);

// Set the Edit Control to use the configuration settings for HTML (light).
this.editControl.ResetColoring(this.editControl.Configurator.KnownLanguages[3] as IConfigLanguage);

// Set the Edit Control to use the configuration settings for HTML (light) using the file extension.
this.editControl.ResetColoring(this.editControl.Configurator.GetLanguage("html") as IConfigLanguage);

// Set the Edit Control to use the configuration settings for VB.NET.
this.editControl.ResetColoring(this.editControl.Configurator.KnownLanguages[4] as IConfigLanguage);

// Set the Edit Control to use the configuration settings for VB.NET using the file extension.
this.editControl.ResetColoring(this.editControl.Configurator.GetLanguage("vb") as IConfigLanguage);

// Set the Edit Control to use the configuration settings for XML.
this.editControl.ResetColoring(this.editControl.Configurator.KnownLanguages[5] as IConfigLanguage);

// Set the Edit Control to use the configuration settings for XML using the file extension.
this.editControl.ResetColoring(this.editControl.Configurator.GetLanguage("xml") as IConfigLanguage);

// Set the Edit Control to use the configuration settings for C#.
this.editControl.ResetColoring(this.editControl.Configurator.KnownLanguages[6] as IConfigLanguage);

// Set the Edit Control to use the configuration settings for C# using the file extension.
this.editControl.ResetColoring(this.editControl.Configurator.GetLanguage("cs") as IConfigLanguage);
```

### VB.NET Example

```vb
' Set the Edit Control to use the configuration settings for the default
```

## API Reference

### ResetColoring Method

- **Description**: Resets the colorization settings of the Edit Control based on the specified language configuration.
- **Parameters**:
  - `IConfigLanguage`: The language configuration to apply to the Edit Control.

## Code Examples

### C# Example

```csharp
this.editControl.ResetColoring(this.editControl.Configurator.GetLanguage("html") as IConfigLanguage);
```

### VB.NET Example

```vb
editControl.ResetColoring(editControl.Configurator.GetLanguage("html") as IConfigLanguage)
```

## Cross References

- [Previous Page: Overview of Edit Control](#overview)
- [Next Page: Customizing Syntax Highlighting](#customizing-syntax-highlighting)

<!-- tags: [Syncfusion, WinForms, EditControl, LanguageConfiguration, KnownLanguages, FileExtensions] keywords: [resetcoloring, configlanguage, syntaxhighlighting, configurationsettings, html, vbnet, xml, csharp, languageconfigurator] -->
```