*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kokkeli
    Set Password  passu001
    Set Password Confirmation  passu001
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ko
    Set Password  passu001
    Set Password Confirmation  passu001
    Submit Register Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  kokkeli
    Set Password  passu1
    Set Password Confirmation  passu1
    Submit Register Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kokkeli
    Set Password  passu001
    Set Password Confirmation  passu002
    Submit Register Credentials
    Register Should Fail With Message  Password and confirmation do not match

Login After Successful Registration
    Set Username  kokkeli
    Set Password  passu001
    Set Password Confirmation  passu001
    Submit Register Credentials
    Go To Login Page
    Set Username  kokkeli
    Set Password  passu001
    Submit Login Credentials
    Login Should Succeed
    
Login After Failed Registration
    Set Username  kokkeli
    Set Password  passu001
    Set Password Confirmation  v44r4p455u
    Submit Register Credentials
    Go To Login Page
    Set Username  kokkeli
    Set Password  passu001
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open


