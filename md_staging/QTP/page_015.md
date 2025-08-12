```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: QTP
page_number: 015
page_id: QTP#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:02:01Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Provides details on手动配置 `swfconfig` 文件。
- Explains the steps to configure QTP to use the custom libraries shipped with Essential QuickTest Professional.

## Content

### 2.1.2.2 Manual Configuration

This section provides details about the manual configuration of the `swfconfig` file.

#### Steps to Configure QTP to use the Custom Libraries shipped in Essential QuickTest Professional

1. Navigate to the following path:
   ```
   (Installed location of Essential QuickTest Professional)\Config
   ```
   <!-- Note: You will find three folders, named 2.0, 3.5 and 4.0 here. The folders 2.0, 3.5 and 4.0 consist of swfconfig files for .NET 2.0, .NET 3.5 and .NET 4.0 frameworks respectively. -->
   
2. Open the `swfconfig` file by double-clicking it. You can view the mapping for all the supported controls here. The sample code below maps the grid control to its corresponding DLL.

#### Example Mapping in XML

```xml
[XML]

<CC Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
<CustomRecord>
<Component>
<Context>AUT</Context>
<DllName>C:\Program files\Syncfusion\Essential TestStudio\<Version Number>\Bin\2.0\GridControl.dll</DllName>
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
```

#### Note on DLL Path

In the preceding code, the fully qualified name of the DLL given in the `<DllName>` tag assumes that you have installed the Essential QuickTest Professional in the following default path:
```
C:\Program Files\Syncfusion\Essential QuickTest Professional\<Version number>\
```

If you have installed Essential QuickTest Professional in any other path, you need to give the correct path of the DLL in all the `<DllName>` tags. For example, if Essential QuickTest Professional is located in `D:\Essential QuickTest Professional\<Version number>`, then the code should be as follows:

## API Reference
- Namespace: `Syncfusion.Windows.Forms.Grid`
- Class: `GridControl`
- DLL: `GridControl.dll`

## Code Examples

### Example: Mapping Grid Control

```xml
<CC Control Type="Syncfusion.Windows.Forms.Grid.GridControl">
<CustomRecord>
<Component>
<Context>AUT</Context>
<DllName>D:\Essential QuickTest Professional\<Version number>\Bin\2.0\GridControl.dll</DllName>
<TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomRecord>
<CustomReplay>
<Component>
<Context>AUT</Context>
<DllName>D:\Essential QuickTest Professional\<Version number>\Bin\2.0\GridControl.dll</DllName>
<TypeName>Syncfusion.TestStudio.Grid.GridControl</TypeName>
</Component>
</CustomReplay>
</Control>
```

## Page-level Navigation/TOC (if applicable)
- Manual Configuration
- Steps to Configure QTP to use the Custom Libraries shipped in Essential QuickTest Professional

## Cross References
- No direct cross references provided on this page.

<!-- tags: [Essential QuickTest Professional, Manual Configuration, swfconfig, QTP, custom libraries, .NET frameworks, Syncfusion, WinForms] keywords: [Manual Configuration, swfconfig file, QTP, custom libraries, .NET frameworks, Syncfusion, WinForms] -->
```