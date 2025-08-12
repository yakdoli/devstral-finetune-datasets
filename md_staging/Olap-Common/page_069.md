```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: Olap Common
page_number: 069
page_id: Olap Common#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:25Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
olapDataManager.MdxQuery = "MDX Query Here"
olapDataManager.ExecuteCellSet()
```

### 4.3.17 Virtual KPI Element

Key performance indicators can be virtually defined during run time. This feature enables users to create KPIs without storing them in SSAS (SQL Server Analysis Services). This feature is very useful when users want to define KPIs at run time and also minimize the time necessary to create KPIs.

#### 4.3.17.1 Properties

**Table 12: VirtualKpiElement Class Properties**

| Property             | Description                                    | Type | Data Type |
|----------------------|------------------------------------------------|------|-----------|
| Name                 | Gets or sets the name for VirtualKpiElement.  | CLR  | String    |
| KpiValueExpression   | Gets or sets the value which indicates the value expression for VirtualKpiElement. | CLR  | String    |
| KpiGoalExpression    | Gets or sets the value which indicates the goal expression for VirtualKpiElement. | CLR  | String    |
| KpiStatusExpression  | Gets or sets the value which indicates the status expression for VirtualKpiElement. | CLR  | String    |
| KpiTrendExpression   | Gets or sets the value which indicates the trend expression for VirtualKpiElement. | CLR  | String    |
| KpiTrendGraphic      | Gets or sets the name of the graphic used to represent the result of the trend expression. | CLR  | String    |
| KpiStatusGraphic     | Gets or sets the name of the graphic used to represent the result of the status expression. | CLR  | String    |

**Table 13: OlapReport Class Properties**

<!-- tags: [syncfusion, winforms, olap, kpi, virtual kpi, mdx query, sql server analysis services, ssas, essential olapcommon] keywords: [kpi, runtime, mdx, ssas, virtual, data type, expression, status, trend, graphic, asynchronous, essential olap] -->
```