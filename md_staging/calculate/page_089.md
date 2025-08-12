```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: calculate
page_number: 089
page_id: calculate#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:11Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Configures web control performance using attributes in the project's `web.config` file.
- Demonstrates handling Excel spreadsheets using Essential XlsIO and Essential Calculate.

## Content

### Web Control Performance

#### Figure 36: Web Control Performance

The image shows a detailed view of HTTP response headers for web control performance. Key attributes include:

- **Server**: ASP.NET Development Server/9.0.0.0
- **Date**: Wed, 12 Mar 2008 03:29:00 GMT
- **X-AspNet-Version**: 2.0.50727
- **Content-Encoding**: gzip
- **Cache-Control**: private
- **Expires**: Thu, 12 Mar 2009 03:20:58 GMT
- **Last-Modified**: Wed, 12 Mar 2008 03:20:48 GMT

To achieve optimal web control performance, the following attributes need to be set in the project's `web.config` file:

```xml
<configuration system.web.extensions>
    <!-- ... -->
    <scripting>
        <ScriptResourceHandler enableCompression="true" enableCaching="true" />
    </scripting>
    <!-- ... -->
</system.web.extensions>
```

#### Benefits of Gzipping Resource Files

As the resource files get gzipped:

- **It saves the precious network bandwidth.**
- **It reduces the load-time.** As a result, the web form, which consists of the Syncfusion controls, will get loaded faster on the client browser.
- **It also reduces the network traffic.**

### 4.3 Working with an Excel Spreadsheet

You can use the Microsoft Excel to design spreadsheets that can be used on systems where MS Excel is not installed. This can be done by using a combination of Essential XlsIO and Essential Calculate, where:

- **Essential XlsIO** can be used to read and write the spreadsheet.
- **Essential Calculate** can be used to compute values as they are modified in the spreadsheet.

#### Example

To illustrate this process, consider the following sample project:

```
Essential Studio\X.X.X\Windows\Calculation.Windows\Samples\2.0\XlsFileUsingExcelRW
```

## API Reference (if applicable)

### Using Essential XlsIO and Essential Calculate

The integration of Essential XlsIO and Essential Calculate is designed to handle spreadsheet operations effectively without requiring MS Excel installation. Utilize these components to achieve the desired functionalities.

## Code Examples (multi-language supported)

### Example: Configuration for Web Control Performance

```xml
<configuration system.web.extensions>
    <scripting>
        <ScriptResourceHandler enableCompression="true" enableCaching="true" />
    </scripting>
</configuration>
```

### Example: Sample Project Path

```
Essential Studio\X.X.X\Windows\Calculation.Windows\Samples\2.0\XlsFileUsingExcelRW
```

## Page-level Navigation/TOC (if applicable)

- **Web Control Performance**
- **Working with an Excel Spreadsheet**

## Cross References

See also:

- **Essential XlsIO Documentation**
- **Essential Calculate Documentation**

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Essential Calculate, Essential XlsIO, Web Control Performance, Excel Spreadsheet Handling] keywords: [web.config, gzip, network bandwidth, load-time, network traffic, XlsIO, Calculate, sample project, configuration, HTTP response headers, Syncfusion] -->
```