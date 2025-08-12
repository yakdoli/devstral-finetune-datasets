<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_066.jpeg
document_name: pdf
page_number: 066
page_id: pdf#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:27:51Z
fidelity: lossless
-->

## Overview

- Overview of the `DocumentSaved` and `SaveProgress` events.
- Description of the `PdfSection` class and its methods and properties.

## Content

### Sections

A section in a PDF document contains pages with the same parameters. Here are the details:

- Contains pages with the same parameters.
- When new pages are added to the section, it obtains parameters from the section even if it was imported from another section or document.
- When a high-level graphic object needs to be drawn on more than one page, it adds a new page to the section of the start page from which the object starts, if required.

### PdfSection Class

The `PdfSection` class allows creating and managing sections. Below are the members exposed by the `PdfSection` class.

#### Events

| Name            | Description                                             |
|-----------------|---------------------------------------------------------|
| `DocumentSaved` | This event is raised when the document is saved.       |
| `SaveProgress`  | This event exposes the progression of the save state of the document. |

#### Methods

| Name            | Description                                              |
|-----------------|----------------------------------------------------------|
| `Add`           | Overloaded.                                              |
| `Clear`         | Removes all the pages from the section.                 |
| `Contains`      | Determines whether the page is within the section.      |
| `DrawTemplates` | Draws page templates on the page.                       |
| `IndexOf`       | Gets the index of the page.                             |
| `Insert`        | Inserts a page at the specified index.                  |
| `OnPageAdded`   | Called when the page is added.                          |
| `OnPageSaving`  | Called when a page is being saved.                     |
| `Remove`        | Removes the page from the section.                      |
| `RemoveAt`      | Removes the page by its index in the section.           |

#### Properties

| Name   | Description                     |
|--------|-----------------------------------|
| `Count`| Gets the count of the pages in the section. |

## API Reference

### Namespace: Syncfusion.Pdf

#### Class: PdfSection

##### Methods

| Name            | Description                                              |
|-----------------|----------------------------------------------------------|
| `Add`           | Overloaded.                                              |
| `Clear`         | Removes all the pages from the section.                 |
| `Contains`      | Determines whether the page is within the section.      |
| `DrawTemplates` | Draws page templates on the page.                       |
| `IndexOf`       | Gets the index of the page.                             |
| `Insert`        | Inserts a page at the specified index.                  |
| `OnPageAdded`   | Called when the page is added.                          |
| `OnPageSaving`  | Called when a page is being saved.                     |
| `Remove`        | Removes the page from the section.                      |
| `RemoveAt`      | Removes the page by its index in the section.           |

##### Properties

| Name   | Description                     |
|--------|-----------------------------------|
| `Count`| Gets the count of the pages in the section. |

## Code Examples

### Example: Using PdfSection

```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;

// Create a new PDF document
PdfDocument document = new PdfDocument();

// Create a section
PdfSection section = new PdfSection();

// Add pages to the section
section.Pages.Add(new PdfPage());

// Draw on the page
PdfGraphics graphics = section.Pages[0].Graphics;
graphics.DrawString("Hello, World!", new PdfStandardFont(PdfFontFamily.Helvetica, 12), PdfBrushes.Black, new PointF(10, 10));

// Save the document
document.Save("Output.pdf");
```

## Page-level Navigation/TOC

- Sections
  - Overview of sections
- PdfSection Class
  - Methods
  - Properties

## Cross References

- See also:
  - [Syncfusion PDF API Documentation](#)
  - [PdfDocument Class](#)
  - [PdfPage Class](#)

<!-- tags: [Syncfusion, WinForms, PDF, PdfSection, DocumentSaved, SaveProgress] keywords: [PdfSection, methods, properties, sections, document, page, save, progress] -->