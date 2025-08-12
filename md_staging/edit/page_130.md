```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: edit
page_number: 130
page_id: edit#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:13Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## External Configuration File

You can plug-in an external configuration file that defines a custom language to the Edit Control by using the `Configurator.Open` and `ApplyConfiguration` methods in conjunction, as shown in the below code snippet.

### [C#]
```csharp
// Plug-in an external configuration file.
this.editControl.Configurator.Open(configFile);

// Apply the configuration defined in the configuration file.
this.editControl.ApplyConfiguration("CustomLanguage");
```

### [VB.NET]
```vb
' Plug-in an external configuration file.
Me.editControl.Configurator.Open(configFile)

' Apply the configuration defined in the configuration file.
Me.editControl.ApplyConfiguration("CustomLanguage")
```

## Run Time Configuration Settings

Syntax Highlighting and Code Coloring can be implemented at run time by using the Language Coloring Configuration Editor.
```