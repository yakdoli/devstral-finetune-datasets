```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: pdf
page_number: 053
page_id: pdf#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:57Z
fidelity: lossless
-->

```csharp
get
{
    if (m_pdfDocument != null)
        return m_pdfDocument;
    return null;
}
}
public PdfLoadedDocument pdfLoadedDoc
{
    get
    {
        if (m_pdfLoadedDocument != null)
            return m_pdfLoadedDocument;
        return null;
    }
}
public HttpResponse Response
{
    get
    {
        return m_response;
    }
}
public HttpReadType ReadType
{
    get
    {
        return m_readType;
    }
    set
    {
        m_readType = value;
    }
}
}
public PdfResult(PdfDocument pdfDocument, string filename, HttpResponse response, HttpReadType type)
{
    this.m_pdfDocument = pdfDocument;
    this.m_pdfLoadedDocument = null;
    this.FileName = filename;
    this.m_response = response;
    this.ReadType = type;
}
```

## API Reference (if applicable)

### Constructors

#### `public PdfResult(PdfDocument pdfDocument, string filename, HttpResponse response, HttpReadType type)`
- **Parameters**:
  - `pdfDocument`: The `PdfDocument` object to be manipulated.
  - `filename`: The string representing the name of the file.
  - `response`: The `HttpResponse` object, likely used for handling the HTTP response.
  - `type`: The `HttpReadType` enum indicating the type of read operation.

### Properties

#### `public PdfDocument Document`
- **Getter**: Returns the `PdfDocument` object if it is not null; otherwise, returns `null`.

#### `public PdfLoadedDocument pdfLoadedDoc`
- **Getter**: Returns the `PdfLoadedDocument` object if it is not null; otherwise, returns `null`.

#### `public HttpResponse Response`
- **Getter**: Returns the `HttpResponse` object.

#### `public HttpReadType ReadType`
- **Getter**: Returns the `HttpReadType` enum representing the read type.
- **Setter**: Sets the `HttpReadType` to the provided value.

---

## Code Examples (multi-language supported)

```csharp
// Example usage of PdfResult
PdfDocument pdfDoc = new PdfDocument();
PdfLoadedDocument loadedDoc = new PdfLoadedDocument(pdfDoc);
HttpResponse response = new HttpResponse();
HttpReadType readType = HttpReadType.Display;

PdfResult result = new PdfResult(pdfDoc, "example.pdf", response, readType);
```

---

## Page-level Navigation/TOC (if applicable)

- **Constructors**
  - `PdfResult(PdfDocument pdfDocument, string filename, HttpResponse response, HttpReadType type)`
- **Properties**
  - `Document`
  - `pdfLoadedDoc`
  - `Response`
  - `ReadType`

---

## Cross References

See also:
- `PdfDocument`
- `PdfLoadedDocument`
- `HttpResponse`
- `HttpReadType`

---

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```