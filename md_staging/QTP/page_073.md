```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: QTP
page_number: 073
page_id: QTP#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:16Z
fidelity: lossless
-->

## Essential QuickTest Professional

### SwfConfig.xml File Structure

The `SwfConfig.xml` file will look like the following:

```xml
[XML]
<?xml version="1.0" encoding="UTF-8" ?>
<Controls>
    <Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
        <CustomRecord>
            <Component>
                <Context>AUT</Context>
                <DllName>C:\Program Files\Syncfusion\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
                <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
            </Component>
        </CustomRecord>
        <CustomReplay>
            <Component>
                <Context>AUT</Context>
                <DllName>C:\Program files\Syncfusion\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
                <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
            </Component>
        </CustomReplay>
    </Control>
    .........
</Controls>
```

**Note**: Ensure that the `<DllName>` element contains the correct path to the corresponding DLL.

### Steps to Handle SwfConfig.xml

7. Save the `SwfConfig.xml` file.

8. Restart QTP once the `SwfConfig.xml` file is saved to refresh the mappings to the required controls before starting the test.

**Note**: Mapping for the required controls can be done in a similar manner.

## 7.1.2 How to Know Whether My SwfConfig File Holds an Invalid Assembly Path Reference

### Overview
- This section explains how to identify if the `swfconfig` file contains an invalid assembly path reference.

### Steps to Verify

1. Open the Syncfusion Essential QTP Configurator located at (Installed location of Essential QuickTest Professional)\\Utilities\\SwfConfigUtility\\SwfConfigUtility.exe.

### Additional Information
- Use the Syncfusion Essential QTP Configurator tool to ensure that the paths in the `swfconfig` file are valid and point to the correct assemblies.

## API Reference (if applicable)

### WinForms-specific conventions
- The `SwfConfig.xml` file is crucial for mapping controls and their corresponding DLLs for automation purposes.

### Code Examples

```csharp
// Example of a control mapping in SwfConfig.xml
<Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
    <CustomRecord>
        <Component>
            <Context>AUT</Context>
            <DllName>C:\Path\To\Your\Dll\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
        </Component>
    </CustomRecord>
</Control>
```

### Cross References
- For more information on configuring essential assemblies, refer to the Syncfusion documentation on control mapping.

<!-- tags: [syncfusion-sdk, swfconfig, qtp, control-mapping] keywords: [swfConfigUtility, dllname, typename, syncfusion.windows.forms.grid.gridcontrol] -->
```
