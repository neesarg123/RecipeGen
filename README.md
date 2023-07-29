## Be Organized and Inspired with RecipeGen
### What this is
With **Notion**, we can easily keep track of what items we have in our household. This can be very useful when you're about to go grocery shopping and need to know which items you need to buy.

With **ChatGPT**, you can ask for a step-by-step recipe of virtually any dish and even ask it to generate one on the fly by giving it a list of available ingredients in your pantry.

So why not **merge these two amazing use cases together** to allow for a **streamlined experience of cooking novel recipes based on the ingredients you possess**?
### How to use
#### Setting up the Notion side
Step 0: Download Notion

Step 1: Create a page with a database. Add **at least two columns: 1 for Text and 2 for Checkbox**. For example, I have a column named "Item" (to put the name of the items) and a checkbox column named "Have it?". `NOTE:` if you put different names for your columns, you will need to change the variable values within the `"get_database_entries.py"` file -- `TEXT_COLUMN_NAME` and `CHECKBOX_COLUMN_NAME`

Step 2: Acquire ID of the database (See [link](https://stackoverflow.com/questions/67728038/where-to-find-database-id-for-my-database-in-notion#:~:text=If%20this%20is%20just%20for%20yourself%2C%20you%20can%20get%20the%20database%20ID%20from%20the%20URL%20of%20the%20page%3A)). Now store this token as an OS environment variable -- call it NOTION_DATABASE_ID

Step 3: Get A Notion Token (by making an internal integration) (See [link](https://www.notion.so/my-integrations)). Now store this token as an OS environment variable -- call it NOTION_TOKEN

Step 4: Add the integration within your Notion page (created in Step 1) (See [link](https://developers.notion.com/docs/create-a-notion-integration#:~:text=Go%20to%20the,for%20connections...%20menu.))

All done! Customize your Notion page to your liking...add new columns if you want, it's all good!

#### Setting up the OpenAI side
Step 0: Get an OPENAI API token from here: [link](https://platform.openai.com/account/api-keys)

`NOTE: Yes, you will have to provide payment information and you will be billed based on your own use of your own API token`

Step 1: Once again, store this token as an OS environment variable -- call it OPENAI_API_TOKEN

All set! Now simply run the `"get_chat_gpt_response.py"` file and see your recipes pop up under the "Recipes/" directory!
