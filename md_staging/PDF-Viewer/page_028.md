```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_028.jpeg
document_name: PDF Viewer
page_number: 028
page_id: PDF Viewer#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:51:24Z
fidelity: lossless
-->

# Northwind Customers

## Overview
- The page displays a PDF document showcasing a customer database for the fictional company **Northwind Traders**.
- The PDF contains a table listing customer information, including IDs, company names, contact details, and addresses.
- The table is presented in a scrollable view, indicating the use of a document viewer control.

## Content

### Customer Table

| CustomerID | CompanyName           | ContactName          | Address                         | City             | PostalCode | Country   | Phone              | Fax               |
|------------|------------------------|----------------------|---------------------------------|------------------|------------|-----------|--------------------|-------------------|
| ALFKI      | Alfons Futterkiste    | Maria Anders         | Obere Str. 57                 | Berlin          | 12209      | Germany   | 030-0074321        | 030-0076545       |
| ANATR      | Ana Trujillo Emparedados y Helados | Ana Trujillo | Avda. de la Construcción 2222 | México D.F.     | 05021      | Mexico    | (5) 55-4729       | (5) 55-3745       |
| ANTON      | Antonio Moreno Taquería | Antonio Moreno      | Mataderos 2312               | México D.F.     | 05023      | Mexico    | (5) 55-3932       |                   |
| AROUT      | Around the Horn        | Thomas Hardy         | 120 Hanover Sq.               | London          | WA1 1DP    | UK        | (171) 555-7788    | (171) 555-6750    |
| BERGS      | Berglunds snacks/döner | Christina Berglund  | Berguvsvägen 8               | Luleå          | S-95822    | Sweden    | 0921-123465        | 0921-123467       |
| BLAUS      | Blauer See Delikatessen | Hanna Moos          | Forsterstr. 57               | Mannheim        | 68306      | Germany   | 0621-08460         | 0621-08924        |
| BLONP      | Blondel père et fils   | Frédéric Citeaux    | 24, place Kleber              | Strasbourg      | 67000      | France    | 88.60.15.31       | 88.60.15.32       |
| BOLID      | Bólido Comidas preparadas | Martin Sommer     | C/ Araquil, 67               | Madrid          | 28023      | Spain     | (91)25522         | (91)25591        |
| BONAP      | Bon appétit            | Laurence Lebihan    | 12, rue des Bouchers           | Marseille       | 13008      | France    | 91.24.45.40       | 91.24.45.41       |
| BOTTM      | Bottom-Dollar Markets  | Elizabeth Lincoln    | 23 Tsawassen Blvd.           | Tsawassen       | T2F 8M4    | Canada    | (604) 555-4729    | (604) 555-3745    |
| BSBEV      | B's Beverages          | Victoria Ashworth    | Fauntleercy Circus             | London          | EC2 5NT    | UK        | (171) 555-1212    |                   |
| CACTU      | Cactus Comidas para llevar | Patricio Simpson | Carrito 333                   | Buenos Aires    | 1010       | Argentina | (1)35-5555        | (1)35-4892        |
| CENTC      | Centro comercial Moctezuma | Francisco Chang | Sierras de Granada 9993      | México D.F.     | 05022      | Mexico    | (5) 55-3392       | (5) 55-7293       |
| CHOPS      | Chop-suey Chinese      | Yang Wang           | Hauptstr. 29                  | Bern            | 3012       | Switzerland| 0452-076545       |                   |
| COMMI      | Comércio Mineiro       | Pedro Afonso        | Av. dos Lusiadas, 23          | São Paulo       | 05432-043  | Brazil    | (11) 55-7647      |                   |
| CONSH      | Consolidated           | Elizabeth Berkeley   | Berkeley                       | London          | WX1 6LT    | UK        | (171)             |                   |

### Document Viewer Demonstration
- The PDF is displayed within a `PdfDocumentView` control, as indicated by the window title and interface elements.
- The document viewer allows for interactive scrolling, as evidenced by the visible scroll bar.
- The content is clearly formatted and structured for easy readability.

## API Reference
- This section contains information specific to the Syncfusion Winforms PDF viewer control. It may include API calls for displaying and interacting with PDF documents.
- Example methods could include creating a new `PdfDocumentView` instance, loading PDF files, and handling user interactions such as scrolling and zooming.

### Example Code
```csharp
// Sample C# code for loading and displaying a PDF document
using Syncfusion.Pdf;
using Syncfusion.PdfViewer.WindowsForms;

PdfDocument document = new PdfDocument(@"path_to_pdf_file.pdf");
PdfViewer viewer = new PdfViewer();
viewer.Load(document);

// Attach the viewer to the form or container
this.Controls.Add(viewer);
```

## Figures
- **Figure 11: PDF displayed in PdfDocumentView**
  - This figure showcases the PDF document as rendered in the document viewer, highlighting how the viewer control presents and navigates the document.

## Cross References
- See also:
  - [Syncfusion PDF Viewer Documentation](#)
  - [WinForms Controls Overview](#)

<!-- tags: [syncfusion, winforms, pdf viewer, northwind traders, document control, pdf-ocr-to-markdown] keywords: [pdf viewer, northwind customers, document viewer, syncfusion winforms, api reference] -->
```