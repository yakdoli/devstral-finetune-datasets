```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: DocIo
page_number: 045
page_id: DocIo#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:22Z
fidelity: lossless
-->

## Overview

- Essential DocIO is deployed in an ASP.NET MVC application by adding necessary assemblies and configurations in the Web.config file.
- Word documents can be created directly within an ASP.NET MVC application using Essential DocIO.

## Content

### 3.3.5 ASP.NET MVC

Now, you have created an ASP.NET MVC application (refer to *Creating Platform Application*). This section covers the following:

- Deploying Essential DocIO in an ASP.NET MVC Application
- Creating a Word document in an ASP.NET MVC Application

#### Deploying Essential DocIO in an ASP.NET MVC Application

The following steps will guide you to deploy Essential DocIO:

1. **Add the Syncfusion.DocIO.Base assembly into the Reference folder** to deploy Essential DocIO to the application.

2. **Add the following assembly reference under the `<compilation>` tag of Web.config file**:

   ```xml
   [ASPX]

   <compilation debug="true">
       <assemblies>
           ...
           <add assembly="Syncfusion.DocIO.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89"/>
           ...
       </assemblies>
   </compilation>
   ```

   > **Note:** `X.X.X.X` in the above code corresponds to the version number of the Essential Studio version that you are currently using.

3. **Add the following under the `<namespaces>` tag of Web.config file**:

   ```xml
   [ASPX]
   ```

```html
<!-- tags: [Essential DocIO, ASP.NET MVC, Word document creation, deployment, Assembly configuration, Web.config, Syncfusion.DocIO.Base] keywords: [Essential DocIO, ASP.NET MVC, creating Word documents, deploying DocIO, Web.config, Syncfusion.DocIO.Base, Version configuration, namespace declaration, PublicKeyToken] -->
```