```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: edit
page_number: 057
page_id: edit#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:29Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

### Word Level Navigation

#### C#

```csharp
this.editControl1.MoveLeftWord();
this.editControl1.MoveRightWord();
```

#### VB.NET

```vb
Me.editControl1.MoveLeftWord();
Me.editControl1.MoveRightWord();
```

### Line Level Navigation

The following APIs enable text navigation in the Edit Control, in terms of lines.

| Edit Control Method | Description                                      |
|---------------------|--------------------------------------------------|
| MoveToLineStart    | Moves caret to the beginning of the line. First whitespaces will be skipped. |
| MoveToLineEnd      | Moves caret to the end of the line.               |

#### C#

```csharp
this.editControl1.MoveToLineStart();
this.editControl1.MoveToLineEnd();
```

#### VB.NET

```vb
Me.editControl1.MoveToLineStart();
Me.editControl1.MoveToLineEnd();
```

### Page Level Navigation

The following APIs enable text navigation in the Edit Control, in terms of pages.

| Edit Control Method | Description              |
|---------------------|---------------------------|
| MovePageUp         | Moves caret one page up. |
| MovePageDown       | Moves caret one page down. |
```


<!-- tags: [syncfusion, winforms, edit, navigation, api] keywords: [moveleftword, moverightword, movetolinestart, movetolineend, movepageup, movepagedown, essential edit for windows forms, page level navigation, line level navigation, word level navigation, edit control, caret movement, text navigation] -->
```