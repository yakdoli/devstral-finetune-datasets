```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: edit
page_number: 127
page_id: edit#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:45Z
fidelity: lossless
-->

## Overview

- Configuring syntax highlighting or editing settings using `ApplyConfiguration` and `ResetColoring` methods.
- Support for loading configuration settings for various languages using different methods like KnownLanguages enumerator, file extensions, or indexes.
- Examples in both C# and VB.NET for setting the Edit Control to use configuration settings.

## Content

[C#]

```csharp
this.editControl.ApplyConfiguration(this.editControl.Configurator.KnownLanguages[1] as IConfigLanguage);

// Using the name of the language in the associated configuration file.
IConfigLanguage config = this.editControl.Configurator.GetLanguage("sql") as IConfigLanguage;
this.editControl.ApplyConfiguration(config.Language);
```

### [VB.NET]

```vb
' Considering configuration settings for SQL as an example.
' Using the KnownLanguages enumerator.
Me.editControl.ApplyConfiguration(KnownLanguages.SQL)

' Using the file extension of the associated language.
Me.editControl.ApplyConfiguration(Me.editControl.Configurator.GetLanguage("sql"))

' Using the associated index in the KnownLanguages collection.
Me.editControl.ApplyConfiguration(Me.editControl.Configurator.KnownLanguageNames(1))

' Using the name of the language in the associated configuration file.
Dim config As IConfigLanguage = Me.EditControl.Configurator.GetLanguage("sql")
Me.editControl.ApplyConfiguration(config.Language)
```

You can also load any of the configuration settings by using the `ResetColoring` method, as shown in the code below.

### [C#]

```csharp
// Set the Edit Control to use the configuration settings for the default language.
this.editControl.ResetColoring(this.editControl.Configurator.KnownLanguages[0] as IConfigLanguage);

// Set the Edit Control to use the configuration settings for SQL.
this.editControl.ResetColoring(this.editControl.Configurator.KnownLanguages[1] as IConfigLanguage);

// Set the Edit Control to use the configuration settings for SQL using the file extension.
this.editControl.ResetColoring(this.editControl.Configurator.GetLanguage("sql") as IConfigLanguage);
```

## API Reference

### Methods

- **ApplyConfiguration(IConfigLanguage language)**: Applies the configuration settings for the specified language.
- **ResetColoring(IConfigLanguage language)**: Resets the configuration settings of the Edit Control.

### Classes

- **IConfigLanguage**: Represents a configuration language for the Edit Control.
- **Configurator**: Provides methods to access and configure known languages.

### Properties (within Configurator)

- **KnownLanguages**: Collection of supported languages.
- **GetLanguage(String extension)**: Retrieves the configuration language based on the specified file extension.

## Tags and Keywords
<!-- tags: [syncfusion, winforms, edit control, configuration, syntax highlighting, known languages] keywords: [ApplyConfiguration, ResetColoring, IConfigLanguage, Configurator, KnownLanguages] -->
```