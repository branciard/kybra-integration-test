# Test Kybra integration 


## Prerequiste
https://demergent-labs.github.io/kybra/installation.html

Based on https://demergent-labs.github.io/kybra/hello_world.html

## deploy
'''
~/.pyenv/versions/3.10.7/bin/python -m venv venv
source venv/bin/activate
'''

'''
pip install kybra
pip install iscc_core
'''

'''
dfx stop
dfx start --clean --background

'''
dfx identity new test_unencrypted --storage-mode plaintext
dfx identity use test_unencrypted
'''

'''
dfx deploy
'''