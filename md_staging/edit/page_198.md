```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: edit
page_number: 198
page_id: edit#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:13Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Creating, Loading, and Saving a File
- Loading and Saving Contents

## Content

### 4.8.4 File Sharing

By default, Edit Control locks the file currently loaded into it, and does not allow access to the same by any external application. To enable file sharing, set the `SharedFileMode` property of the Edit Control to `True`.

| **Edit Control Property** | **Description**                                                                 |
|---------------------------|--------------------------------------------------------------------------------|
| `SharedFileMode`          | Gets / sets value indicating whether file should be opened in shared mode. |

#### Code Examples

```csharp
// Enable file sharing.
this.editControl1.SharedFileMode = true;
```

```vb.net
' Enable file sharing.
Me.editControl1.SharedFileMode = True
```

### 4.8.5 Lexical Analysis And Semantic Parsing

Text parsing occurs when a new document is loaded or when modifications occur in an already loaded document. In case of modifications, the Edit Control intelligently reparses only what is necessary to ensure that the text model is up to date with the contents of the editor. Ideally, parsing the Edit Control occurs in a two-phase approach:

1. **First Phase:** Lexical analysis
2. **Second Phase:** Semantic parsing

#### Lexical Analysis

Lexical analysis breaks up text into tokens. Semantic parsing goes a step further and assigns extra contextual meaning to the tokens. Semantic relations recognized by the semantic parser are based on how human beings represent knowledge of the world. Semantic parsing allows tokens to be accessed and processed in a more meaningful way than lexical analysis, moving the automation of understanding the tokens to a higher level. A semantic parser consumes the output of the lexical analyzer and operates by analyzing the sequence of tokens returned. The parser matches these sequences to an end state, which may be one of the possible end states. The end states define the goals of the parser. When an end state is reached, the program using the parser implements some action-specific code.

## Page-level Navigation/TOC (if applicable)
- [Getting Started](#)
- [Properties](#)
- [Methods, Events, and Fields](#)

<!-- tags: [Syncfusion Winforms, File Sharing, Lexical Analysis, Semantic Parsing, Edit Control, SharedFileMode] -->
<!-- keywords: [File Sharing, Lexical Analysis, Semantic Parsing, SharedFileMode, editControl, text parsing, document loading, document modifications] -->
```