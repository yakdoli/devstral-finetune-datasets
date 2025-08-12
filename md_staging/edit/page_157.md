<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_157.jpeg
document_name: edit
page_number: 157
page_id: edit#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:19Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to extract and add code snippets in C# and VB.NET using the `CodeSnippetsExtractor` class.
- Explains the process of adding new code snippets to the current language of the Edit Control.
- Details the use of `SnippetContainer` for organizing and displaying code snippets in containers.

## Content

This is illustrated in the code given below.

### Extracting Code Snippets

[C#]

```csharp
CodeSnippetsExtractor.Extract(csharpsnippetsPath, editControl1);
```

[VB.NET]

```vb
CodeSnippetsExtractor.Extract(vbsnippetsPath, editControl1)
```

### Adding Code Snippets

Code Snippets are added to the current language of the Edit Control by using the below given method.

| Edit Control Method       | Description                                     |
|---------------------------|-------------------------------------------------|
| AddCodeSnippet            | Adds new code snippet to current language.     |

[C#]

```csharp
this.editControl1.AddCodeSnippet(string title, ArrayList literals, string code);
```

[VB.NET]

```vb
Me.editControl1.AddCodeSnippet(String title, ArrayList literals, String code)
```

### Using Snippet Containers

The code snippets can also be contained in containers and displayed in the pop-up of the snippets. The static `Extract` method of the `CodeSnippetsExtractor` class is used to extract and fill the container object. The container object can be added to the `SnippetsContainer` of the Edit Control by using the `AddContainer` method. This is illustrated in the code given below.

[C#]

```csharp
private CodeSnippetsContainer container = new Syncfusion.Windows.Forms.Edit.Utils.CodeSnippets.CodeSnippetsContainer();
container = CodeSnippetsExtractor.Extract(csharpsnippetsPath@"\Loops");
container.Name = "Loops";
this.editControl1.Language.SnippetsContainer.AddContainer(container);
```

[VB.NET]

```vb
Dim container As CodeSnippetsContainer = New Syncfusion.Windows.Forms.Edit.Utils.CodeSnippets.CodeSnippetsContainer()
```

## API Reference

### Methods
- `CodeSnippetsExtractor.Extract(path, editControl)`
- `EditControl.AddCodeSnippet(title, literals, code)`
- `EditControl.Language.SnippetsContainer.AddContainer(container)`

## Code Examples

### C#
```csharp
private CodeSnippetsContainer container = new Syncfusion.Windows.Forms.Edit.Utils.CodeSnippets.CodeSnippetsContainer();
container = CodeSnippetsExtractor.Extract(csharpsnippetsPath@"\Loops");
container.Name = "Loops";
this.editControl1.Language.SnippetsContainer.AddContainer(container);
```

### VB.NET
```vb
Dim container As CodeSnippetsContainer = New Syncfusion.Windows.Forms.Edit.Utils.CodeSnippets.CodeSnippetsContainer()
```

## Cross References
- [See also: CodeSnippetsExtractor, Edit Control, SnippetContainer]

### Conclusion
The functionality allows for the seamless integration of code snippets into the Syncfusion Edit Control, enhancing productivity by providing quick access to commonly used code fragments.

<!-- tags: [Syncfusion Winforms, Edit Control, CodeSnippetsExtractor, CodeSnippetsContainer] keywords: [Extract, AddCodeSnippet, SnippetContainer, Language, Edit Control, VB.NET, C#, container, snippets] -->