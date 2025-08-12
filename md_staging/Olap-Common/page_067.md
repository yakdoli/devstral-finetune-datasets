```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: Olap Common
page_number: 067
page_id: Olap Common#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:35Z
fidelity: lossless
-->

# Essential OlapCommon

## 4.3.16 MDX Query Parsing

### 4.3.16.1 MDX Query binding with drill up and drill down operations

This feature provides support for the drill up and drill down operations for BI components such as BI Grid, BI Chart, and BI Client in order to view the OLAP data through different levels using an MDX query instead of the OlapReport class. Previously, the drill up and drill down operations were supported by the OlapReport class only.

#### Use Case Scenarios

This feature is useful when the user wants to perform drill up or drill down operations with the OLAP data using an MDX query instead of the OlapReport class.

#### Properties

Table: Property Table

| Property                | Description                                                                                   | Type | Data Type | Reference links |
|-------------------------|-----------------------------------------------------------------------------------------------|------|-----------|----------------|
| AllowMdxToRepo         | Gets or sets a value indicating whether to parse the given MDX into the OlapReport class or not. The default value is true. | CLR   | Boolean   | N/A             |
| Parse                  |                                                                                               |      |           |                 |

#### Sample Links

- **OlapGrid [WPF]**  
  `<InstalledDrive>:\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<version>\WPF\OlapGrid.WPF\Samples\Defining Reports\MDX Query Demo`

- **OlapChart [WPF]**  
  `<InstalledDrive>:\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<version>\WPF\OlapChart.WPF\Samples\Defining Reports\MDX Query Demo`

- **OlapClient [WPF]**  
  `<InstalledDrive>:\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\WPF\OlapClient.WPF\Samples\Product Showcase\MDX Query Demo`

- **OlapGrid [Silverlight]**

<!-- tags: [product, syncfusion, winforms, mdx query, olapreport, drill up, drill down, bi grid, bi chart, bi client] keywords: [mdx query, olapreport, drill operations, olapgrid, olapchart, olapclient, syncfusion winforms, essential studio] -->
```