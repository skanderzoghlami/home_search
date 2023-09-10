import time
import requests
import winsound

while True:
    try:
        # Make the API call here
        response = requests.get('http://127.0.0.1:8000/api/make-api-calls/')
        
        # Process the response as needed
        if response.status_code == 200:
            data = response.json()
            print(data['message'])
            
            if data['message'] == 'Something is available!':
                # Play a notification sound
                winsound.Beep(1000, 1000)  # 1000 Hz frequency, 1000 ms (1 second) duration
        
        else:
            print(f"API call failed with status code {response.status_code}")
        
        # Wait for 10 seconds before the next API call
        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # You might want to handle exceptions gracefully here
