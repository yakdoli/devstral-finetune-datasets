```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: XlsIO
page_number: 054
page_id: XlsIO#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:16Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- The section discusses the deployment and integration of Essential XlsIO in an ASP.NET MVC application.
- It covers features like encryption, decryption, Ole Objects, tracking changes, and handling streams and tables in XlsIO documents.

## Content

### Feature Support Comparison

| Feature         | Yes | No |
|-----------------|-----|----|
| Encryption      | Yes | Yes |
| Decryption      | No  | No  |
| Ole Objects     | No  | No  |
| Track changes   | No  | No  |
| Streams         | Yes | Yes |
| Tables          | No  | No  |

### 3.3.5 ASP.NET MVC

Now, you have created a ASP.NET MVC application (refer Creating a Platform Application). This section covers the following:

- Deploying Essential XlsIO in an ASP.NET MVC Application
- Create and add a XlsIO document with pages to the application

#### Deploying Essential XlsIO in an ASP.NET MVC Application

The following steps will guide you to deploy Essential XlsIO:

1. Add the **Syncfusion.XlsIO.Base** assembly into the Reference folder to deploy Essential XlsIO to the application.
2. Add the following assembly reference under `<compilation>` tag of Web.config file.

```xml
[XML]
<compilation debug="true">
    <assemblies>
        ...
        <add assembly="Syncfusion.XlsIO.Base, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89"/>
        ...
    </assemblies>
</compilation>
```

## Code Examples
The code snippet demonstrates adding the `Syncfusion.XlsIO.Base` assembly to the Web.config file for an ASP.NET MVC application.

<!-- tags: [Essential XlsIO, ASP.NET MVC, deployment, configuration] keywords: [Syncfusion.XlsIO.Base, assembly, Web.config, encryption, decryption, Ole Objects, stream, table] -->
```