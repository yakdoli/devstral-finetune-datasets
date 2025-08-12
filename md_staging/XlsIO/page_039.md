```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: XlsIO
page_number: 039
page_id: XlsIO#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:50:39Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page provides steps to deploy Essential XlsIO in an ASP.NET application.

## Content

### 1. Marking the Application Directory

The appropriate directory, usually where the aspx files are stored, must be marked as Application in IIS.

### 2. Syncfusion Assemblies

The following Syncfusion assemblies need to be in the `bin` folder that is beside the aspx files:

- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.XlsIO.Base.dll

They can also be in the GAC, in which case, they should be referenced in the `Web.config` file using the following code:

```xml
[ASPX]
<configuration>
    <system.web>
        <compilation>
            <assemblies>
                <add assembly="Syncfusion.XlsIO.Base, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89" />
            </assemblies>
        </compilation>
        ...
    </system.web>
</configuration>
```

**Note:** `X.X.X` in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.

### Additional Resources

Please refer to the document in the following location for a step-by-step process of Syncfusion assemblies deployment in ASP.NET:

```plaintext
http://www.syncfusion.com/support/user/uploads/webdeployment_c883f681.pdf
```

### Figure: Sample Application Directories in IIS

The following steps will guide you to deploy Essential XlsIO in an ASP.NET application:

<!-- tags: [Essential XlsIO, ASP.NET, deployment, Syncfusion Assemblies, WebDeployment, GAC] keywords: [dotnet, aspx, bin folder, Application Directory, Web.config, Syncfusion.Core.dll, Syncfusion.Compression.Base.dll, Syncfusion.XlsIO.Base.dll, versioning] -->
```