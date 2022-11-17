#Feature: Jules.app sign_up test
#
#  Background:
#    Given sign up: I am a user on jules sign up page
#
#    @jules_test_debug
#    Scenario: I create an account
#      When sign_up: I click sign up button
#      When sign_up: I click personal button
#      When sign_up: I click continue button
#      When sign_up: I send first name "marian"
#      When sign_up: I click continue first name button
#      When sign_up: I send last name "negru"
#      When sign_up: I click last_name_continue_button
#      When sign_up: I set my email to "asad"
#      Then sign_up: I receive message:Please enter a valid email address