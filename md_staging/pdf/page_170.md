```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_170.jpeg
document_name: pdf
page_number: 170
page_id: pdf#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:10Z
fidelity: lossless
-->

## Essential PDF

### Overview
- **Calculate** javascript action to be performed to recalculate the value of the field
- **Format** javascript action to be performed before the field is formatted to display the value
- **Validate** javascript action to be performed when the value of the field is changed
- **KeyPressed** javascript action to be performed when the user types, key-stroke into a text field or combo box, or modifies the selection in a scrollable list box

**Summary:** JavaScript actions are used to handle dynamic behavior in fields, including calculations, formatting, validation, and user interactions, while annotations provide interactive elements like sounds, files, and links.

### Fields
Additionally, the fields support all the actions that are supported by annotations.

### 4.1.3.2 Annotation

An annotation associates an object such as a note, sound, or movie with a location on the page of a PDF document, or provides a way to interact with the user, by means of the mouse and keyboard.

An annotation is activated when you click the left mouse button.

#### Types of Annotations
- **PdfSoundAnnotation** plays sound file
- **PdfAttachmentAnnotation** opens attached file
- **PdfUriAnnotation** navigates to specified URI
- **PdfActionAnnotation** performs specified action
- **PdfFileLinkAnnotation** opens file with the specified path
- **PdfDocumentLinkAnnotation** navigates to specified destination within the document
- **PdfPopupAnnotation** displays the text in a pop-up window for entry and editing
- **PdfLineAnnotation** displays a single straight line on the page

#### Code Examples

```csharp
// Creating a Pop-up Annotation
RectangleF popupAnnotationRectangle = new RectangleF(0, 50, 50, 50);
PdfPopupAnnotation popupAnnotation = new PdfPopupAnnotation(popupAnnotationRectangle, "Test popup annotation");
popupAnnotation.Border.Width = 4;
popupAnnotation.Icon = PopupIcon.NewParagraph;
page.Annotations.Add(popupAnnotation);

// Creating a URI Annotation
RectangleF uriAnnotationRectangle = new RectangleF(0, 100, 80, 20);
PdfUriAnnotation uriAnnotation = new PdfUriAnnotation(uriAnnotationRectangle, "http://www.google.com");
page.Annotations.Add(uriAnnotation);

// Creating a Document Link Annotation
RectangleF docLinkAnnotationRectangle = new RectangleF(0, 200, 80, 20);
PdfDocumentLinkAnnotation documentAnnotation = new PdfDocumentLinkAnnotation(docLinkAnnotationRectangle);
documentAnnotation.Text = "Document link annotation";
```

### Related Information
Annotations are interactive elements in a PDF document that enhance user interaction and provide additional information or functionality upon user engagement.

<!-- tags: [product, module, control, api, version?] keywords: [JavaScript actions, fields, annotations, PdfSoundAnnotation, PdfAttachmentAnnotation, PdfUriAnnotation, PdfActionAnnotation, PdfFileLinkAnnotation, PdfDocumentLinkAnnotation, PdfPopupAnnotation, PdfLineAnnotation, Pdf] -->
```