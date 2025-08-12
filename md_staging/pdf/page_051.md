```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_051.jpeg
document_name: pdf
page_number: 051
page_id: pdf#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:27:13Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Deploying Essential PDF in an ASP.NET MVC Application
- Creating and adding a PDF document with pages to the application

## Content

### Deploying Essential PDF in an ASP.NET MVC Application

The following steps will guide you to deploy Essential PDF:

1. **Add the Syncfusion.Pdf.Base assembly into the Reference folder to deploy Essential PDF to the application.**

2. **Add the following assembly reference under `<compilation>` tag of Web.config file.**

   ```xml
   [ASPX]
   <compilation debug="true">
       <assemblies>
           ...
           <add assembly="Syncfusion.Pdf.Base, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89"/>
           ...
       </assemblies>
   </compilation>
   ```

3. **Add the following under `<namespaces>` tag of Web.config file.**

   ```xml
   [ASPX]
   <namespaces>
       ...
       <add namespace="Syncfusion.Pdf"/>
       ...
   </namespaces>
   ```

Essential PDF is now deployed in your ASP.NET MVC application.

### Create and add a PDF document with pages to the application

The following steps illustrate how to create a Word document in an MVC application.

#### Step 1: View

```markdown
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [pdf, deployment, mvc, asp.net, essential pdf, web.config] keywords: [syncfusion.pdf.base, web.config, namespaces, assemblies, compile, essentialpdf, mvc application] -->
```