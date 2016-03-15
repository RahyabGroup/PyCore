# Created by root at 1/6/16
Feature: a user can subscribe for notification (SSE) with user Id and message type

  Scenario Outline: a registered user can subscribe for notifications with user Id and message type
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an email and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When user "<userX>" subscribes for notifications with type "<message_type>" from server - subscribe
    And we send a push notification to the user "<userX>" with type "<message_type>" - push
    Then the notifications will be received for user "<userX>" successfully
    Examples:
    | userX | message_type  |
    | X     | wall-post     |


#  Scenario Outline: a registered user cant subscribe to SSE with empty user id
#    Examples:
#    | userX | message_type  |
#    | X     | wall-post     |
#

#  Scenario Outline: a registered user cant subscribe to SSE with invalid user id
#    Examples:
#    | userX | message_type  |
#    | X     | wall-post     |
#
#
#  Scenario Outline: a registered user cant subscribe to SSE with empty message_type
#    Examples:
#    | userX | message_type  |
#    | X     | wall-post     |
#
#
#
#  Scenario Outline: a registered user can subscribe to SSE twice
#    Examples:
#    | userX | message_type  |
#    | X     | wall-post     |


#
# @api.route("/notification/")
# def index():
#     debug_template = """
#      <html>
#        <head>
#        </head>
#        <body>
#          <h1>Server sent events</h1>
#
#          <div id="event"></div>
#
#          <input type="text" name="user_id" value="5691150ecae6cd5820f71671">
#          <input type="text" name="message_type" value="wall-post">
#
#          <script type="text/javascript" >
#          var eventOutputContainer = document.getElementById("event");
#          str1 = "http://localhost:8084/api/v1.0/notification/";
#          str2 = document.getElementsByName('user_id')[0].value;
#          str3 = document.getElementsByName('message_type')[0].value;
#          str4 = str1.concat(str2).concat("/").concat(str3);
#          var evtSrc = new EventSource(str4);
#
#          evtSrc.onmessage = function(e) {
#              console.log(e.data);
#              eventOutputContainer.innerHTML = e.data;
#          };
#          </script>
#        </body>
#      </html>
#     """
#     return (debug_template)