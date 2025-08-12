```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: HTMLUI
page_number: 106
page_id: HTMLUI#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:09:21Z
fidelity: lossless
-->

## HTMLUI Tables Sample

### Overview
- Demonstrates how to implement Tables using HTMLUI.
- Includes various table configurations like colspan, rowspan, and nested tables.
- Covers topics discussed in the broader "Loading HTML" section.

### Content

#### HTMLUI Tables Sample
This sample illustrates how to implement Tables using HTMLUI. Below is a visualization of the sample:

**Figure 34: HTMLUI Tables Sample**

The sample includes the following tables:

1. **Table 1**
   - **Row 1:** Contains a column with `Colspan=3`.
   - **Row 2:** Displays a custom height in the first column.
   
   ```html
   <table>
     <tr>
       <th colspan="3">This is a column with Colspan=3</th>
     </tr>
     <tr>
       <td>Column 1 with custom height</td>
       <td>Column 2</td>
       <td>Column 3</td>
     </tr>
   </table>
   ```

2. **Table 2**
   - **Row 1:** Contains a column with `Rowspan=2`.
   
   ```html
   <table>
     <tr>
       <td rowspan="2">Column 1 with rowspan=2</td>
       <td>Column 2</td>
       <td>Column 3</td>
     </tr>
     <tr>
       <td>Column 2</td>
       <td>Column 3</td>
     </tr>
   </table>
   ```

3. **Table 3**
   - **Row 1:** Contains a nested table within a cell.
   
   ```html
   <table>
     <tr>
       <td>
         <table>
           <tr>
             <th>Nested Table</th>
           </tr>
           <tr>
             <td>Column 1</td>
             <td>Column 2</td>
             <td>Column 3</td>
           </tr>
           <tr>
             <td>Column 1</td>
             <td>Column 2</td>
             <td>Column 3</td>
           </tr>
           <tr>
             <td>Column 1</td>
             <td>Column 2</td>
             <td>Column 3</td>
           </tr>
         </table>
       </td>
     </tr>
   </table>
   ```

#### Location of the Sample
By default, this sample can be found under the following location:

```
C:\Documents and Settings\username\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\HTMLUI.Windows\Samples\2.0\HTML Tags\HTMLUITables
```

## Page-level Navigation/TOC
- **Section:** 4.10.1 HTMLUI Tables Sample

## Cross References
- **Related Section:** Loading HTML

<!-- tags: HTMLUI, Tables, WinForms, Syncfusion, rowspan, colspan, nested tables, version: 11.4.0.26 -->
```