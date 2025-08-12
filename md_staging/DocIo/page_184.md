```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_184.jpeg
document_name: DocIo
page_number: 184
page_id: DocIo#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:45Z
fidelity: lossless
-->

# Essential DocIO

DocIO has the ability to preserve Word comments, but the creation of comments from APIs or its modification is limited.

## Overview
- Word comments are subdocuments represented by a special marker that defines the comment's location and special data that defines the comment text and formatting.
- The WComment class models the structure and properties of comments, providing a way to access and manipulate comment attributes.
- WCommentFormat and WCommentBody types offer detailed control over the formatting and text content of comments.

## Content

### Comments in Word Documents
Comment is one of the subdocuments of Word. Presentation of this subdocument in the Word document consists of two parts:
- **Special marker**: Defines the comment location in the document.
- **Special data**: Defines the text and formatting of the comment.

### WComment Class Properties
The WComment class models the structure and properties of the comments. The main properties of the WComment class are:

- **TextBody**: Contains the text of the comment.
- **Format**: Specifies the format for the comment.

The `TextBody` property returns the object of the `WTextBody` type. The `Format` property returns the object of the `WCommentFormat` type.

### Class Hierarchy
The class hierarchy for WComment is:
```
ParagraphItem
  |
  WComment
```

### Public Constructor
The public constructor for the WComment class is:

| Name      | Description                                    |
|-----------|------------------------------------------------|
| WComment  | Initializes a new instance of the WComment class. |

### Public Properties
The public properties of the WComment class are as follows:

| Name       | Description                      |
|------------|----------------------------------|
| EntityType | Gets the type of the entity.     |
| Format     | Gets the format.                |
| TextBody   | Gets the comment body.          |

### WCommentFormat Properties and Methods
WCommentFormat has the following public properties and methods:
- (Not explicitly detailed in the image, but mentioned as having its own set of properties and methods.)

## API Reference

### WComment Class
- **Namespace**: Specifies the namespace under which the WComment class is defined.
- **Properties**:
  - **EntityType**: Returns the type of the entity.
  - **Format**: Returns the format of the comment.
  - **TextBody**: Returns the body of the comment.

### WCommentFormat Class
- **Properties**:
  - (Not detailed in the image but implied to have public properties and methods as mentioned.)

:::note
WComment and related classes provide detailed interfaces for manipulating comments within Word documents, enabling developers to create, modify, and format comments programmatically.
:::

## Code Examples

### Example: Creating a New Comment
```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.DLS;

// Create a new Word document.
WordDocument document = new WordDocument();
IW_comment comment = new W_comment();

// Set the comment body.
comment.TextBody.Text = "This is a sample comment.";

// Add the comment to the document.
document.LastParagraph.Append(comment);
```

## RAG Annotations

<!-- tags: DocIO, WComment, WCommentFormat, WTextBody, Word comments, Document Manipulation, Syncfusion Winforms keywords: DocIO, comments, WComment, WCommentFormat, WTextBody, Word document, comment body, format, class hierarchy, API reference -->
```