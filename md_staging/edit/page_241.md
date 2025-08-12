```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_241.jpeg
document_name: edit
page_number: 241
page_id: edit#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:10Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes the `CodeSnippetTemplateTextChanging` event raised when the text of a code snippet template member is about to change.
- Provides details on handling the event with a sample implementation in C# and VB.NET.

## Content

### 4.14.3.3 CodeSnippetTemplateTextChanging Event

This event is raised when the text of the code snippet template member is to be changed.

The event handler receives an argument of type `CodeSnippetTemplateTextChangingEventArgs`. The following `CodeSnippetTemplateTextChangingEventArgs` members provide information specific to this event:

| Member                     | Description                                      |
|----------------------------|--------------------------------------------------|
| Cancel                     | Indicates whether action has to be canceled.    |
| CodeSnippet                | Code snippet that is currently activated.        |
| NewText                    | New text.                                        |
| TemplateMemberName        | Name of template member that is to be changed.   |

### C#

```csharp
// Change the text of all template members with defined name of currently
// activated code snippet.
this.editControl.ChangeSnippetTemplateText(" old member name", " new text");

// Handle the CodeSnippetTemplateTextChanging event.
this.editControl.CodeSnippetTemplateTextChanging += new
Syncfusion.Windows.Forms.Edit.CodeSnippetTemplateTextChangingHandler(editControl_CodeSnippetTemplateTextChanging);

private void editControl_CodeSnippetTemplateTextChanging(object sender,
Syncfusion.Windows.Forms.Edit.CodeSnippetTemplateTextChangingEventArgs e)
{
    // The below line will be displayed in the output window at runtime.
    Console.WriteLine(" CodeSnippetTemplateTextChanging event is raised ");
}
```

### VB.NET

```vbnet
' Change the text of all template members with defined name of currently
' activated code snippet.
Me.editControl.ChangeSnippetTemplateText(" old member name", " new text")

' Handle the CodeSnippetTemplateTextChanging event.
Me.editControl.CodeSnippetTemplateTextChanging += New
```

## Code Examples

### C#

```csharp
this.editControl.ChangeSnippetTemplateText(" old member name", " new text");
this.editControl.CodeSnippetTemplateTextChanging += new
Syncfusion.Windows.Forms.Edit.CodeSnippetTemplateTextChangingHandler(editControl_CodeSnippetTemplateTextChanging);

private void editControl_CodeSnippetTemplateTextChanging(object sender,
Syncfusion.Windows.Forms.Edit.CodeSnippetTemplateTextChangingEventArgs e)
{
    Console.WriteLine(" CodeSnippetTemplateTextChanging event is raised ");
}
```

### VB.NET

```vbnet
Me.editControl.ChangeSnippetTemplateText(" old member name", " new text")
Me.editControl.CodeSnippetTemplateTextChanging += New
```

<!-- tags: [Syncfusion Winforms, CodeSnippetTemplateTextChanging, Event, C#, VB.NET, Version 11.4.0.26] keywords: [code snippet, template text, text changing, event handler, event arguments, Syncfusion.Windows.Forms.Edit, CodeSnippetTemplateTextChangingEventArgs] -->
```