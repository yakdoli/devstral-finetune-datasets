```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: QTP
page_number: 072
page_id: QTP#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:56Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Overview
- Important notes about DLL paths
- Alternative installation paths for `Essential QuickTest Professional`
- XML code snippets for custom configuration

### Content

#### Path Assumptions and Customization

**Note:** In the preceding code, the fully qualified name of the DLL given in the `<DllName>` tag assumes that you have installed the Essential QuickTest Professional in the following default path:

**Default Path:**
```plaintext
C:\Program Files\Syncfusion\Essential QuickTest Professional\<Version number>\
```

If you have installed Essential QuickTest Professional in any other path, you need to give the correct path of the DLL in all the `<DllName>` tags. For example, if Essential QuickTest Professional is located in `D:\Essential QuickTest Professional\<version number>`, then the code should be as follows:

```xml
[XML]

<Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
    <CustomRecord>
        <Component>
            <Context>AUT</Context>
            <DllName>D:\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
        </Component>
    </CustomRecord>
</CustomReplay>
<Component>
    <Context>AUT</Context>
    <DllName>D:\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
    <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomReplay>
</Control>
```

#### Steps for Customizing Configuration

1. **Select Controls to Test:**
   - Select the segment of the code containing the controls to be tested.

2. **Copy Selected Code:**
   - On the Edit menu, click Copy.

**Note:** While selecting the code for copying, exclude the following lines of code:

```xml
[XML]

<?xml version="1.0" encoding="UTF-8" ?>
```

3. **Open Configuration File:**
   - Open the `SwfConfig.xml` file located under the following location:
   ```plaintext
   <QuickTest Professional Installation Path>\dat\SwfConfig.xml
   ```

4. **Paste Copied Segment:**
   - Paste the copied segment under the `<?xml>` tag in `SwfConfig.xml`.

### API Reference

#### File Paths
- `SwfConfig.xml`: `<QuickTest Professional Installation Path>\dat\SwfConfig.xml`

### Code Examples

#### XML Configuration Snippet
The provided XML snippet illustrates how to configure custom controls within the `SwfConfig.xml` file.

```xml
[XML]

<Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
    <CustomRecord>
        <Component>
            <Context>AUT</Context>
            <DllName>D:\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
            <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
        </Component>
    </CustomRecord>
</CustomReplay>
<Component>
    <Context>AUT</Context>
    <DllName>D:\Essential TestStudio\<Version number>\Bin\2.0\GridControl.dll</DllName>
    <TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomReplay>
</Control>
```

### Page-level Navigation/TOC
- Path Assumptions and Customization
- Steps for Customizing Configuration
- API Reference
- Code Examples

### RAG Annotations
- **Tags:** Essential QuickTest Professional, DLL Path Configuration, XML Configuration, GridControl, SwfConfig.xml
- **Keywords:** CustomRecord, Component, Context, DllName, TypeName, AUT, Syncfusion Windows Forms, GridControl, Version number, Path customization
```