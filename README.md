1.Title: Registration
	Description -To check if registration works in "Twitch.tv" via Email
	Preconditions -  
	Prioroty -High
	Severity: -Critical
	Test Steps: 1.Open site "Twitch.tv"
				2.Click "Sign Up" button
				3.Choose registration via Email
				4.Input "Username", "Password","DateOfBirth","Email"
				5.Click "Sign Up" button
	Expected Results: Button occurs "Remind Me Later"
2.Title: Button "Following"
	Description -To check if Follow(e.g. Subscribe(Youtube)) button works 
						correctly and displayed in Followed_Channels(e.g Subscriptions(Youtube_Tab))
	Preconditions - Logged In
	Prioroty -Medium
	Severity -Major
	Test Steps: 1.Open "Twitch.tv"
				2.Click First Stream
				3.Click "Follow" Button
				4.Reload page
	Expected Results: Followed channel is appeared in followed channels list.
3.Title: Send Message in Chat 
	Description -To check if chat message(e.g. Comments(Youtube)) is sent to server
	Preconditions - Loggen In, Verified account
	Prioroty -Medium
	Severity -Major
	Test Steps: 1.Open "Twitch.tv"
				2.Click First Stream
				3.Click "Follow" Button
				4.Click chat
				5.Write text
				6.Click "Chat" button
	Expected Results: The sent Text appears in the shared chat 
4.Title: Send Report 
  	Description -To check if report button works
  	Preconditions -Logged In
  	Prioroty -Medium
  	Severity -Major
	Test Steps: 1.Open "Twitch.tv"
       			2.Click First Stream
		        3.Click more options(3 dots) button under Subscribe button
		        4.Click "Report Livestream" button
		        5.Click option "Spam, Scams, or Bots"
		        6.Click "Next" button
		        7.Click option "Spam"
		        8.Click "Next" button
		        9.Write message in the "Tell Us More" text area
		        10.Click "Submit Report" button
  	Expected Results: It will display "Thank you for submitting your report" text
5.Title: Channel Points 
	Description -To check if channel points can increase through watching stream
	Preconditions -Loggen In
	Prioroty -
	Severity -
	Test Steps: 1.Open "Twitch.tv"
				2.Click First Stream
				3.Wait for atleast 5 minutes
	Expected Results: Under chat area current channel points are increased by 10 points.
6.Title: Spend Channel Points
	Description -To check if we can spend channel points
	Preconditions -Logged In, Have Channel Points
	Prioroty -
	Severity -
	Test Steps: 1.Open "Twitch.tv/iltw1" 
				2.Click "Channel Points" button(Under Chat Area)
				3.Purchase any "Highlight my message" product
				4.Write text in chat area
				5.Click "Chat" button
	Expected Results: The current channel points should be decreased after purchasing reward.
7.Title: Add Stream and Delete(Schedule)
	Description -To check if we can add stream schedule and delete it
	Preconditions -Logged In
	Prioroty -
	Severity -
	Test Steps:	1.Open "Twitch.tv"
				2.Click User Icon
				3.Click "Settings" 
				4.Click "Channel and Videos" 
				5.Click "Schedule" 
				6.Click "Add Stream" 
				8.Click "Every Monday" for Frequency
				9.Click "Save Changes"
	Expected Results: "Every Monday - 11:00 AM - 3:00 PM GMT+5" text will appear
8.Title: Check if Stream is started
	Description -To check if stream sevice can work properly
	Preconditions -Logged In, OBS, StartStream
	Prioroty -
	Severity -
	Test Steps: 1.In OBS click start stream
				2.Open Your Twitch account
	Expected Results: The stream should be started and we can view the livestream
9.Title: Ban 
	Description -To check if ban function works properly
	Preconditions -Logged In,2 accounts(sl1meiscsgo and dondoni0413)
	Prioroty -
	Severity -
	Test Steps: "dondoni0413":
					1.Open "Twitch.tv/sl1meiscsgo"
					2.Click "Chat" 
					3.Write text in Chat area 
					4.Click "Chat" button
				"sl1meiscsgo":
					1.Open "Twitch.tv/sl1meiscsgo"
					2.Click "Chat"
					4.Find "message"
					5.Click User of Message
					6.Click "Ban" button looks like stop sign
	Expected Results: "dondoni0413" banned in the chat
10.Title: Edit Panels
	Description -To check if you can edit panels function works properly 
	Preconditions -Logged In 
	Prioroty -
	Severity -
	Test Steps: 1.Open Your Twitch account
				2.Click "Chat"
				3.Click "Edit Panels"
				4.Scrol down
				5.Click giant plus
				6.Click "Add a Text or image panel"
				7.Write title
				8.Click "Submit"
				9.Refresh page 
	Expected Results: About page will have a new panel with text 
