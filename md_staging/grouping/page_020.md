```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: grouping
page_number: 020
page_id: grouping#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:51Z
fidelity: lossless
-->

## Essential Grouping

- Syncfusion.Shared.Base.dll
- Syncfusion.Shared.Windows.dll

Essential Grouping is now deployed in your Windows / WPF applications.

### 3.2.2 ASP.NET

Now, you have created a ASP.NET application (refer Creating Platform Application). This section will guide you to deploy Essential Grouping in an ASP.NET Application.

The following steps will guide you to deploy Essential Grouping in an ASP.NET application:

1. **Marking the Application directory**-The appropriate directory, usually where the aspx files are stored, must be marked as Application in IIS.
2. **Syncfusion Assemblies**-The Syncfusion assemblies need to be in the bin folder that is beside the aspx files.

**Note:** They can also be in the GAC, in which case, they should be referenced in Web.config file.

#### Configuration in Web.config

```xml
<configuration>
    <system.web>
        <compilation>
            <assemblies>
                <add assembly="Syncfusion.Grid.Grouping.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89"/>
            </assemblies>
        </compilation>
        .
        .
        .
    </system.web>
</configuration>
```

**Note:** The version numbers in the above references will vary depending on the version you are linking to.

1. **Data Files**-If you have .xml, .mdb, or other data files, ensure that they have sufficient security permission. Authenticated Users should have full control over the files and the directories in order to give ASP.NET code, enough permissions to open the file during runtime.
```html
```