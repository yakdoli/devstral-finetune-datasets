```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_266.jpeg
document_name: DocIo
page_number: 266
page_id: DocIo#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:02Z
fidelity: lossless
-->

# Essential DocIO

```csharp
Dim document As IWordDocument = New WordDocument("MailMergeDocument.doc")

' Mail merge operations with string arrays data sources
Dim fieldNames As String() = New String() {"Continent", "Country", "Region"}
Dim fieldValues As String() = New String() {"Eurasia", "Germany", "Bavaria"}
document.MailMerge.Execute(fieldNames, fieldValues)

' Mail merge operations with DataTable data source containing data from database.
Dim table As DataTable = GetDataTable("select * from Geography")
document.MailMerge.Execute(table)

' Mail merge operations with DataView data source, created basing on the DataTable
Dim dataView As DataView = New DataView(GetDataTable("select * from Geography"))
dataView.Sort = "CountryName ASC"
document.MailMerge.Execute(dataView)

' Mail merge operations with DataReader data source
Dim dataReader As IDataReader = GetDataReader("select * from Geography ")
document.MailMerge.Execute(dataReader)
dataReader.Close()

' Mail merge operations for the specified region
Dim table As DataTable = GetDataTable("select * from Employees")
table.TableName = "Geography"
document.MailMerge.ExecuteGroup(table)

document.Save("AfterMailMerge.doc")
' or
document.Save("AfterMailMerge.docx", FormatType.Docx)
```

It is also possible to conditionally format the merge fields dynamically by using the MergeField events.

## See Also

- Nested Mail Merge
- Mail merge Events
- Additional Mail Merge Features

### 4.6.1 Nested Mail Merge
```