```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: DocIo
page_number: 126
page_id: DocIo#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:35Z
fidelity: lossless
-->

## Essential DocIO

### Note: Essential DocIO currently provides support for built-in table styles in Word2007, Word2010, and Word2013 formats.

### 4.3.4 Content Control

The Content control helps you to design Word documents (.docx) and templates (.dotx) to have the following features:

- **User Interface**—Allows end users to enter data only in a controlled section of the Word document.
- **Data Protection**—Restricts users from editing the protected sections of a Word document or template.
- **Data Binding**—Binds the Content control to a data source.

Limited support has been added to the Essential DocIO to preserve the Content control with custom XML mapping (data binding).

The following are the list of Content controls for which the preservation support is added:

- Rich Text Content control
- Plain Text Content control
- Picture Content control
- Combo Box Content control
- Drop-down List Content control
- Date Picker Content control
- Check Box Content control (Word 2010 only)

### Note: Currently Essential DocIO does not provide support to edit/modify the Content controls. Track changes information will not be preserved using DocIO.

---

### 4.4 Paragraph

The `WParagraph` class represents a single paragraph in a document. A DocIO paragraph contains paragraph items inside. You can add paragraph items by using the `Items` property. This property returns the collection of paragraph items (object of `ParagraphItemCollection` type).

Each paragraph has a paragraph format. The format of the paragraph is set by using the `ParagraphFormat` property. This property is used to define the paragraph border, style of texture, foreground and background color, paragraph spacing, and so on. For more details on Paragraph Formatting, see `WParagraphFormat`.

#### Property:
- **IsInCell**: defines whether the current paragraph belongs to the table cell (is in the table cell)

```
## API Reference

#### Properties:
- **IsInCell**: indicates if the current paragraph is inside a table cell.

#### Methods:
- **Add**: Adds paragraph items to the `Items` property.
- **SetFormat**: Configures the paragraph format using the `ParagraphFormat` property.

#### Example:
```csharp
// Creating a Paragraph
var doc = new WordDocument();
var section = doc.AddSection();
var paragraph = section.AddParagraph("Hello, World!");

// Setting Paragraph Format
paragraph.ParagraphFormat.FontName = "Arial";
paragraph.ParagraphFormat.FontSize = 12;
paragraph.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Left;

// Checking if the paragraph is in a table cell
bool isInCell = paragraph.IsInCell;
Console.WriteLine($"Is inside a table cell: {isInCell}");
```
```

---

### RAG Annotations
<!-- tags: [DocIO, ContentControl, Paragraph, ParagraphFormatting, isインターフェース, データ保障, データバインド, WordTemplates] keywords: [Essential DocIO, Word documents, Content Control, WParagraph, ParagraphFormat, IsInCell, Plain Text Content control, Combo Box Content control, Drop-down List Content control, Date Picker Content control, Check Box Content control] -->
```