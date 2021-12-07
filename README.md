** CSGO Proof Of Concept: **

Installation:
To run the CS:GO proof of concept code there a few applications that need to be installed on the sender machine -
1. Steam Client
2. Counter Strike : Global Offensive
3. CS:GO SDK
Steam can be installed here -
https://store.steampowered.com
CSGO can be found here -
https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/
For the CSGO SDK, a prime account is required which can be acquired for $14.99. The purchase can be made on the CS:GO page linked above.The CS:GO SDK can be located on the Steam client by clicking on the tools section and then scrolling down to the SDKs section.
Note: The Hammer Editor and the SDK works best with a Windows system. At this time it cannot be confirmed if the editor would work on a Linux/Unix system.
Building A Map:
Map creation is a fairly complex process. Since maps can be built to the creators taste links can be found for creating/building maps here rather than specific instructions on how this project was built -
First Map Creation -
https://developer.valvesoftware.com/wiki/Your_First_Map
Counter Strike Level Creation -
https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Level_Crea tion
The base map for this project was created using this youtube video -
https://www.youtube.com/watch?v=dhcoHQcrYKA
      
Message Encoding:
For the message encoding the following steps need to be followed -
1. An entity is placed on the map with class “info_player_terrorist”.
2. For ease of use the entity can be named based on their order in the message i.e. first
bot can be named “first”, second bot “second” and so on. This can be accessed by
double clicking on the entity or hitting “CTRL +T”.
3. If this is the first bot on the map, set “EnabledbyDefault” as “Yes”.
4. For the next bot (and all subsequent bots) on the map, set “EnabledbyDefault” as “No”.
5. To create the trigger logic, select the block tool with the texture “Trigger” and place a
block that just about covers the first bot.
6. Change the function to “Trigger_multiple” by hitting “CTRL +T” on the trigger.
7. In the outputs tab of the trigger entity, add a new row and fill in the following details -
Output name - OnEndTouch Target entities named - first Via this input - SetDisabled After delay of - 0.0 seconds
And enable the “fire once only” field. This will disable the bot once it has been shot
down.
8. Add another row in the outputs tab with -
Output name - OnEndTouch Target entities named - second Via this input - SetEnabled After delay of - 0.0 seconds
And enable the “fire once only” field. This will enable the next bot once the previous bot has been shot down.
9. Repeat steps 4-8 appropriately changing the names in the bot’s “name” and trigger’s “Target entities named” fields depending on the order of the bots.
For more help on triggers - this video might be helpful -
https://www.youtube.com/watch?v=IUOA0JlihIQ
 
Map Publication:
1. To publish the map, open CS:GO and access the console by clicking on “~”.
2. In the console, enter “workshop_publish”.
3. Click map on the top right corner and click add on the bottom right.
4. Fill in all the map information and upload the bsp file and at least one screenshot of the
map. For game modes - select Casual, Competitive and Custom.
5. Click on the agreement statements and the map should be published successfully.
When a map is published for the first time it has to go through a Steam verification process and may take a few hours to complete - all subsequent updates to the map will take about 10 minutes or less.
Message Decoding:
To decode the map - the receiver must find the map on Steam’s community page found here -
https://steamcommunity.com/workshop/browse/?appid=730
Although that might be a long and tedious process, the easier option would be to go to the sender’s steam page and click on workshop items to view their map. My personal steam account can be found here -
https://steamcommunity.com/profiles/76561198349105403
Getting into the game -
1. Click on the map that needs to be decoded and click on “Subscribe”. The map should be
available in game now and can be accessed whenever the player wants to decode the
message.
2. Open up the game and click on the play button on the top left. This should display all the
different modes the game has to offer.
3. Click on Workshop Maps, select the map and hit on “Go” to start the game.
Setting up logs and cheats -
1. Select the Counter Terrorist team.
2. Open up console and type in the following commands one line at a time -
sv_cheats 1
bot_stop 1
mp_freezetime 0 mp_round_restart_deplay 0 log on
host_timescale 5
sv_infinite_ammo 1
ent_fire !picker addoutput “modescale 0”
3. Once everything is set up, start shooting down the bots.
4. Once all the bots have been eliminated the game will end with a rewards page. The
game can now be closed.
  
Python Script:
Once the logs have been collected from the game, a python script parses through these to decode the message from the map.
The following code snippet reads the logs one line at a time and checks the z-axis for the kill location. Since the bots are stationary, their spawn and death locations are the same.
while True:
overt_msg = f.readline() if not overt_msg:
break
if "TERRORIST" in overt_msg:
if "killed" in overt_msg:
message2 = overt_msg.split("\"") message = message2[4]
if "64] with" in message:
covert += "0" else:
covert += "1"
To run the code, change the file path on line three -
f = open("/*.log", "r")
The binary message should be printed on the screen.
