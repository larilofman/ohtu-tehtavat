*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  laril  passu666
    Output Should Contain  User with username laril already exists

Register With Too Short Username And Valid Password
    Input Credentials  oi  passu666
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  pirre  lyhyt
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  liisa  oikeinpitkapassu
    Output Should Contain  Password too simple

*** Keywords ***
Create User And Input New Command
    Create User  laril  passu123
    Input New Command
