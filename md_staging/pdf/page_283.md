```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_283.jpeg
document_name: pdf
page_number: 283
page_id: pdf#page_283
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:03Z
fidelity: lossless
-->

## WhiteList

- **Purpose**: Gets or sets the white-list values.

---

### Methods

#### Table 6: Method Table

| Method          | Description                                                    |
|-----------------|----------------------------------------------------------------|
| PerformOCR      | Performs OCR on images in the loaded PDF document.          |

---

### 4.2.9.2 Prerequisites

This section covers the mandatory requirements for using OCR support.

#### 4.2.9.2.1 DLLs

The following assemblies need to be referenced in your application to use the Tesseract OCR engine.

**Syncfusion DLLs:**

- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.Pdf.Base.dll
- Syncfusion.OcrProcessor.dll

**Tesseract DLLs:**

- SyncfusionTesseract.dll (Tesseract version 3.0)
- liblpept168.dll (Leptonica image processing library used by the Tesseract OCR engine since version 3)

---

#### 4.2.9.2.2 Windows Deployment

Use the following steps to organize Windows deployment:

1. Place the SyncfusionTesseract.dll and liblpept168.dll assemblies in the Bin folder.
2. Refer to the following assemblies to your project:
   - Syncfusion.Core.dll
   - Syncfusion.Compression.Base.dll
   - Syncfusion.Pdf.Base.dll
   - Syncfusion.OCRProcessor.Base.dll

---

## API Reference (if applicable)

### 4.2.9.2 Prerequisites

#### Syncfusion DLLs

- **Syncfusion.Core.dll**
- **Syncfusion.Compression.Base.dll**
- **Syncfusion.Pdf.Base.dll**
- **Syncfusion.OcrProcessor.dll**

#### Tesseract DLLs

- **SyncfusionTesseract.dll** (Tesseract version 3.0)
- **liblpept168.dll** (Leptonica image processing library used by the Tesseract OCR engine since version 3)

---

### Code Examples (multi-language supported)

#### Required Reference Code Example

```csharp
using Syncfusion.Core;
using Syncfusion.Compression.Base;
using Syncfusion.Pdf.Base;
using Syncfusion.OcrProcessor.Base;
```

---

### Cross References

See also:

- \[Cross-reference links or text, if present on the page.]

---

<!-- tags: [product, module, control, api, version] keywords: [OCR, Tesseract, DLLs, Windows Deployment, Syncfusion.Core.dll, Syncfusion.Compression.Base.dll] -->
```