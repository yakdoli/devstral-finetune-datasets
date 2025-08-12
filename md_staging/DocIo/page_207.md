```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en (keep original; do not translate)  
source_filename: page_207.jpeg  
document_name: DocIo  
page_number: 207  
page_id: DocIo#page_207  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T04:40:46Z  
fidelity: lossless  
-->

## Overview  
- Public properties and methods related to styling in the document.  
- Overview of character formatting through the WCharacterFormat class.  
- Hierarchy of formatting classes.

## Content  

### Public Properties  

| Name                      | Description                                                                                                                                                                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BaseStyle                 | Gets the base style.                                                                                                                                                                                                                          |
| StyleType                 | Gets the type of the style.                                                                                                                                                                                                                   |
| UseContextualAlternates    | Gets or sets a value indicating whether to use contextual alternates (Microsoft Word 2010 specific property).                                                                     |
| Ligatures                 | Gets or sets the ligatures type (Microsoft Word 2010 specific property).                                                                                                          |
| NumberForm                | Gets or sets the number form type (Microsoft Word 2010 specific property).                                                                                                       |
| NumberSpacing             | Gets or sets the number spacing type (Microsoft Word 2010 specific property).                                                                                                    |
| StylisticSet              | Gets or sets the stylistic set type (Microsoft Word 2010 specific property).                                                                                                      |

### Public Methods  

| Name             | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| Clone            | Clones itself.                                                                               |
| NameToBuiltIn    | Converts string style names to BuiltinStyle.                                                  |

### Character Formats  
- **WCharacterFormat** class represents character formatting in the Word document.  
- WCharacterFormat class is used to get or set the formatting for text chunks, special symbol or marker (for example marker of picture, text box, footnote, etc.). WCharacterFormat customizes the appearance of the element (for example text chunk or symbol) in the document, starting with font name to the style of texture and spacing between characters.

### Class Hierarchy  
- **FormatBase**

## API Reference  
- **Namespace**:  
  - WCharacterFormat class.

## Code Examples  
- No specific code examples are provided in this document section.

## Cross References  
- See also:  
  - WCharacterFormat, FormatBase.

<!-- tags: [syncfusion-sdk, winforms, wcharacterformat, formatting, style, microsoft word, class hierarchy] keywords: [styletype, ligatures, numberform, numberspacing, contextualelement, microsoft word 2010, public properties, public methods, character formatting, texchunk, marker] -->
```