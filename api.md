# KYJstream Api Document

## Logs Api
### GET `/kyj_stream/logs`
#### URL Params
ex. `/kyj_stream/logs?time_begin=20210425T185613&time_end=20210425T185617&names=werkzeug,root&keywords=Debugger||Restarting&levels=WARNING&regex=^\*`  
All params are case sensitive  

##### time_begin
ex. `time_begin=20210425T185613`  
default: 20210301  
  
  
##### time_end
ex. `time_end=20210425T185617`  
default: {now}  
  
  
##### names  
ex. `names=werkzeug,root`  
please seperate with `,`  
  
  
##### levels  
ex. `levels=WARNING,INFO`  
please seperate with `,`  
  
  
##### keywords  
For single keyword  
ex. `keywords=Debugger`  
  

For AND condition  
ex. `keywords=Debugger%26%26restarting`  
%26 is HTML encoding for `&`  
so in input area, it should be `Debugger&&Restarting`  
  
For OR condition  
ex. `keywords=Debugger||restarting`  
  
P.S. Cannot use AND and OR at the same time  
If there is complicated condition required, please use regex in regex field.  
  
  
##### regex
Directly write your regex.
ex. `regex=^\*` (messages that start with `*`)
  

#### Response
```
{
  "status":"success",
  "data":{
    "logs":[
      {
        "time":"2021-04-25 18:56:13",
        "name":"werkzeug",
        "level":"WARNING",
        "msg":"* Debugger is active!"
      },
      {
        "time":"2021-04-25 18:56:17",
        "name":"root",
        "level":"WARNING",
        "msg":"Restarting"
      }
    ]
  }
}
```