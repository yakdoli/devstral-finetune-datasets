```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: edit
page_number: 090
page_id: edit#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:44Z
fidelity: lossless
-->

# Editing Comments

### Adding Comments

**C#**
```csharp
this.editControl1.CommentLine(1);
this.editControl1.CommentSelection();
this.editControl1.CommentText(new Point(1, 1), new Point(7, 7));
```

**VB.NET**
```vbnet
Me.editControl1.CommentLine(1)
Me.editControl1.CommentSelection()
Me.editControl1.CommentText(New Point(1, 1), New Point(7, 7))
```

### Removing Comments

Comments can be removed by using the below given methods.

| Edit Control Method        | Description                          |
|----------------------------|--------------------------------------|
| UnCommentLine              | UnComments single line.             |
| UnCommentSelection         | UnComments selected text.           |
| UnCommentText              | UnComments text in the specified range. |

**C#**
```csharp
this.editControl1.UnCommentLine();
this.editControl1.UncommentSelection();
this.editControl1.UncommentText(new Point(1, 1), new Point(7, 7));
```

**VB.NET**
```vbnet
Me.editControl1.UnCommentLine()
Me.editControl1.UncommentSelection()
Me.editControl1.UncommentText(New Point(1, 1), New Point(7, 7))
```

### 4.4.10 Break Points

## API Reference

### Methods

- **CommentLine**  
  Marks a single line as a comment.

- **CommentSelection**  
  Marks the selected text as a comment.

- **CommentText**  
  Marks text in the specified range as a comment.

- **UnCommentLine**  
  Removes comments from a single line.

- **UnCommentSelection**  
  Removes comments from the selected text.

- **UnCommentText**  
  Removes comments from text in the specified range.

## Code Examples

Example 1: Adding Comments
```csharp
this.editControl1.CommentLine(1);
this.editControl1.CommentSelection();
this.editControl1.CommentText(new Point(1, 1), new Point(7, 7));
```

Example 2: Removing Comments
```csharp
this.editControl1.UnCommentLine();
this.editControl1.UncommentSelection();
this.editControl1.UncommentText(new Point(1, 1), new Point(7, 7));
```

## Cross References

See also:
- 4.4.9 Adding and Removing Comments
- 4.4.11 Break Point Range Operations

<!-- tags: [syncfusion, winforms, edit control, commenting, breakpoints, version 11.4.0.26] keywords: [comments, selection, text, uncomments, range, break points] -->
```