```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_028.jpeg
document_name: edit
page_number: 028
page_id: edit#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:32Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to create a new configuration language and apply it to an Edit Control.
- Shows how to define custom format objects and their attributes using the `Language.Add` method.
- Explains the process of creating a `ConfigLexem` object belonging to a defined format.

## Content

### Create a New Configuration Language and Apply It

#### C#
```csharp
// Create a new configuration language and apply the same to the contents of the Edit Control.
IConfigLanguage currentConfigLanguage = 
    this.editControl1.Configurator.CreateLanguageConfiguration(newConfigLanguage);
this.editControl1.ApplyConfiguration(currentConfigLanguage);
```

#### VB.NET
```vbnet
' Create a new configuration language and apply the same to the contents of the Edit Control.
Dim currentConfigLanguage As IConfigLanguage = 
    Me.editControl1.Configurator.CreateLanguageConfiguration(NewConfigLanguage)
Me.editControl1.ApplyConfiguration(currentConfigLanguage)
```

#### Create a Custom Format Object and Define Its Attributes

2. **Create a custom format object by using the `Language.Add` method of the Edit Control and define its attributes.**

#### C#
```csharp
// Creating a custom format object.
ISnippetFormat formatMethod = this.editControl1.Language.Add("CodeBehind");

// Defining its attributes.
formatMethod.FontColor = Color.IndianRed;
formatMethod.Font = new Font("Garamond", 12);
formatMethod.BackColor = Color.Yellow;
```

#### VB.NET
```vbnet
' Creating a custom format object.
Dim formatMethod As ISnippetFormat = 
    Me.EditControl1.Language.Add("CodeBehind")

' Defining its attributes.
formatMethod.FontColor = Color.IndianRed
formatMethod.Font = New Font("Garamond", 12)
formatMethod.BackColor = Color.Yellow
```

### Create a ConfigLexem Object

3. **Create a `ConfigLexem` object that belongs to the above defined format and define its attributes.**

#### C#
```csharp
// [Implementation details for creating a ConfigLexem object will be continued]
```

### Summary

This section illustrates the process of configuring the `EditControl` in Syncfusion Winforms by creating a new configuration language, defining custom format objects, and specifying the attributes for these formats. These configurations allow for enhanced customization and control over the appearance and behavior of the `EditControl`.

## Page Navigation
- **Previous:** [EditControl Properties and Methods](page_027)
- **Next:** [Advanced Formatting and Lexical Analysis](page_029)

<!-- tags:yncfusion winforms, edit control, configuration language, custom format objects, configlexem, attributes, properties, methods, lexical analysis keywords: Syncfusion.Winforms, edit, configuration, format, attributes, lexeme -->
```