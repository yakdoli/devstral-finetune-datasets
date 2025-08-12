```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: Olap Common
page_number: 077
page_id: Olap Common#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:57Z
fidelity: lossless
-->

# Essential Olap Common

## Steps in Establishing a Connection and Processing Data

### Overview
- Establish a connection to the specified data source using a connection string containing details about the data source.
- Connect to a server or an offline cube.
- Provide input for data processing using either MDX Query or OlapReport.
- Process the data based on the input type, where the method differs for OLAP base.
- Execute the MDX query or generate an MDX query from the OlapReport.
- Format the result set for the controls and display the output.

### Detailed Steps

1. **Get the input to establish a connection to the specified data source**:
   - The connection information is provided as a connection string that includes details about the data source.
   - Example connection string: `"DataSource = localhost; Initial Catalog = Adventure Works DW";`

2. **Connect to a server or an offline cube**:
   - Establish a connection to the desired data source.

3. **Provide input for data processing**:
   - Once the connection is established, input two types of inputs to process the OLAP data:
     - **MDX Query**: Write an MDX Query for the database and use that query as input.
     - **OlapReport**: Create an OLAP report and provide that report as input to the OlapDataManager.

4. **Output based on input type**:
   - The output will be the same regardless of the input type.
   - However, the processing method will differ in the OLAP base depending on the input type.

5. **Execute the MDX query**:
   - If an MDX query is given as input, the query will be executed on the connected database.

6. **Process the OlapReport**:
   - If an OlapReport is given as input:
     - **a.** An MDX query specification will be created based on the OlapReport.
     - **b.** The MDX query will be generated using the OlapQueryBuilderEngine.
     - **c.** The generated query will be executed on the connection database.

7. **Obtain the result**:
   - Once the query is executed, either from the MDX query input or the OlapReport input, the result is obtained.

8. **Format the result**:
   - The result set will be formatted to provide input for the controls.
   - The formatted input will be passed to the controls.

9. **Display the output**:
   - The output will be displayed in the controls.

### In Silverlight

1. **Requirements for OlapDataManager**:
   - The OlapDataManager requires an OlapReport and a Virtual Channel in the form of OlapDataManager.

2. **Data Binding**:
   - The OlapDataManager is a set to control, and in the `DataBind` method, the control makes an asynchronous call with the help of a virtual channel provided in OlapDataManager.

3. **Communication via WCF Service**:
   - With the help of WCF Service, the control communicates with the Olap base to retrieve the CellSet.

4. **Control-OlapDataManager Communication**:
   - The control passes the obtained CellSet to the OlapDataManager.
   - In turn, the OlapDataManager returns the PivotEngine to the control.

5. **Displaying the Output**:
   - The output will be reflected in the controls.

## 4.5.2 Steps in processing Non-OLAP data

### Overview
- Process the Non-OLAP data (such as IEnumerable, IList, DataTable, DataView, etc.) to provide the specified formatted input to the controls.
- For Non-OLAP data, no connection needs to be established.

### Processing Non-OLAP data

To process the Non-OLAP data:
1. Give the two inputs.

## API Reference (if applicable)
- [Details to be added as per the documentation]

## Code Examples (multi-language supported)
- [Code examples to be added as per the documentation]

<!-- tags: [Syncfusion Winforms, OLAP, Non-OLAP, OlapDataManager, OlapReport, MDX Query, WCF Service, CellSet, PivotEngine, Silverlight] keywords: [data processing, connection string, query execution, result formatting, output display, virtual channel, asynchronous call, data controls] -->
```