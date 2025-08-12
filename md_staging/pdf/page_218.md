```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_218.jpeg
document_name: pdf
page_number: 218
page_id: pdf#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:14Z
fidelity: lossless
-->

# Essential PDF

## Overview
- A .NET library capable of producing Adobe PDF files.
- Supports easy creation of PDF files from any .NET language.
- Features include drawing text, adding images, tables, shapes, and encryption.

## Content

### General Features

The various features of PDF are listed below:

#### Drawing Text Support
- Text Formatting.
- Center, Left, Right, and Justify text alignments.
- Inserting Unicode support.
- MultiColumn text

#### Font Types
- Supports Predefined Fonts
- True type Fonts
- CJK Fonts

### 4.1.7.1.4 Draw Right-To-Left Text

#### Overview
- Essential PDF provides support for drawing RTL languages into the PDF document.

#### Description
Middle eastern languages such as Hebrew and Arabic are written predominantly from right-to-left. Numbers are written with the most significant digit left-most, just as in European or other left-to-right text. Languages written in left-to-right scripts are often mixed; hence the complete document is bidirectional in nature; a mix of both right-to-left (RTL) and left-to-right (LTR) writing. Text written in the Hebrew and Arabic languages are often referred to as bidirectional or "bidi" in short.

#### Code Example
```csharp
// Set the font with unicode option
Font f = new Font("Arial", 14);
```

## API Reference (if applicable)
- Not explicitly detailed in this section, but typically includes namespaces and members related to the PDF SDK.

## Code Examples
- Provided a C# example for setting the font with Unicode support.

## Cross References
- Refer to general PDF features and test case scenarios in the context of RTL text handling.

<!-- tags: [Essential PDF, Syncfusion, Winforms, .NET library, bidirectional text, Arabic, Hebrew, LTR, RTL] keywords: [PDF generation, text alignment, Unicode support, font types, bidirectional, multilingual support] -->
```