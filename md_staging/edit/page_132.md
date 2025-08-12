```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_132.jpeg
document_name: edit
page_number: 132
page_id: edit#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:01:39Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Set language configuration instance object.
this.editControl.Configurator = editConfig.Configurator;

// Applies coloring of the specified language to the text.
this.editControl.ApplyConfiguration(newLang);
}
}
```

### [VB.NET]

```vb
Dim activeLang As IConfigLanguage = Me.EditControl.Parser.Formats

' Create an instance of ConfigurationDialog.
Dim editConfig As New frmConfigDialog(Me.editControl.Configurator, activeLang)

If editConfig.ShowDialog(Me) = DialogResult.OK AndAlso Not (activeLang Is Nothing) Then
    Dim newLang As IConfigLanguage =
    If(editConfig.Configurator.KnownLanguageNames.Contains(activeLang.Language), 
       editConfig.Configurator(activeLang.Language), 
       editConfig.Configurator.DefaultLanguage)
    If Not (newLang Is Nothing) Then
        ' Set language configuration instance object.
        Me.editControl1.Configurator = editConfig.Configurator

        ' Applies coloring of the specified language to the text.
        Me.editControl1.ApplyConfiguration(newLang)
    End If
End If
```

A sample which demonstrates the above features is available in the below sample installation path.

**..\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Edit.Windows\Samples\2.0\Syntax Highlighting\CustomConfigFileDemo**

## See Also

- Creating a Custom Language Configuration File

### 4.5.1 XML Based Configuration Files

<!-- tags: [Windows Forms, Syntax Highlighting, Language Configuration, Custom Config File, XML] keywords: [language configuration, coloring, text, editcontrol, configurator, configuration, active language, default language, custom config file, xml] -->
```