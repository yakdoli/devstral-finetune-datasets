```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: edit
page_number: 159
page_id: edit#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:35Z
fidelity: lossless
-->

## Code Snippets Feature

### Overview
- Demonstrates how to show code snippets using the `ShowCodeSnippets()` method in both C# and VB.NET.
- Explains how to set the border for active code snippets using the `DrawCodeSnippetBorder` property.

### Code Examples

#### C#
```csharp
// Shows the code snippets' choice list.
this.editControl1.ShowCodeSnippets();
```

#### VB.NET
```vbnet
' Shows the code snippets' choice list.
Me.editControl1.ShowCodeSnippets()
```

### Border Settings

The border for active code snippets can be set using the `DrawCodeSnippetBorder` property of the Edit Control.

#### C#
```csharp
this.editControl1.DrawCodeSnippetBorder = true;
```

#### VB.NET
```vbnet
Me.editControl1.DrawCodeSnippetBorder = True
```

### Sample Path
A sample demonstrating the above feature is available at the following installation path:

```
.. \My Documents \Syncfusion \EssentialStudio \Version Number \Windows \Edit.Windows \Samples \2.0 \ IntelliSense Functions \ ContextSnippetsDemo
```

### Context Choice

#### Overview
- Explains the Context Choice support, which allows you to create pop-ups for displaying a list of options to complete the user's input.
- Discusses how this feature is modeled on the `List Members` IntelliSense feature of Visual Studio and its use in programming languages.

#### Features
- **Pop-up Display**: After typing a period (.) after a class name in C# or VB.NET, a pop-up lists all class members.
- **Dynamic Selection**: The list automatically selects and highlights the appropriate member as you type.
- **Autocomplete**: Using the UP/DOWN ARROW keys, you can select a Context Choice item and press TAB to autocomplete.
- **Dismissal**: Pressing the ESC key dismisses the Context Choice pop-up.

<!-- tags: [Syncfusion Winforms, ContextChoice, IntelliSense, BorderSettings, CodeSnippets, ContextChoiceFeature, EditControl] keywords: [Context Choice, List Members, IntelliSense, Class Members, AutoComplete, Pop-up, ESC] -->
```
