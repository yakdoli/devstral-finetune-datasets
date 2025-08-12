<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_295.jpeg
document_name: edit
page_number: 295
page_id: edit#page_295
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:33Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
ILEXMLParser(), endParsePoint, endVirtualPoint.Y, endVirtualPoint.X, True)

Dim format As ISnippetFormat =
    editControl1.RegisterUnderlineFormat(Color.Red, UnderlineStyle.Wave, UnderlineWeight.Thick)
Me	editControl1.SetUnderline(startCoordinatePoint, endCoordinatePoint, format)
```

## 5.15 How To Plug-in an External Configuration Dile Into the Edit Control

The Edit Control supports the creation and plug-in of custom configuration files into the Edit Control for syntax coloring. The configuration file has to be in XML format, and as per the directions in the Configuration Settings section. The following code snippet illustrates how to plug-in an external configuration file.

### [C#]

```csharp
// Plug-In an external configuration file.
this.editControl1.Configurator.Open(" Configuration_File.xml ");
```

### [VB.NET]

```vb
' Plug-In an external configuration file.
Me.editControl1.Configurator.Open(" Configuration_File.xml ")
```

## 5.16 How To Programatically Display the Code Snippets

You can display the code snippets programmatically by using the `StreamEditControl` class of Edit Control. The following code snippet illustrates this.

### [C#]

```csharp
private void editControl1_ReadOnlyChanged(object sender, EventArgs e)
{
    edit = (StreamEditControl)sender;
}

private void menuItem15_Click(object sender, EventArgs e)
{
    edit.ShowCodeSnippets();
}
```

## Page-level Navigation/TOC (if applicable)
- 5.15 How To Plug-in an External Configuration Dile Into the Edit Control
- 5.16 How To Programatically Display the Code Snippets

## Cross References
See also: Edit Control, Syntax Coloring, Configuration Files, External Plugins

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Edit Control, Configuration, Syntax Coloring, Plugins] keywords: [Edit Control, Syntax Coloring, External Configuration, Plugins, Programmatic Display, Code Snippets, StreamEditControl] -->
