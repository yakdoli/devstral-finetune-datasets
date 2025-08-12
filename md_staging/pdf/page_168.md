```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: pdf
page_number: 168
page_id: pdf#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:04Z
fidelity: lossless
-->

## Overview

- Action—Demonstrates various file actions and form actions supported by Essential PDF.
- Annotation—Demonstrates various annotation types supported by Essential PDF.
- Attachments—Explains how various file attachments can be carried out by using Essential PDF.
- Portfolio—Demonstrates how to create a PDF Portfolio to add multiple files of different formats, created in different applications.

## Content

### Note: You must add the `Syncfusion.Pdf.Interactive` namespace to work with interactive features.

#### **4.1.3.1 Actions**

Essential PDF supports different actions triggered by different events and user interaction. There are a lot of possible actions such as playing a particular sound or movie, launching an application or URI, and so on.

Essential PDF supports the following types of actions:

- `PdfSoundAction`, which plays the specified music file
- `PdfUriAction` that launches the specified URI
- `PdfGoToAction` that goes to the specified page of the document
- `PdfJavaScriptAction`, which executes specified PDF javascript code
- `PdfLaunchAction` that launches the application or opens the document
- `PdfNamedAction`, which goes to the named destination: next, previous, first, or last page
- `PdfSubmitAction`, which submits the data that is entered into the PDF form
- `PdfResetAction` that resets the fields of the PDF form

### Code Example

```csharp
[C#]
PdfUriAction uriAction = new PdfUriAction("http://www.google.com");

PdfDestination dest = new PdfDestination(page, new Point(0, 100));

PdfGoToAction goToAction = new PdfGoToAction(page);
goToAction.Destination = dest;
uriAction.Next = goToAction;

PdfJavaScriptAction javaAction = new PdfJavaScriptAction("app.alert(\"Hello \\\")");
goToAction.Next = javaAction;

document.Actions.AfterOpen = soundAction;
```

## Page-level Navigation/TOC (if applicable)
<!-- tags: [Essential PDF, actions, annotations, attachments, portfolio, interactive features, Syncfusion Winforms, version 11.4.0.26] keywords: [Syncfusion.Pdf.Interactive, PdfSoundAction, PdfUriAction, PdfGoToAction, PdfJavaScriptAction, PdfLaunchAction, PdfNamedAction, PdfSubmitAction, PdfResetAction, document.Actions.AfterOpen, PdfDestination, navitation] -->
```