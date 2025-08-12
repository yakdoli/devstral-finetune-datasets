```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: XlsIO
page_number: 047
page_id: XlsIO#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:06Z
fidelity: lossless
-->

# Essential XlsIO

Now, you have created a Silverlight application (refer [Creating a Platform Application](#)). This section covers the following:

- Deploying Essential XlsIO in a Silverlight Application
- Creating and adding an Excel document (with worksheets) to the application

## Deploying Essential XlsIO in a Silverlight Application

The following steps will guide you to deploy Essential XlsIO:

1. Open the `MainPage.xaml` of the application in the designer.
2. Add the `Syncfusion.Compression.Silverlight.dll` and `Syncfusion.XlsIO.Silverlight.dll` assemblies as references to the application.

Essential XlsIO is now deployed in your Silverlight application.

## Creating and Adding an Excel Document (With Worksheets) to the Application

Essential XlsIO for Silverlight has support for creation and manipulation of richly formatted Excel [97-2003] format spreadsheets from scratch on the client side. Advanced features like Data Validation, Conditional Formatting and Charts can also be used in this approach.

Following steps will guide you to create a simple spreadsheet:

1. Add references to the following assemblies.
   - `Syncfusion.Compression.Silverlight.dll`
   - `Syncfusion.XlsIO.Silverlight.dll`
2. The next step is to add reference to the following namespace.
   - `Syncfusion.XlsIO` (using Syncfusion.XlsIO)

```csharp
using Syncfusion.XlsIO;
```

3. Instantiate the Excel Engine.

```csharp
```

## API Reference

### Creating and Manipulating Excel Documents

```csharp
```

## Code Examples

### Instantiating the Excel Engine
```csharp
using Syncfusion.XlsIO;
```

### Creating and Saving an Excel Document

```csharp
```

<!-- tags: [essentialxlsio, silverlight, platformapplication, creatingexcel, datavalidation, conditionalformatting, charts] keywords: [xlsio, silverlight application, excel document, worksheets, data validation, conditional formatting, charts] -->
```