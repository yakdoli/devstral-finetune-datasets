```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: pdf
page_number: 039
page_id: pdf#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:26:28Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Deploys Essential PDF in an ASP.NET application by setting up the application directory and configuring Syncfusion assemblies.

## Content

### Figure: Sample Application Directories in IIS

The following steps will guide you to deploy Essential PDF in an ASP.NET application:

1. **Marking the Application directory**  
   - The appropriate directory, usually where the aspx files are stored, must be marked as Application in IIS.

2. **Syncfusion Assemblies**  
   - The Syncfusion assemblies need to be in the `bin` folder that is beside the aspx files.

   **Note:** They can also be in the GAC, in which case, they should be referenced in the Web.config file.

   ```xml
   [ASPX]
   <configuration>
       <system.web>
   ```

## Page-level Navigation/TOC (if applicable)
- The provided content details the deployment steps for Essential PDF in an ASP.NET application.

## Cross References
- See also: [Syncfusion Assemblies], [Application Directory Configuration], [Web.config References]

<!-- tags: [essential-pdf, asp-net-application, application-deployment, syncfusion-applications] keywords: [essential pdf, aspx files, bin folder, gac, web.config, iis] -->
```