```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: DocIo
page_number: 222
page_id: DocIo#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:07Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Learn to use tab stops, tab leaders, and document formatting in a Word document.
- Understand adding, removing, and modifying tab stops in a paragraph.
- Explore creating custom list styles in MS Word using DocIO.

## Content

### Handling Tab Stops and Tab Leaders

Here are examples of managing tab stops in a Word document:

```csharp
// Add tab stop at position 36 with left justification and dotted tab leader
paragraph.ParagraphFormat.Tabs.AddTab(36, TabJustification.Left, Syncfusion.DocIO.DLS.TabLeader.Dotted)

// Add tab stop at position 80 with right justification and hyphenated tab leader
paragraph.ParagraphFormat.Tabs.AddTab(80, TabJustification.Right, Syncfusion.DocIO.DLS.TabLeader.Hyphenated)

// Add tab stop at position 144 with centered justification and no tab leader
paragraph.ParagraphFormat.Tabs.AddTab(144, TabJustification.Centered, Syncfusion.DocIO.DLS.TabLeader.NoLeader)

// Remove tab at index 1 from the tab collection
paragraph.ParagraphFormat.Tabs.RemoveAt(1)

// Remove tab at position 144
paragraph.ParagraphFormat.Tabs.RemoveByTabPosition(144)

// Append a tab character to the paragraph
paragraph.AppendText("\t")

// Append text to the paragraph
paragraph.AppendText("Tabs are added and removed")

// Save the Word document
document.Save("Sample.doc", FormatType.Doc)
```

### 4.4.2.5 Lists

#### ListStyle Class

The `ListStyle` class represents list properties in the Word paragraph style. A collection of list styles is accessible through the `WordDocument.ListStyles` property.

##### Creating Custom List Styles

You can create your own list style. To add a list style using DocIO, use the `WordDocument.AddListStyle` method. Every list style has its own name, accessible via the `Name` property. There are two types of list styles:

- **Numbered**
- **Bulleted**

You can specify the type of the list style by using the `ListType` property. Each `ListStyle` object contains a collection of list levels. This collection can consist of up to nine levels (maximum number of list levels). The collection of list levels is accessible through the `Levels` property. This property returns the `ListLevelCollection` object, which contains objects of the `WListLevel` class.

#### List Styles in MS Word

This section deals with list styles specific to Microsoft Word.

## API Reference

### ListStyle Methods
- **AddTab(int position, TabJustification justification, TabLeader leader)**
  - Adds a tab stop to the paragraph with specified position, justification, and leader.

- **RemoveAt(int index)**
  - Removes the tab stop at the specified index.

- **RemoveByTabPosition(int position)**
  - Removes the tab stop at the specified position.

- **AddListStyle(string name, ListType type)**
  - Adds a new list style to the document with the specified name and type.

### Properties
- **Name**: Gets or sets the name of the list style.
- **ListType**: Specifies the type of the list style.
- **Levels**: Gets the collection of list levels associated with the style.

### ListLevel Methods
- **ListLevelCollection Class**: Represents a collection of list levels within a `ListStyle`.

## Code Examples

### Example: Creating a Custom List Style

```csharp
// Create a new Word document
WordDocument document = new WordDocument();

// Add a new list style
ListStyle listStyle = document.ListStyles.AddListStyle("CustomNumberedList", ListType.Number);

// Set properties for the list style
listStyle.NumberFormat = "%1.";

// Add the list style to the document
document.ListStyles.AddListStyle(listStyle);

// Save the document
document.Save("CustomListStyle.doc", FormatType.Doc);
```

<!-- tags: [docio, syncfusion, msword, liststyles, tabstops, formatting, numbering, bulleted] -->
```