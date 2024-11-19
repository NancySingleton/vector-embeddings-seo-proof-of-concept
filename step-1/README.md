# Approach
- We already use the Screaming Frog tool.
- This tool crawls the site and produces some information about each page.
- We can configure it to run any extra JavaScript that we want on each page, and add some data to an extra column in the results.
- We want to add a script that will calculate an embedding for each page, and add it to an embedding column in the results.

# Prerequisites
- We want the script to use Open AI to calculate the embeddings.
- Communicating with Open AI requires an API key. We already have this.

# Creating the script
- Screaming Frog have a template script available that we can use.
- The script needs to be edited to include the Open AI API key.

# Using the script
- Instructions are [here](https://ipullrank.com/vector-embeddings-is-all-you-need#:~:text=How%20to%20Vectorize%20a%20Site%20with%20Screaming%20Frog%20SEO%20Spider).