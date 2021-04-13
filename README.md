#  Step for setup the cab_booking project

Step 1. Install python(V3.9), django(V3.1.6) and djnago restframework(V3.12.2).

      pip install djangorestframework
      
Step 2. Update your SECRET_KEY in config.py file.
        
        By default it has sqlite3 but you want to use Mysql or anyother database, then remove sqlite3 config settings from setting.py file and update the                   required server configuration in Config.py file as eg given for mysql in comments
        
Step 3. Now, we are done with the pre-requisites. Run the migration command to create the tables schema by the commands as given below.

          1. python3 manage.py makemigrations
          2. python3 manage.py migrate

Step 4. Run the server.
        
        python3 manage.py runserver
        
Step 5. Register the driver by using driver_registation API via POSTMAN or django server. request POST : http://127.0.0.1:9000/api/v1/driver/register/
       
       
       Example request body given below,update the content in <> with the real content
           BODY :   {
                      "email": "<author@xyz.com>",
                      "name": "<driver_name>",
                      "phone_number": <phone_number>,
                      "license_number": "<license_number>",
                      "car_number": "<car_number>"
                      
                  }
          
    After the successful registration, you will be receving the response  as below   
    
    Response:{
                      "id":<id_number>
                      "email": "<author@xyz.com>",
                      "name": "<driver_name>",
                      "phone_number": <phone_number>,
                      "license_number": "<license_number>",
                      "car_number": "<car_number>"
                      
                  }
                  
  Step 6. enter the driver location by using driver/sendlocation api 
          request post :http://127.0.0.1:9000/api/v1/driver/sendlocation/
          
          
          Example request body given below,update the content in <> with the real content
           BODY :{
                    "driver": <driver_id>,
                    "latitude": <latitude>,
                    "longitude": <longitude>
                }
                
          After the successful , you will be receving the response  as below   
    
       Response:{   "id":<location_id>
                    "driver": <driver_id>,
                    "latitude": <latitude>,
                    "longitude": <longitude>
                }
                
                
  step7. Find the near by driver list by using GetListOfAvailableCab  API
          request post : http://127.0.0.1:9000/api/v1/passenger/available_cabs/
        
        
         Example request body given below,update the content in <> with the real content
           BODY :{
                   
                    "latitude": <passenger_latitude>,
                    "longitude": <passenger_longitude>
                }
            After the successful, you will be receving the response  as below   
    
           Response: list of avaiable cabs or 
                     {
                          "Unavailable": "Sorry, no cabs are available at this time"
                      }

  
                
  Thankyou
                  
  
