```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: DocIo
page_number: 042
page_id: DocIo#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:23Z
fidelity: lossless
-->

# Essential DocIO

Now, you have created a Silverlight application (refer to [Creating Platform Application]). This section covers the following:

- Deploying Essential DocIO in a Silverlight Application
- Creating a Word Document

### Overview

- Essential DocIO has native support for creating and manipulating Word documents in a Silverlight application.
- Note: DocIO provides support to create documents only in the `.doc` and `.dot` formats. It does not support the Word 2007 format.

## Deploying Essential DocIO in a Silverlight Application

The following steps will guide you to deploy Essential DocIO:

1. Open the `MainPage.xaml` of the application in the designer.
2. Add the `Syncfusion.DocIO.Silverlight.dll` assembly as a reference to the application.

Essential DocIO is now deployed in your Silverlight application.

## Creating a Word Document

### Overview

- Essential DocIO for Silverlight has support for creation and manipulation of richly formatted Word [97-2003] format documents. Advanced features like Mail merge, Search, and replace can also be used in this approach.

Following steps will guide you to create a simple Word document with "Hello World" written on the first paragraph of the first section.

### Steps to Create a Word Document

1. Add reference to the following assemblies in your Silverlight application:
   - `Syncfusion.Compression.Silverlight.dll`
   - `Syncfusion.DocIO.Silverlight.dll`
2. The next step is to add references to the following namespaces:
   - `Syncfusion.DocIO.DLS` (using `Syncfusion.DocIO.DLS`)
   - `Syncfusion.DocIO` (using `Syncfusion.DocIO`)

<!-- tags: [Essential DocIO, Silverlight, Word document, deployment, creation] keywords: [DocIO, Silverlight, Word, document creation, deployment] -->
```