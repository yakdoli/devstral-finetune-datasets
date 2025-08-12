```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_129.jpeg
document_name: edit
page_number: 129
page_id: edit#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:25Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to set the configuration settings for different programming languages and file extensions using the `ResetColoring` method.
- Highlights the configuration settings for SQL, Pascal, HTML (light), VB.NET, XML, and C#.
- Details the use of file extensions to configure the editing environment for specific language syntax highlighting.

## Content

### Setting Configuration Settings

The `ResetColoring` method is used to set the configuration settings for the `Edit Control` to appropriately highlight syntax for various languages and file types. Below are examples of configuring the `Edit Control` for different languages and file extensions:

```vb
' language.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.KnownLanguages(0))
' Set the Edit Control to use the configuration settings for SQL.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.KnownLanguages(1))
' Set the Edit Control to use the configuration settings for SQL using the file extension.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.GetLanguage("sql"))
```

#### Pascal
```vb
' Set the Edit Control to use the configuration settings for Pascal.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.KnownLanguages(2))
' Set the Edit Control to use the configuration settings for Pascal using the file extension.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.GetLanguage("pas"))
```

#### HTML (light)
```vb
' Set the Edit Control to use the configuration settings for HTML (light).
Me.editControl1.ResetColoring(Me.editControl1.Configurator.KnownLanguages(3))
' Set the Edit Control to use the configuration settings for HTML using the file extension.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.GetLanguage("html"))
```

#### VB.NET
```vb
' Set the Edit Control to use the configuration settings for VB.NET.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.KnownLanguages(4))
' Set the Edit Control to use the configuration settings for VB.NET using the file extension.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.GetLanguage("vb"))
```

#### XML
```vb
' Set the Edit Control to use the configuration settings for XML.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.KnownLanguages(5))
' Set the Edit Control to use the configuration settings for XML using the file extension.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.GetLanguage("xml"))
```

#### C#
```vb
' Set the Edit Control to use the configuration settings for C#.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.KnownLanguages(6))
' Set the Edit Control to use the configuration settings for C# using the file extension.
Me.editControl1.ResetColoring(Me.editControl1.Configurator.GetLanguage("cs"))
```

## API Reference

- **`ResetColoring` Method**
  - **Purpose**: Resets the syntax highlighting configuration for the `Edit Control` based on the specified language.
  - **Parameters**:
    - **Language**: The `LanguageDto` object representing the language configuration.
  - **Returns**: None.

<!-- tags: [Syncfusion, Winforms, Edit Control, Syntax Highlighting, Configuration Settings, KnownLanguages, GetLanguage] keywords: [Edit Control, Syntax Highlighting, Configuration Settings, file extension, language configuration, html, vb.net, xml, c#, pascal, sql] -->
```