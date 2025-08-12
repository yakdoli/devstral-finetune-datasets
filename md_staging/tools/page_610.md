<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_610.jpeg
document_name: tools
page_number: 610
page_id: tools#page_610
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:23:48Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduces the structure and validation of an XML dataset schema and corresponding XML file for Windows Forms.

## Content

### XML Schema Definition

The following XML schema defines the structure for a dataset named `NewDataSet`. It includes a roster element that can contain multiple occurrences of various employee-related elements.

```xml
<xs:element name="NewDataSet" msdata:IsDataSet="true" msdata:EnforceConstraints="False">
    <xs:complexType>
        <xs:choice maxOccurs="unbounded">
            <xs:element name="roster">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="PositionID" type="xs:string" minOccurs="0" />
                        <xs:element name="EmployeeID" type="xs:string" minOccurs="0" />
                        <xs:element name="PersonID" type="xs:string" minOccurs="0" />
                        <xs:element name="FirstName" type="xs:string" minOccurs="0" />
                        <xs:element name="LastName" type="xs:string" minOccurs="0" />
                        <xs:element name="BizUnitName" type="xs:string" minOccurs="0" />
                        <xs:element name="Title" type="xs:string" minOccurs="0" />
                        <xs:element name="FunctionalTitle" type="xs:string" minOccurs="0" />
                        <xs:element name="CorporateID" type="xs:string" minOccurs="0" />
                        <xs:element name="UserID" type="xs:int" minOccurs="0" />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:choice>
    </xs:complexType>
</xs:element>
```

### Validation of Written Schema

1. **Validate the written Schema**  
   Ensure that the provided schema is valid by validating it against an XML Schema Validator.

### Adding an XML File

2. **Add an XML file (Say newdataset.xml) with the following data**  
   The XML file should conform to the schema outlined above. Below is an example of how the XML file should be structured:

```xml
<?xml version="1.0" standalone="yes"?>
<NewDataSet xmlns="http://tempuri.org/NewDataSet.xsd">
    <roster>
        <PositionID>12345</PositionID>
        <EmployeeID>1000</EmployeeID>
        <PersonID>01</PersonID>
    </roster>
</NewDataSet>
```

### Explanation
- The `roster` element contains the details of an employee, including `PositionID`, `EmployeeID`, and `PersonID`.
- All elements are optional as indicated by `minOccurs="0"` in the schema.

## API Reference (if applicable)
- No specific API reference is provided in this content, as the focus is on XML schema definition and validation.

## Code Examples
- **XML Schema:** See the detailed schema definition provided above.
- **XML Instance:** See the example XML file structure provided above.

## Cross References
- This section focuses on XML structure and validation, typical in Windows Forms applications for managing structured data.

## RAG Annotations

<!-- tags: [syncfusion, windows forms, xml, schema definition, xml validation] keywords: [NewDataSet, roster, PositionID, EmployeeID, PersonID, XML schema, XML validation, Windows Forms] -->