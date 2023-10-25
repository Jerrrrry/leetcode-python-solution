Describe a difficult interaction you had with a customer. How did you deal with it? What was the outcome? How would you handle it differently?  

Give me an example of a tough or critical piece of feedback you received. What was it and what did you do about it?  

Have you ever created a metric that helped identify a need for a change in your department? What was the metric? Why did you create it? How did this and other information influence change? What was the outcome of the change?  

You have thousands of alarm definitions stored in a file that you need to ensure are 
set up to monitor key metrics within your application stack. 

There is an [ALARM SERVICE] which provides a (C)reate(R)read(U)pdate(D)elete REST API 
and an SDK client in the language of your choice.

Write an alarm [INGESTION SERVICE] which synchronizes the alarms in the service
using the [REST CRUD API] so that every time you run the ingestion program it ensures the alarms 
contained in the alarms service match the ones in the [INPUT FILE].
  - Create alarms that don't exist
  - Update alarms that do exist
  - Delete alarms that don't exist.

Block Diagram
[INPUT FILE] <-- [INGESTION SERVICE] ---<CREATE/UPDATE/DELETE>----> [ALARM SERVICE]

[INPUT FILE] Format with Header
name,threshold,metric_name,comparison_method,alarm_state,tracking_metric_id,contact,metric_math

[ALARM CRUD API] Methods
 
Method: client.create(<alarm_definition_request_object)
Desc: Creates a new alarm in the alarm service.
Input: <alarm_definition_request_object>
Output: <alarm_client_response_object>
  
Method: client.read(<alarm_name>)
Desc: Returns an alarm definition based on alarm name
Input: <alarm_name>
Output: <alarm_definition_request_object>

Method: client.list_alarms()
Desc: Returns a list of alarms from the alarm service
Output: array<alarm_definition_request_object>

Method: client.update(<alarm_definition_request_object>)
Desc: Update an alarm
Output: <alarm_client_response_object>

Method: client.delete(<alarm_name>)
Desc: Deletes an alarm 
Input: <alarm_name>
Output: <alarm_client_response_object>

[ALARM CRUD API] Request and Response Objects

<alarm_definition_request_object> for CREATE/UPDATE API operations.
{
    'name': "alarm_name",
    'params': {
        'threshold': "3",
        'metric_name': "foo",
        'comparison_method': "gt", # Also can be gte, lt, lte, eq, neq 
        'alarm_state': "active" # Also can be set to "inactive" or "in_alarm"
        'tracking_metric_id': "uuid-string-here-for-tracking-metric",
        'contact': [
            "user@example.com", 
            "ldap:ldap-group-name", 
            "posix:posix-group-name", 
            "ticket:path-to-ticket"
        ],
        'metric_math': "sum", # Also could have avg, max, p90, p50, median, mode, etc.
    }
}
    
<alarm_client_response_object> for READ/UPDATE/DELETE API operations
{
    'name': "alarm_name", 
    'status': '200' . # Also can be 400,500, etc.
}



  