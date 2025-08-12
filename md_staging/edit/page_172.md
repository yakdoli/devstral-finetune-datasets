```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: edit
page_number: 172
page_id: edit#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:50Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Covers operations related to the Edit Control in Syncfusion WinForms.
- Demonstrates setting a custom size for the Context Prompt window.
- Explains the events provided by the Edit Control for managing Context Prompt operations.

## Content

### Context Prompt Operations

The Edit Control provides the following set of events for performing Context Prompt operations.

| Edit Control Event              | Description                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------|
| ContextPromptBeforeOpen         | This event occurs when the Context Prompt window is about to open. User can cancel it.               |
| ContextPromptClose              | This event occurs when the Context Prompt window has been closed.                                   |
| ContextPromptSelectionChanged   | This event occurs when a Context Prompt item has been selected.                                     |

#### Code Example in VB.NET

```vb
Me.editControl1.ContextPromptSize = New System.Drawing.Size(125, 75)
Me.editControl1.UseCustomSizeContextPrompt = True
```

#### Code Example in C#

```csharp
// Store the lexem name invoking the ContextPrompt popup.
string contextPromptLexem = "";

private void editControl1_ContextPromptBeforeOpen(object sender, System.ComponentModel.CancelEventArgs e)
{
    ILexem lex;
    ILexemLine lexemLine =
        this.editControl1.GetLine(this.editControl1.CurrentLine);

    // Gets the index of the current word in that line.
    int ind = GetContextPromptCharIndex(lexemLine);

    if (ind <= 0)
    {
        e.Cancel = true;
        return;
    }

    lex = lexemLine.LineLexems[ind - 1] as ILexem;

    // If the count is less than '2', do not show the Context Prompt popup.
    if (lexemLine.LineLexems.Count < 2)
        e.Cancel = true;
}
```

## Page-level Navigation/TOC
- Context Prompt Operations
- Edit Control Events
  - ContextPromptBeforeOpen
  - ContextPromptClose
  - ContextPromptSelectionChanged

## Cross References
- See also: related sections or pages with similar content, if available in the document.

<!-- tags: [syncfusion, winforms, edit control, context prompt, events] keywords: [Edit Control, Context Prompt, ContextPromptBeforeOpen, ContextPromptClose, ContextPromptSelectionChanged] -->
```