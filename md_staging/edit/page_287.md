```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_287.jpeg
document_name: edit
page_number: 287
page_id: edit#page_287
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:01Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- This page shows how to create custom formats and define ConfigLexems that belong to those formats in Syncfusion Winforms.
- It includes detailed C# and VB.NET code examples for defining lexems.
- Explains how to dynamically validate text using the TextChanged event.

## Content

The following code snippet illustrates how to create Custom Formats and define ConfigLexems that belong to those Formats.

### C#
```csharp
// Create a format and set its attributes
ISnippetFormat formatMethod = this.editControl1.Language.Add("MethodName");
formatMethod.FontColor = Color.HotPink;
formatMethod.Font = new Font("Garamond", 12);

// Create a lexem that belongs to this format
ConfigLexem configLex = new ConfigLexem("Method[0-9]*", "", 
    FormatType.Custom, false);
configLex.IsBeginRegex = true;
configLex.FormatName = "MethodName";

// Add it to the current language's lexems collection
this.editControl1.Language.Lexems.Add(configLex);
this.editControl1.Language.ResetCaches();
```

### VB.NET
```vb
' Create a format and set its properties
Dim formatMethod As ISnippetFormat = 
    Me.editControl1.Language.Add("MethodName")
formatMethod.FontColor = Color.HotPink
formatMethod.Font = New Font("Garamond", 12)

' Create a lexem that belongs to this format
Dim configLex As New ConfigLexem("Method[0-9]*", "", FormatType.Custom, 
    False)
configLex.IsBeginRegex = True
configLex.FormatName = "MethodName"

' Add it to the current language's lexems collection 
Me.editControl1.Language.Lexems.Add(configLex)
Me.editControl1.Language.ResetCaches()
```

### 5.8 How To Dynamically Validate Text Using the TextChanged Event

Text can be validated dynamically by using the `TextChanged` event and a Timer. The validation routine is invoked in response to a brief pause by the user while typing. The following code snippet illustrates this.

## Page-level Navigation/TOC (if applicable)
- [5.8 How To Dynamically Validate Text Using the TextChanged Event](#5.8-how-to-dynamically-validate-text-using-the-textchanged-event)

## Cross References
- See also: [TextChanged Event Documentation](#textchanged-event-documentation), [Timer Control Documentation](#timer-control-documentation)

<!-- tags: [Syncfusion Winforms, TextChanged Event, ConfigLexems, Custom Formats, Validation] keywords: [editControl, lexems, dynamic validation, custom formats, textChanged, timer] -->
```