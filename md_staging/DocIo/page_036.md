```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: DocIo
page_number: 036
page_id: DocIo#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:19Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes the unsupported features under the current scenario.
- Guides through deploying Essential DocIO in an ASP.NET application.

## Content

### Unsupported Features
However, the following features are not currently supported under this scenario.
- **OLE Object**

### Deployment Steps for ASP.NET
The following steps will guide you to deploy Essential DocIO in an ASP.NET application:

1. **Marking the Application directory**
   - The appropriate directory, usually where the aspx files are stored, must be marked as Application in IIS.
2. **Syncfusion Assemblies**
   - The Syncfusion assemblies need to be in the bin folder that is beside the aspx files.
   
   **Note**: They can also be in the GAC, in which case, they should be referenced in Web.config file.

   ```xml
   [ASPX]
   <configuration>
     <system.web>
       <compilation>
         <assemblies>
           <add assembly="Syncfusion.DocIO.Base, Version=X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89" />
         </assemblies>
       </compilation>
     </system.web>
   </configuration>
   ```

   **Note**: X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.

3. **Data Files**
   - If you have .xml, .mdb, or other data files, ensure that they have sufficient security permission.
   - Authenticated Users should have full control over the files and the directories in order to give ASP.NET code, enough permission to open the file during runtime.

### Additional Reference
Refer to the document in the following path, for step-by-step process of Syncfusion assemblies deployment in ASP.NET:

```plaintext
http://www.syncfusion.com/support/user/uploads/webdeployment_c883f681.pdf
```

## Tags and Keywords
<!-- tags: Essential DocIO, Syncfusion, ASP.NET, deployment, OLE Object, Syncfusion Assemblies, GAC, security permissions, XML, MDB, Data Files, authenticated users, file permissions, reference document, user guide, version 11.4.0.26, Windows Forms keywords: Essential DocIO, deployment, application directory, Syncfusion Assemblies, GAC, security settings, data files, authenticated users, file permissions -->
```