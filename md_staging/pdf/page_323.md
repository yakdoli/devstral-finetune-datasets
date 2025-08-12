```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_323.jpeg
document_name: pdf
page_number: 323
page_id: pdf#page_323
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:43Z
fidelity: lossless
-->

### 4.4.1.1.1 Use Case Scenario

**Overview:**

- Introduces the architectural changes implemented by Microsoft with Internet Explorer 9 to support HTML5 standards using DirectX (D2D) for hardware acceleration.
- Discusses the implications for HTML to PDF conversion due to IE's reliance on GDI-based rendering after IE9.
- Highlights the need for a Gecko-based rendering engine to generate select-able text PDFs when IE9 or later is installed.

Starting with Internet Explorer 9, Microsoft has made a series of core-architectural changes to Internet Explorer. One of them was to use DirectX (a.k.a. D2D) to render webpage to achieve full-hardware acceleration development to support HTML5 standard features instead of GDI based rendering. As our HTML to PDF conversion depends on IE's GDI based rendering during conversion, our HTML Converter will not be able to generate PDF documents that contain selectable text. Hence, if the machine has IE9 or later installed, then you should consider using our Gecko based rendering. This approach will reliably generate PDF documents that are text selectable and printer friendly.

---

### 4.4.1.1.2 Prerequisites

The following prerequisites are required for executing the HTML to PDF conversion process:

| **Components**                             | **List of Dependencies**                                                                                               |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **DLLs**                                   | - Syncfusion.Core.dll                                                                                                  |
|                                            | - Syncfusion.Compression.Base.dll                                                                                     |
|                                            | - Syncfusion.Pdf.Base.dll                                                                                             |
|                                            | - Syncfusion.HtmlConverter.Base.dll                                                                                   |
|                                            | - Syncfusion.GeckoHtmlRenderer.dll                                                                                    |
|                                            | - Syncfusion.GeckoWrapper.dll                                                                                         |
| **Software Development Kit (SDK)**        | - XulRunner-SDK 2.0                                                                                                   |

---

### 4.4.1.1.3 Installation Steps

#### Overview:
- Focuses on facilitating the conversion process by ensuring the Active-X Wrapper controls are registered correctly.
- Details the manual registration procedure for the `Syncfusion.GeckoWrapper.dll`.

To facilitate conversion, our HTML Converter depends on our Active-X Wrapper control which talks to GECKO APIs during conversion. While installing the Essential Studio, the assembly manager will register the Syncfusion.GeckoWrapper.dll in the machine. To register our Active-X wrapper control manually:

1. Copy the `Syncfusion.GeckoWrapper.dll` to the Bin folder of Gecko SDK (a.k.a. XulRunner-SDK 2.0.) which can download from this **[location]**.
2. Register the `Syncfusion.GeckoWrapper.dll` using the following command in the command prompt:
   ```
   regsvr32 Syncfusion.GeckoWrapper.dll
   ```

---

### 4.4.1.1.4 Conversion of HTML to PDF using Gecko Rendering Engine

#### Overview:
- Explains the process of converting HTML to PDF using the Gecko Rendering Engine.
- Provides code snippets demonstrating the initialization of the Gecko Rendering Engine.

The following code snippets explain the conversion of HTML to PDF using the Gecko Rendering Engine.

- **C# Example**:
```csharp
// Initializing the Gecko Rendering Engine
GeckoHtmlRendererControl renderer = new GeckoHtmlRendererControl();
```

#### Summary:
- The conversion process involves utilizing the Gecko Rendering Engine through the `GeckoHtmlRendererControl` class.
- This approach ensures that the PDF documents generated are text-selectable and printer-friendly.

---

<!-- tags: [syncfusion, winforms, html-to-pdf, gecko-rendering, conversion, api, 11.4.0.26] keywords: [html to pdf, gecko engine, text selectable, internet explorer, active-x, rendering html, pdf generation] -->
```