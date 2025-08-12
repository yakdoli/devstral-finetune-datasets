```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: pdf
page_number: 061
page_id: pdf#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:27:32Z
fidelity: lossless
-->

# 4 Concepts and Features

The concepts and features of Essential PDF are grouped under the following sections.

**Note:** The concepts, features, and APIs are common to Windows, Web, and WPF except for the way the documents are streamed to the browser.

## 4.1 PDF Generator

PDF Generator is an easy-to-use and affordable solution to create a PDF file. This section demonstrates all basic elements used to create a PDF document from scratch.

### 4.1.1 Introduction

This section explains all the basic concepts of Essential PDF that helps to **create a simple PDF document**. It includes the following sub-sections.

- **Document Object Model** - Provides an overview of the Essential PDF object model, enabling you to work with PDF in a quick glance
- **Pen and Brush** - Describes the basic element used to draw graphic elements such as text and shapes
- **Fonts** - Demonstrates various fonts supported by Essential PDF, which can be used to write multilingual text

#### 4.1.1.1 Document Object Model

PdfDocument is a top-level object in Essential PDF, which is a representation of a PDF document. The document contains a collection of sections that are represented by the **PdfSection** class, which is a logical entity containing a collection of pages and their settings. Pages (which are represented by **PdfPage class**) are the main destinations of the graphics output.

**Note:** A document should contain at least one section with one page.
```