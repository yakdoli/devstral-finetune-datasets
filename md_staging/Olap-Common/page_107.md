```html
<!--                                                                                                     
source: image                                                                                         
domain: syncfusion-sdk                                                                                
task: pdf-ocr-to-markdown                                                                             
language: en (keep original; do not translate)                                                        
source_filename: page_107.jpeg                                                                        
document_name: Olap Common                                                                            
page_number: 107                                                                                      
page_id: Olap Common#page_107                                                                         
product: Syncfusion Winforms                                                                           
version: 11.4.0.26                                                                                    
timestamp: 2025-08-09T07:21:08Z                                                                        
fidelity: lossless                                                                                   
-->                                                                                                   
                                                                                                      
## Essential OlapCommon                                                                                

### Instantiate the WCF service using Basic Http Binding and End Point Address values:                                                                         
                                                                                                      
- Declare the `IOLapDataProvider` for Service instantiation as given in the following code:                                                                    
                                                                                                      
#### C#                                                                                             
                                                                                                       ```csharp                                                                              
                                                                                           // Declaring the IOLapDataProvider for service instantiation                                                                                          
                                                                                           IOLapDataProvider DataProvider = null;                                                                                            
                                                                                                       ```                                                                                 
                                                                                                      
#### VB                                                                                            
                                                                                                       ```vb                                                                                
                                                                                           ' Declaring the IOLapDataProvider for service instantiation                                                                                          
                                                                                           Dim DataProvider As IOLapDataProvider = Nothing                                                                                  
                                                                                                       ```                                                                                 
                                                                                                      
- Specify the `basicHttpBinding` and Instantiate the `DataProvider` from the `ChannelFactory` as given in the following code:                                     
                                                                                                       [C#]                                                                                                     
                                                                                                       ```csharp                                                                              
                                                                                           private void InitializeConnection()                                                                                            
                                                                                           {                                                                                          
                                                                                                     Binding basicHttpBinding = new BasicHttpBinding(BasicHttpSecurityMode.None)                                                                                            
                                                                                                     {                                                                                      
                                                                                                       MaxBufferSize = 2147483647, MaxReceivedMessageSize = 2147483647                                                                                                              
                                                                                                     };                                                                          
                                                                                                     var Uri = App.Current.Host.Source.ToString();                                                                    
                                                                                                     EndpointAddress address = new EndpointAddress(new Uri(Uri +                                                                                                              
                                                                                                "........Services/OlapManager.svc/basic"));                                                                          
                                                                                                     ChannelFactory<IOLapDataProvider> clientChannel = new ChannelFactory<IOLapDataProvider>(basicHttpBinding, address);                                                   
                                                                                                     DataProvider = clientChannel.CreateChannel();                                                                     
                                                                                           }                                                                                          
                                                                                                       ```                                                                                 
                                                                                                      
## Page-level Navigation/TOC (if applicable)                                                          
                                                                                                      
<!-- tags: [OlapCommon, WCF service, BasicHttpBinding, IOLapDataProvider] keywords: [Instantiating WCF service, EndPointAddress, Service instantiation, C#, VB, App.Current.Host.Source, Syncfusion, Syncfusion Winforms, ChannelFactory] -->
```
