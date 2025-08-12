```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_071.jpeg
document_name: QTP
page_number: 071
page_id: QTP#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:33Z
fidelity: lossless
-->

# 7 Frequently Asked Questions

## 7.1 General

### 7.1.1 How to manually configure Syncfusion control to work with QTP

#### Steps to Configure QTP to use the Custom Libraries shipped in Essential QuickTest Professional

1. Navigate to the following path:
   ```
   (Installed location of Essential QuickTest Professional)\Config
   ```
   **Note:** You will find three folders here: 2.0, 3.5, and 4.0. The folders 2.0, 3.5, and 4.0 consist of `swconfig` files for .NET 2.0, .NET 3.5, and .NET 4.0 frameworks respectively.

2. Open the `swconfig` file by double-clicking it. You can view the mapping for all the supported controls here. Given below is the sample code that maps the grid control to its corresponding DLL.

   ```xml
   [XML]
   <CC ControlType="Syncfusion.Windows.Forms.Grid.GridControl">
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
   </CC>
   ```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content: <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
- Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: QTP#page_071#getting-started -->. Do not add if the heading text is unclear.
```

<!-- tags: [Syncfusion Winforms, QTP, configuration, control mapping, swconfig] keywords: [Syncfusion, Essential QuickTest Professional, grid control, DLL mapping, XML configuration] -->