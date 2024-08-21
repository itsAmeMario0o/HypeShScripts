# HypeShScripts

Run in a virtual environment:
# python -m venv venv
# source venv/bin/activate

Set environment variable on your machine. For MacOS:

nano ~/.bash_profile
export BEARER_TOKEN="your_token_here"

Save and close

To ensure the changes are effective, reload shell:

source ~/.bash_profile

Verify environment variable set:

echo $BEARER_TOKEN