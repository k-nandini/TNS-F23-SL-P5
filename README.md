# TNS-F23-SL-P5
Assignment 4 for Core Systems Lab - Self as System (Digital Diva)
	- https://digital-diva.onrender.com/

# Instructions
1) Click/Tap on "Let's Talk" or Press "SPACEBAR" to get an advice.
2) Click/Tap on "Tell me more." or Press "SPACEBAR" to generate a new advice.
3) To update advice change the URL to "~/import_data"
   	- This will update the database from the CSV file and add new data.
   	- The data in the CSV file is generated from my Youtube Comments data.
   	- NOTE: The CSV file is located in the static folder >> assets >> csv.
4) To remove duplicates change the URL to "~/remove_duplicates"
	- NOTE: Remove duplicates has known bugs and will remove all data.
	- Hence: For now please execute "step 4" and then execute "step 3" to only import fresh data.
 
# Future areas of improvement
- Animation for advice text: - advice could be shown with a typing animation like ChatGPT. 
- Fix remove_duplicates function.
- Add better navigation and make the app more intuitive.
- Create a page to upload the CSV/Update the CSV file from the web page.
- Add Authentication for backend functions such as updating DB from CSV, and removing duplicates.
- Random color generated background
- User can input a question before generating a random quote from DB, so it is more interactive (like an actual life coach).
