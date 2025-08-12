```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: pdf
page_number: 169
page_id: pdf#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:22Z
fidelity: lossless
-->

## Overview
- Describes how to define and link different actions such as UriAction, PdfGoToAction, and PdfJavaScriptAction in a PDF document using Syncfusion's PDF library.
- Explains the concept of chaining actions using the `Next` property and demonstrates this with an example in VB.NET.
- Lists various document, annotation, and form field actions available within the Syncfusion PDF library.

## Content

### Code Example: Chaining Actions in a PDF Document

```vb
[VB.NET]

Dim uriAction As Syncfusion.Pdf.Interactive.PdfUriAction = New Syncfusion.Pdf.Interactive.PdfUriAction("http://www.google.com")

Dim dest As Syncfusion.Pdf.Interactive.PdfDestination = New Syncfusion.Pdf.Interactive.PdfDestination(page, New Point(0, 100))

Dim goToAction As Syncfusion.Pdf.Interactive.PdfGoToAction = New Syncfusion.Pdf.Interactive.PdfGoToAction(page)
goToAction.Destination = dest
uriAction.Next = goToAction

Dim javaAction As Syncfusion.Pdf.Interactive.PdfJavaScriptAction = New Syncfusion.Pdf.Interactive.PdfJavaScriptAction("app.alert(""Hello "")")
goToAction.Next = javaAction

document.Actions.AfterOpen = soundAction
```

**Note:** The `Next` property of an action is used to specify the queue of actions as illustrated in the preceding example.

### Document Object Actions

1. **Following are the actions for Document Object:**
   - **AfterOpen** action to be performed after the document is opened
   - **AfterPrint** action to be performed after the document is printed
   - **AfterSave** action to be performed after the document is saved
   - **BeforeClose** action to be performed before the document is closed
   - **BeforePrint** action to be performed before the document is printed
   - **BeforeSave** action to be performed before the document is saved

### Annotation Object Actions

2. **Following are the actions for Annotation Object:**
   - **GotFocus** action to be performed when the annotation gets focus
   - **LostFocus** action to be performed when the annotation loses focus
   - **MouseEnter** action to be performed when the cursor enters the active area of the annotation
   - **MouseLeave** action to be performed when the cursor leaves the active area of the annotation
   - **MouseDown** action to be performed when the mouse button is pressed inside the active area of the annotation
   - **MouseUp** action to be performed when the mouse button is released inside the active area of the annotation

### Form Field Object Actions

3. **Following are the actions for Form Field Object:**

## API Reference (if applicable)
- **Namespace:**
  - `Syncfusion.Pdf.Interactive`
- **Class Members:**
  - `PdfUriAction`
  - `PdfDestination`
  - `PdfGoToAction`
  - `PdfJavaScriptAction`
  - `PdfAction`

## Code Examples
- The provided VB.NET code snippet demonstrates how to create and link different types of actions in a PDF document.

### WinForms-specific conventions
- Utilizes VB.NET syntax and integrates with Syncfusion's .NET PDF library for document manipulation.

## Cross References
- Refer to Syncfusion's official documentation for additional details on PDF actions and scripting.

<!-- tags: [PDF, actions, VB.NET, Syncfusion Winforms, document actions, annotation actions, form field actions] keywords: [PdfUriAction, PdfDestination, PdfGoToAction, PdfJavaScriptAction, AfterOpen, AfterPrint, BeforeClose, MouseEnter, MouseLeave, MouseDown, MouseUp] -->
```