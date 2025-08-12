```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_140.jpeg
document_name: edit
page_number: 140
page_id: edit#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:05Z
fidelity: lossless
-->

## WinForms Find and Replace Feature

The following table outlines the functionality of various find and replace operations in the `editControl` of Syncfusion WinForms:

| Function | Description |
|----------|-------------|
| FindCurrentText | Finds the next occurrence of the word on which the cursor is presently on. |
| FindNext | Finds the next occurrence of the current search text. |
| ReplaceAll | Replaces all occurrences of the search text with the replacement text as per the conditions specified like match case, match whole word, search hidden text, and search up. |

### Code Examples

#### C#

```csharp
// Finds the first occurrence of the specified text as per the conditions specified.
this.editControl.FindText("Essential Edit", true, true, true, true, null);

// Searches for given string in the text of control and returns text range of first found occurrence.
this.editControl.FindRange(searchString, startLocation, endLocation,
    matchWholeWord, searchHiddenText, searchUp, useRegex);

// Looks for specified expression in text.
this.editControl.FindRegex(startLine, startColumn, expression,
    bSearchInCollapsed, searchUp);

// Replaces the first occurrence of the specified text with the replacement text as per the conditions specified.
this.editControl.ReplaceText("ShowVerticalScrollbar",
    "ShowVerticalScroller");

// Finds the next occurrence of the word on which the cursor is presently on.
this.editControl.FindCurrentText();

// Finds the next occurrence of the current search text.
this.editControl.FindNext();

// Replaces all occurrences of the search text with the replacement text as per the conditions specified.
this.editControl.ReplaceAll(" Drag-and-drop",
    "Drag and drop");
```

#### VB.NET

```vb
' Finds the first occurrence of the specified text as per the conditions specified.
Me.editControl.FindText("Essential Edit", True, True, True, True, Nothing)

' Searches for given string in the text of control and returns text range of
```
<!-- tags: [Syncfusion, WinForms, find, replace, essential edit, match case, match whole word, search hidden text, search up] keywords: [findcurrenttext, findnext, replaceall, search text, replace text, text range, search hidden text, search up, regex, control text, essential edit, findText, findRange, findRegex, replaceText] -->
```