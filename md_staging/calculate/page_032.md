```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: calculate
page_number: 032
page_id: calculate#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:04Z
fidelity: lossless
-->

# Essential Calculate

Essential Calculate is deployed in your Windows application.

## 3.3.2 ASP.NET

Now, you have created an ASP.NET application (refer to *Creating Platform Application*). This section illustrates how to deploy Essential Calculate into this ASP.NET application.

### Deploying Essential Calculate in an ASP.NET Application

This section provides information and instructions for deploying ASP.NET applications that use Essential Calculate. This is in addition to the section on Deploying Essential Studio for ASP.NET (*Common --> Deploying Essential Studio for ASP.NET*) in the Getting Started Guide.

Essential Calculate ships with .NET Framework 2.0 (Visual Studio 2005) version of the C# and VB.NET samples, which are installed beneath 2.0 directories. During installation, application directories are created in IIS for each of the C# and VB.NET samples.

The following steps will guide you to deploy Essential Calculate in an ASP.NET application:

1. **Marking the Application Directory**  
   The appropriate directory, usually where the aspx files are stored, must be marked as Application in IIS.

2. **Syncfusion Assemblies**  
   The Syncfusion assemblies need to be in the *bin* folder that is beside the aspx files.

---

**Note:** They can also be in the GAC, in which case, they should be referenced in the *Web.config* file.

```xml
[ASPX]
<configuration>
  <system.web>
    <compilation>
      <assemblies>
        <add assembly="Syncfusion.Calculate.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89"/>
      </assemblies>
    </compilation>
    ...
  </system.web>
</configuration>
```

## API Reference

## Code Examples

<!-- tags: [product, syncfusion-winforms, essential-calculate, asp.net, deployment, api, version-11.4.0.26] keywords: [essential calculate, asp.net deployment, syncfusion studio, application directory, assemblies, bin folder, web.config, gac] -->
```