```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: edit
page_number: 141
page_id: edit#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:15Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Provides detailed methods for searching and replacing text in a document.
- Includes examples of using various methods in the `editControl` for different search and replace functionalities.
- Highlights the support for enhanced Find and Replace dialog boxes under advanced features.

## Content

### Search Methods

```vb
Me.editControl1.FindRange(searchString, startLocation, endLocation, matchWholeWord, searchHiddenText, searchUp, useRegex)
' Looks for specified expression in text.
Me.editControl1.FindRegex(startLine, startColumn, expression, bSearchInCollapsed, searchUp)
' Replaces the first occurrence of the specified text with the replacement text as per the conditions specified.
Me.editControl1.ReplaceText("ShowVerticalScrollbar", "ShowVerticalScroller")
' Finds the next occurrence of the word on which the cursor is presently on.
Me.editControl1.FindCurrentText()
' Finds the next occurrence of the current search text.
Me.editControl1.FindNext()
' Replaces all occurrences of the search text with the replacement text as per the conditions specified.
Me.editControl1.ReplaceAll("Drag-and-drop", "Drag and drop")
```

#### Figure: "FindText" method

![EditControl Sample](https://example.com/editcontrol_sample.png)  
*Figure 46: "FindText" method*

### Find and Replace Dialog Boxes

Edit Control also supports advanced and customizable Find and Replace dialog boxes. The Find dialog box is invoked by using the `ShowFindDialog` method. The keyboard shortcut to this dialog box is Ctrl+F.

## API Reference

### Methods Overview

- **FindRange**: Searches for a specified string within a specified range with various match options.
- **FindRegex**: Performs regex-based searches with options to include collapsed text.
- **ReplaceText**: Replaces a specific occurrence of a text string with another.
- **FindCurrentText**: Finds the next occurrence of the word currently under the cursor.
- **FindNext**: Finds the next occurrence of the current search text.
- **ReplaceAll**: Replaces all occurrences of a search text with the replacement text.

### Parameters and Usage

#### FindRange Method
- **Parameters**:
  - `searchString`: The string to search for.
  - `startLocation`: The starting location for the search.
  - `endLocation`: The ending location for the search.
  - `matchWholeWord`: Boolean to match whole words only.
  - `searchHiddenText`: Boolean to search through hidden text.
  - `searchUp`: Boolean to search upwards.
  - `useRegex`: Boolean to use regular expressions.

#### FindRegex Method
- **Parameters**:
  - `startLine`: The starting line for the search.
  - `startColumn`: The starting column for the search.
  - `expression`: The regular expression to use.
  - `bSearchInCollapsed`: Boolean to search through collapsed text.
  - `searchUp`: Boolean to search upwards.

### Keyboard Shortcut

The Find dialog box can be invoked using the keyboard shortcut `Ctrl+F`.

<!-- tags: [syncfusion, winforms, editcontrol, find, replace, dialog boxes, search, text, api, methods, version: 11.4.0.26] keywords: [findtext, regex, replace, findnext, findcurrenttext, showfinddialog, keyboard shortcut, search range, replacement, advanced features] -->
``` 
